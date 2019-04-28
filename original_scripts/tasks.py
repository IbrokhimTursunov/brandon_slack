from original_scripts.browser import create_workspace
from original_scripts.database import Emails
from original_scripts.csv_file import CSVFile

emails = CSVFile().read_emails()
db = Emails()
db.insert_records(emails)
unused_emails = db.get_all_unused_emails()

tasks = dict()
for email in unused_emails:
    task = create_workspace.delay(email)
    db.mark_as_used(email)
    tasks[email] = task.id

