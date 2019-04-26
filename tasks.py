from browser import create_workspace
from database import Emails
from csv_file import CSVFile

emails = CSVFile().read_emails()
tasks = dict()
for email in emails[:1]:
    task = create_workspace.delay(email)
    tasks[email] = task.id

print(tasks)