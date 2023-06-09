from flask import Blueprint, redirect, render_template, request, flash, url_for
from sql.db import DB
import pycountry
company = Blueprint('company', __name__, url_prefix='/company')


@company.route("/search", methods=["GET"])
def search():
    rows = []
    
    # TODO search-1 retrieve id, name, address, city, country, state, zip, website, employee count as employees for the company
    query = """
    SELECT companies.id, companies.name, companies.address, companies.city, companies.country, companies.state, companies.zip, companies.website, COUNT(employees.id) as employees 
    FROM IS601_MP3_Companies companies LEFT JOIN IS601_MP3_Employees employees ON companies.id = employees.company_id 
    WHERE 1=1
    """
    group_by_query = " GROUP BY companies.id, companies.name, companies.address, companies.city, companies.country, companies.state, companies.zip, companies.website"
    
    
    args = {}
    
    allowed_columns = [("name", "Name"), ("address", "Address"), ("city", "City"), ("country", "Country"), ("state", "State"), ("zip", "Zip"), ("Website", "Website"), ("employees","Employees")]
    
    # TODO search-2 get name, country, state, column, order, limit request args
    name = request.args.get("name")
    country = request.args.get("country")
    state = request.args.get("state")
    column = request.args.get("column")
    order = request.args.get("order")
    limit = request.args.get("limit")
    
    # TODO search-3 append a LIKE filter for name if provided
    if name:
        name_filter = f"%{name}%"
        query += " AND companies.name LIKE %(name_filter)s"
        args["name_filter"] = name_filter
    
    # TODO search-4 append an equality filter for country if provided
    if country:
        query += " AND companies.country = %(country)s"
        args["country"] = country
    
    # TODO search-5 append an equality filter for state if provided
    if state:
        query += " AND companies.state = %(state)s"
        args["state"] = state
    
    query += group_by_query
    
    # TODO search-6 append sorting if column and order are provided and within the allowed columns and allowed order asc,desc
    if column and order:
        if column in [col[0] for col in allowed_columns] and order.lower() in ["asc", "desc"]:
            query += f" ORDER BY {column} {order}"
    
    # TODO search-7 append limit (default 10) or limit greater than or equal to 1 and less than or equal to 100
    if limit:
        try:
            limit = int(limit)
            if limit < 1 or limit > 100:
                raise ValueError
        except ValueError:
            flash("Limit must be a number between 1 and 100", "danger")
        else:
            query += " LIMIT %(limit)s"
            args["limit"] = limit
    else:
        query += " LIMIT 10"
    

    print("query",query)
    print("args", args)
    try:
        result = DB.selectAll(query, args)
        if result.status:
            rows = result.rows
    except Exception as e:
        # TODO search-9 make message user friendly
        flash("An error occurred while searching for Companies.", "danger")
    
    return render_template("list_companies.html", rows=rows, allowed_columns=allowed_columns)


@company.route("/add", methods=["GET","POST"])
def add():
    if request.method == "POST":
        # TODO add-1 retrieve form data for name, address, city, state, country, zip, website
        # TODO add-2 name is required (flash proper error message)
        # TODO add-3 address is required (flash proper error message)
        # TODO add-4 city is required (flash proper error message)
        # TODO add-5 state is required (flash proper error message)
        # TODO add-5a state should be a valid state mentioned in pycountry for the selected state
        # hint see geography.py and pycountry documentation
        # TODO add-6 country is required (flash proper error message)
        # TODO add-6a country should be a valid country mentioned in pycountry
        # hint see geography.py and pycountry documentation
        # TODO add-7 website is not required
        # TODO add-8 zipcode is required (flash proper error message)
        # note: call zip variable zipcode as zip is a built in function it could lead to issues

        name = request.form.get("name")
        address = request.form.get("address")
        city = request.form.get("city")
        state = request.form.get("state")
        country = request.form.get("country")
        zip_code = request.form.get("zip")
        website = request.form.get("website")

        has_error = False # use this to control whether or not an insert occurs
        
        if not name:
            flash("Name is required", "danger")
            has_error = True
        
        if not address:
            flash("Address is required", "danger")
            has_error = True
        
        if not city:
            flash("City is required", "danger")
            has_error = True
        
        if not state:
            flash("State is required", "danger")
            has_error = True
        elif not is_valid_state(state, country):
            flash("Invalid state selected", "danger")
            has_error = True
        
        if not country:
            flash("Country is required", "danger")
            has_error = True
        elif not is_valid_country(country):
            flash("Invalid country selected", "danger")
            has_error = True
        
        if not zip_code:
            flash("Zipcode is required", "danger")
            has_error = True

        if not has_error:
            try:
                result = DB.insertOne("""
                INSERT INTO IS601_MP3_Companies (name, address, city, state, country, zip, website)
                VALUES (%(name)s, %(address)s, %(city)s, %(state)s, %(country)s, %(zip)s, %(website)s);
                """, {"name": name, "address": address, "city": city, "state": state, "country": country, "zip": zip_code, "website": website}) # <-- TODO add-8 add query and add arguments
                if result.status:
                    # TODO add-11 Proper INSERT query should be visible along with the data being inserted
                    flash("Added Company.", "success")
                    return redirect(url_for("company.add"))
            except Exception as e:
                # TODO add-9 make message user friendly
                print(str(e))
                flash("An exception occured while Adding the Company details!", "danger")
        
    return render_template("add_company.html")

