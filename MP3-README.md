<table><tr><td> <em>Assignment: </em> IS601 Mini Project 3  Business Management</td></tr>
<tr><td> <em>Student: </em> Akshitha Rao Annamaneni (aa3382)</td></tr>
<tr><td> <em>Generated: </em> 4/11/2023 5:42:11 AM</td></tr>
<tr><td> <em>Grading Link: </em> <a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-3-business-management/grade/aa3382" target="_blank">Grading</a></td></tr></table>
<table><tr><td> <em>Instructions: </em> <div>Initial Preperation:</div><div><ol><li>Create two new dynos/VMs in Heroku:</li><ol><li>is601-ucid-mp3-dev</li><li>is601-ucid-mp3-prod</li></ol><li>Configure the heroku config vars and github secrets similar to how dev/prod were setup</li><li>Create two new secrets for github and set the values per the machine names in step 1</li><ol><li>HEROKU_APP_MP3_DEV</li><li>HEROKU_APP_MP3_PROD</li></ol><li>Duplicate your dev/prod yml files and have it listen to the mp3-dev and mp3-prod branches respectively</li><ol><li>Make sure you refer to the proper app secrets from step 3</li><li>You can merge these into regular dev/prod later but you'll want your final project to deploy over it (overwrite) on the normal dev/prod dynos/VM</li></ol><li>You can add this HW branch to the dev yml to test your deployments prior to the pull request to dev from step 4</li></ol></div><div><br></div><div><br></div><ol><li>checkout dev and pull any latest changes</li><li>Create a branch called mp3-prod and immediately push it</li><li>Create a branch called mp3-dev and immediately push it</li><li>Create a branch called MiniProject-3</li><li>Add all the baseline files first under a folder called BusinessManagement (included below)</li><li>Don't forget to copy your .env file from flask_sample into BusinessManagement</li><li>source the venv and pip install the requirements.txt</li><li>Run the BusinessManagement/sql/init_db.py script</li><li><b>Immediate add/commit/push to github</b></li><li>Open a pull request to mp3-dev and keep it open until you're done adding the submission file</li><li>Make your code changes per the following requirements</li><ol><li>Important: run the test files indiviudally as you're working/testing to save on query quota usage</li><li>&nbsp;pytest BusinessManagement/test/name_of_test.py -rA</li></ol><li>Add/commit periodically (recommended after you implement a TODO item or checlist item and add a related commit message for clarity)<br></li><ol><li>Do not delete any provided comments</li></ol><li>Anywhere relevant add your ucid and the date you added the code (best to do this as you go)</li><li>You'll be capturing website screenshots from dev and code snippet screenshots (ensure you upload these properly as pull request comments to the pull request from step 10</li><ol><li>Note: You don't need separate screenshots for each checklist item, when possible it's recommended to try to capture multiple items together and reuse the image</li><li>Ensure all screenshots are properly captioned in the deliverable section so it's clear what part you're trying to show</li></ol><li>Once done, copy the markdown or download the md file and save it under the BusinessManagement folder</li><li>Do a final add/commit/push</li><li>Verify everything looks ok in the pull request</li><li>Merge the pull request</li><li>Make a new pull request from mp3-dev to mp3-prod and merge it</li><ol><li>If you want to keep original dev/prod up to date you can merge the changes into those, but they will cause a deploy to occur for each so be mindful</li></ol><li>Navigate to the submission file under the BusinessManagement folder from mp3-prod</li><li>Copy the github url to the exact file and submit it to Canvas</li></ol><div>You'll be implementing a basic Business Management site.</div><div>There will be some provided files fully working as-is and some skeleton files you'll need to fill in.</div><div>The files you need to fill in will have TODO items or comments mentioning what's expected.</div><div>Some files will have "DO NOT EDIT" mentioned, please don't edit these. If there's a doubt about any of them ask.</div><div>There are provided test case files too that all must be passing for full credit. Do not edit these test case files.</div><div>If a test case isn't possible to complete, capture the failed test case locally via `pytest BusinessManagement -rA` first, then you can rename the function to `off_original_name`.</div><div>The site will handle CRUD operations for Companies and Employees as well as allowing import of Company/Employee data via a csv file.</div><div>Note: db.py has been updated to use pymysql instead of mysql-connector-python to aid in easier queries.</div><div><br></div><div>Baseline files:&nbsp;<a href="https://github.com/MattToegel/IS601/tree/F23-MiniProject-3">https://github.com/MattToegel/IS601/tree/F23-MiniProject-3</a>&nbsp;</div><div>May want to download branch as a zip, then copy/paste the files into your repo (if/when you do, please immediately do a git add/commit to record the baseline items)</div><div><br></div><div>Provided files you don't need to edit:</div><div><ul><li>000_create_table_companies.sql</li><li>001_create_table_employees.sql</li><li>db.py</li><li>init_db.py</li><li>flash.html</li><li>company_dropdown.html</li><li>country_state_selector.html</li><li>upload.html</li><li>sort_filter.html</li><li>all test files</li><li>geography.py</li><li>__init__.py (remains empty)</li><li>Dockerfile</li><li>main.py</li><li>index.py</li></ul><div>All other files likely have requirements to fill in.</div></div><div><br></div></td></tr></table>
<table><tr><td> <em>Deliverable 1: </em> Identity Edits and Setup </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of the index page being displayed (from dev)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/230985152-d1767be8-bf77-4478-8892-17cfcf3f9fb7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Index page screenshot from dev<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add screenshot from the DB extension of vs code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/230986873-2d4b7ce1-6335-467b-b9e8-4f5eec63cd43.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Populated IS601_MP3_Companies table <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/230987135-d162404d-ce87-4bf7-b729-357360e921cf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Populated IS601_MP3_Employees table<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 2: </em> Upload / Import CSV File (provided data.csv) </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Add screenshot of /import route (code)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/230989156-6fcf3bae-5fe1-4317-b8d7-9ac7da4b0e72.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Checking whether file is .csv or else flash message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/230989578-d440c870-0854-4ab8-98ca-7253afbaa347.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Reading csv file as dictionary<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/230989953-520e636b-ed04-4b78-bc21-bcf6009d5b67.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Extracting employee &amp; company data and appending to list<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/230990309-bd3c04cc-e259-405c-ba6c-cb2740b31a9a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Flash messages about employee &amp; company loaded<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of the website when uploading the data.csv file</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/230994426-1e6c4e45-6d72-4a75-9bbf-e6af63b73469.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success along with count message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/230994864-049c54e1-2912-4f9c-9183-0053f783fb03.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Submitted without csv file error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/230995108-5a45ceba-f363-4f88-81c3-0963b88772fc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Error message to upload only csv file<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data (basic summary/view)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/230995923-114d59d9-945b-4f42-93ee-f6aa16ed288a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>I have uploaded sample data as shown in screenshots of subtask 2, correspondingly<br>here are the messages in terminal showing employees and company data inserted<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 3: </em> Add Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/230997905-f0558790-482c-4d15-a221-04bbce7dd687.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Regular expression for email format, flashing warning messages if missing, no condition for<br>company<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/230998464-5d595f7d-e2f8-484c-a8d5-2569bb7d99aa.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Flashing success or error message upon adding employee<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/230998884-1af8ba50-cb6c-4ee1-8558-da09c49d6c0e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/230999045-a80e6959-9feb-4adb-a7c7-b8a4ccf087e2.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Success message upon addition of employee<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/230999199-2b19b027-9acc-43fc-be2c-e57d0233bee4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>First name, last name, email error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new employee DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/230999675-5196e147-3e96-4515-a4a8-879ec9b4cdcb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>I have sorted the DB to show the recent created timestamp &amp; the<br>first one is the newly created employee as shown in subtask 2 with<br>id 2993 - FIRST NAME<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 4: </em> List/search Employees </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231000339-0ef7cf2f-5fb4-45ab-be30-0f79911f23c1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Retrieve employee id as id, first_name, last_name, email, company_id, company_name &amp; get fn,<br>ln, email, company, column, order, limit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231000661-2d927843-3415-43f3-a05f-f8a150819c25.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>filters, sorting, limit generation &amp; out of bounds error mes<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231001178-935a6f1a-073a-425b-828e-a37dd4f98876.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>First name filter as &#39;art&quot;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231001341-9d5e11c8-b4d9-40a4-bd2a-b3402ca06910.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Second name filter as &#39;ben&#39;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231001507-f3dc2e7f-7797-45a4-a7b5-3760d8718c51.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Email filter as &#39;@gmail&#39;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231002100-b0a6aeb2-ed6c-49c1-8af2-1a1401210724.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>company filter as &#39;20 20 printing&#39;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231001860-fd212127-02a6-43cb-a44a-734faba62ac4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>First name ascending filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231002011-f12abeab-415d-4854-ad74-34a46c9c08f0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>First name descending filter<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 5: </em> Edit Employee </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231002477-971227df-4817-4457-8d29-66242b2d8641.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Employee id request with flash error message, retrieving data by using request.form.get()<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231002956-7c19fc4e-2672-4a54-9657-3903fafb5ad0.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>First name, last name, email checking with flash error &amp; also checking email<br>format with reg ex<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231003191-38ecf20e-c88f-47a4-b9a9-8855a009efba.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>SQL query to update and show error if anything went wrong<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231003547-cb062025-49d4-4cf6-a229-e77d341dc973.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Fetching data &amp; showing error message message if not went as planned<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231022092-360f27ca-28d6-461f-9aa6-e19970bd973c.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>before<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231022210-223ed7e4-93a8-4562-a82b-239e9e025b52.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After swapping first name with last name (Rebecca Didio became Didio Rebecca)<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of employee data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231022501-0bb61442-041f-4939-a2a1-050471abbe65.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Rebecca Didio will be swapped first name with second name for edit<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231022351-63d5dff5-cc80-4460-9ccb-8b834d0de591.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After editing name changed to Didio Rebecca<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 6: </em> Add company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /add route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231005620-7a6f113b-0754-4a99-b0a8-da207c1de139.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>request.form.get() to retrive name, address, city etc &amp; flash if its required field<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231005862-b4f66b68-94c2-4141-b31f-c36b6c849a06.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>flash error if country, zipcode is not entered. Insert query and making it<br>user friendly showing exception via printf()<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231007249-653acda8-d610-425b-a1ca-fdc0247b2bf1.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Validating state &amp; country using pycountry package<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for add company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231021320-965c2036-b811-404f-8f31-abcf55d073b7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Valid data prior to submission<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231008656-e7c57cd7-07db-469e-bcca-3c40de898903.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Various error messages<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231021355-3ae3f478-f920-4212-86a6-424d1b97e280.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Succesfully added new company<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of new company DB record from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231021429-40a2383d-2e52-449a-83b3-128070acf0a7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>database showing test-company-123 updated in list (see recent modified time)<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 7: </em> List/Search Comapny </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /search route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231009208-a0dae3fc-fe7b-4e53-9e2e-9d6bf6c62124.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Query to retrieve the details of company &amp; request.args.get() to get the details<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231009455-da10fbcf-0250-4927-a158-d9abcb24ab67.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Appending life filters &amp; equality filters and sorting<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231010060-0d0b9b98-26a7-451d-a82a-a15e9549c4cc.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>keeping the limits &amp; producing error message<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for search company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231010233-cf5b8858-bf3b-4e20-b660-10f273a4a66d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Name filter &#39;ch&#39;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231011719-4e9f9a6c-780b-4692-9166-986f3beeba1d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Country filter<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231011924-9d81423a-1270-47ab-8c21-f7befa2d5b7d.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>state filter &#39;hawaii&#39;<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231012550-f461f2f0-1dec-4c0d-88b3-ec7265e71fde.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Ascending cities<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231012437-e086f67b-1c91-4050-b74a-c5332ce0d7e4.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Decending cities<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 8: </em> Edit Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshots of code for /edit route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231012867-bf339a7e-6ba3-4d89-966c-cee3bfff5d6a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>request.form.get() to get details<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231013046-3b23c6e9-1c93-4a47-b947-c834ec642d8a.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Required fields and flash error messages, checking is valid for states and countries<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231013220-a9214dfa-7a84-40af-9ded-819ac8cc8ba7.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>veryfying country and zipcode using pycountry<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231013459-23d4b6ae-b0d9-47b3-b6c7-82b740d3adfb.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Update query and error message<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231013553-9ed00cb3-2e80-4954-8be6-0848d1d4b62e.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Fetch updated data using DB.selectOne &amp; error message if process didnt go well<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Screenshots of website for edit company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231013895-6ea0b2fd-8b22-40e9-9ad8-9f1284e24638.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Number of company in Schott fiber optic is 2 before <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231014161-1c9eddc0-88c3-4dbf-a2cc-11cbc231f9f8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Name of company is &#39;Modified Schott fiber optic&quot;<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshots of DB data before and after of company  data edit from VS Code / IDE</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231014444-4545c4be-e2dc-4567-b588-f5058844bb90.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Database showing modified fiber optic being displayed (due to ascending of recent modifying<br>filter) <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231014742-ceb7948b-b648-4d96-871c-96a9f87cfd30.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Databse showing Fiber optic company, it will be changed to Modified fiber Optic<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 9: </em> Delete Employee and Delete Company </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot of code for /delete route of employee</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231015602-818008ae-c084-44ad-8598-34a7f4753fbf.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Using DB.delete and query to delete, error message, redirect to employee search<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Add a before and after website screenshot of deleting an employee (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231020259-1bc0a8f6-551f-4e82-a024-1d53a8058dec.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>1682	Mariko	Stayer	<a href="mailto:&#x6d;&#x61;&#114;&#x69;&#x6b;&#x6f;&#95;&#115;&#x74;&#97;&#121;&#x65;&#114;&#64;&#104;&#111;&#116;&#109;&#x61;&#105;&#x6c;&#x2e;&#x63;&#111;&#x6d;">&#x6d;&#x61;&#114;&#x69;&#x6b;&#x6f;&#95;&#115;&#x74;&#97;&#121;&#x65;&#114;&#64;&#104;&#111;&#116;&#109;&#x61;&#105;&#x6c;&#x2e;&#x63;&#111;&#x6d;</a>	7036 will be deleted <br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231020478-4aafafa6-5a3c-4215-982d-1297cc4ec3c8.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Mariko Stayer successfully deleted<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 3: </em> Screenshot of code for /delete route of company</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231020825-b5e8c592-9a85-41ab-8354-0d1b59db4c92.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Requrest args to get id, then update it with DB.update, exception to flash<br>error, redirect to company search <br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 4: </em> Add a before and after website screenshot of deleting a company (search results)</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231021039-99ed3ba5-f639-4013-bd59-95a1bf8d7d7f.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>Before deletion of Feltz Printing Service	639 Main St	Anchorage	US	AK	99501<br></p>
</td></tr>
<tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231021197-d18550ac-3bc3-48a5-a787-b562843bb935.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>After succesful deletion of Feltz Printing Service	639 Main St	Anchorage	US	AK	99501<br></p>
</td></tr>
</table></td></tr>
</table></td></tr>
<table><tr><td> <em>Deliverable 10: </em> Test Cases and Misc </td></tr><tr><td><em>Status: </em> <img width="100" height="20" src="https://user-images.githubusercontent.com/54863474/211707773-e6aef7cb-d5b2-4053-bbb1-b09fc609041e.png"></td></tr>
<tr><td><table><tr><td> <em>Sub-Task 1: </em> Screenshot Test case Results</td></tr>
<tr><td><table><tr><td><img width="768px" src="https://user-images.githubusercontent.com/123113065/231019949-085415b5-bbe3-4970-8003-6ad6bc7ce8f5.png"/></td></tr>
<tr><td> <em>Caption:</em> <p>The results dont explicitly show pass or fail, but in general if they<br>failed then there will be a failed message, else ........... indicates a pass<br></p>
</td></tr>
</table></td></tr>
<tr><td> <em>Sub-Task 2: </em> Issues / Learnings / Interesting things to note</td></tr>
<tr><td> <em>Response:</em> <p>This course helped me a lot to do<br></p><br></td></tr>
</table></td></tr>
<table><tr><td><em>Grading Link: </em><a rel="noreferrer noopener" href="https://learn.ethereallab.app/homework/IS601-004-S23/is601-mini-project-3-business-management/grade/aa3382" target="_blank">Grading</a></td></tr></table>
