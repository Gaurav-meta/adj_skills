1. Install Serverless framework from
https://www.serverless.com/framework/docs/getting-started/

2. Install AWS CLI from here:
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

3. Create a virtual env: (skip this step unless you want to create new venv)
python3 -m pip install --user virtualenv
python3 -m venv myapi

4. Skip creating the venv with same name, instead:
source myapi/bin/activate

5. Install boto (AWS SDK) in venv:
pip install boto3

6. Freeze your requirements.txt:
pip freeze > requirements.txt

7. Initialize npm using default options:
npm init

8. Install serverless python
npm install --save serverless-python-requirements

9. serverless.yml file already exists to setup the deployment
10. handler.py already exists to create a serverless function

11. Created a dynamo.py to dump dict to json

12. Created a file importToDynamo.py to import csv data into Dynamo table. The sample csv file has been named adjacentSkills.csv
This file has just three entries which have been derived from the spreadsheet which has a longer list of skills and their adjacent skills

The serverless api is throwing an error when I run "serverless deploy --verbose". It needs to be debugged. On success, it will create a serverless function which could be tested by going to the api gateway and calling the function called get. The same api could be tested using postman. You will need the account keys which are:
access key - AKIASSNJJZ4S4BYXYGPS
secret access key - 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

I have also donwloaded and stored the login credentials in AWS_sshekhar_credentials.csv   You can use this at the time of install AWS cli or use the keys provided above.

You can login as me in aws console:
shashank.s@entomo.co/@1Entomo
Do NOT use this account for any other service as its going to charge my card. Use it only for API related activities.

Search for IAM service, where you will notice that I have created a user called sshekhar. This user id is used by the python scripts.
Search for Dynamo service, where you will notice the table and the three records inserted by running the python script. You can add more data by inserting new rows and then run it from within the venv by calling python3 scriptname.