def is_valid_state(state_code, country_code):
    try:
        # country = pycountry.countries.get(alpha_2=country_code)
        states = pycountry.subdivisions.get(country_code=country_code)
        valid_states = [state.code for state in states]
        if country_code + '-' + state_code in valid_states:
            return True
        return False
    except (KeyError, AttributeError):
        return False

def is_valid_country(country_code):
    try:
        pycountry.countries.get(alpha_2=country_code)
        return True
    except KeyError:
        return False

@company.route("/edit", methods=["GET", "POST"])
def edit():
    # TODO edit-1 request args id is required (flash proper error message)
    id = request.args.get("id")
    if not id: # TODO update this for TODO edit-1
        flash("Company ID is required.", "danger")
        return redirect(url_for("company.search"))
    else:
        if request.method == "POST":
            data = {"id": id} # use this as needed, can convert to tuple if necessary
            # TODO edit-1 retrieve form data for name, address, city, state, country, zip, website
            # TODO edit-2 name is required (flash proper error message)
            # TODO edit-3 address is required (flash proper error message)
            # TODO edit-4 city is required (flash proper error message)
            # TODO edit-5 state is required (flash proper error message)
            # TODO edit-5a state should be a valid state mentioned in pycountry for the selected state
            # hint see geography.py and pycountry documentation
            # TODO edit-6 country is required (flash proper error message)
            # TODO edit-6a country should be a valid country mentioned in pycountry
            # hint see geography.py and pycountry documentation
            # TODO edit-7 website is not required
            # TODO edit-8 zipcode is required (flash proper error message)
            name = request.form.get("name")
            address = request.form.get("address")
            city = request.form.get("city")
            state = request.form.get("state")
            country = request.form.get("country")
            zip_code = request.form.get("zip")
            website = request.form.get("website")

            has_error = False # use this to control whether or not an insert occurs

            # TODO edit-2 name is required (flash proper error message)
            if not name:
                flash("Name is required", "danger")
                has_error = True
            else:
                data["name"] = name
            
            # TODO edit-3 address is required (flash proper error message)
            if not address:
                flash("Address is required", "danger")
                has_error = True
            else:
                data["address"] = address
            
            # TODO edit-4 city is required (flash proper error message)
            if not city:
                flash("City is required", "danger")
                has_error = True
            else:
                data["city"] = city
            
            if not state:
                flash("State is required", "danger")
                has_error = True
            elif not is_valid_state(state, country):
                flash("Invalid state selected", "danger")
                has_error = True
            else:
                state = pycountry.subdivisions.lookup(country +'-'+state)
                data["state"] = state.code.split('-')[1]
                
            # TODO edit-6 country is required (flash proper error message)
            if not country:
                flash("Country is required", "danger")
                has_error = True
            elif not is_valid_country(country):
                flash("Invalid country selected", "danger")
                has_error = True
            else:
                country = pycountry.countries.search_fuzzy(country)[0]
                print(country)
                data["country"] = country.alpha_2
            
            data["website"] = website
        
            # TODO edit-8 zipcode is required (flash proper error message)
            if not zip_code:
                flash("Zipcode is required", "danger")
                has_error = True
            else:
                data["zip"] = zip_code
            

            # note: call zip variable zipcode as zip is a built in function it could lead to issues
            # populate data dict with mappings
            
            print(data)
            if not has_error:
                try:
                    # TODO edit-9 fill in proper update query
                    # name, address, city, state, country, zip, website
                    result = DB.update("""
                    UPDATE IS601_MP3_Companies
                    SET
                        name=%(name)s,
                        address=%(address)s,
                        city=%(city)s,
                        state=%(state)s,
                        country=%(country)s,
                        zip=%(zip)s,
                        website=%(website)s
                    WHERE
                        id=%(id)s
                    """, data)
                    if result.status:
                        print("updated record")
                        flash("Updated record", "success")
                except Exception as e:
                    # TODO edit-10 make this user-friendly
                    print(f"{e}")
                    flash("An error occurred while updating the Company record.", "danger")
        row = {}
        try:
            # TODO edit-11 fetch the updated data
            result = DB.selectOne("SELECT * FROM IS601_MP3_Companies WHERE id=%s", id)
            if result.status:
                row = result.row
                
        except Exception as e:
            # TODO edit-12 make this user-friendly
            flash("An error occurred while fetching the company record.", "danger")
    # TODO edit-13 pass the company data to the render template
    return render_template("edit_company.html", row=row)

@company.route("/delete", methods=["GET"])
def delete():
    # TODO delete-1 delete company by id (unallocate any employees see delete-5)
    # TODO delete-2 redirect to company search
    # TODO delete-3 pass all argument except id to this route
    # TODO delete-4 ensure a flash message shows for successful delete
    # TODO delete-5 for all employees assigned to this company set their company_id to None/null
    # TODO delete-6 if id is missing, flash necessary message and redirect to search
    id = request.args.get("id")
    if id:
        try:
            DB.update("UPDATE IS601_MP3_Employees SET company_id = NULL WHERE company_id = %(id)s", {"id": id})
            result = DB.delete("DELETE FROM IS601_MP3_Companies WHERE id = %(id)s;", {"id": id})
            if result.status:
                flash("Successfully deleted company.", "success")
        except Exception as e:
            flash("An error occurred while deleting the company record.", "danger")
            print(e)

        # TODO delete-3 pass all arguments except id to this route
        args = {k: v for k, v in request.args.items() if k != "id"}
        # TODO delete-2 redirect to employee search
        return redirect(url_for("company.search", **args))
    else:
        # TODO delete-5 if id is missing, flash necessary message and redirect to search
        flash("Company ID is required.", "danger")
        return redirect(url_for("company.search"))
    