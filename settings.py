# Selenium
DRIVER_LOCATION = r'C:\selenium\webdriver\chromedriver.exe'
URL_CREATE = "https://slack.com/create"
TIME_WAIT = 30

# csv file
FILE_NAME_CSV = "emails.csv"

# PostreSQL
DATABASE_NAME = "brandon_slack"
DATABASE_USERNAME = "brandon_slack"
DATABASE_PASSWORD = "ibrlianhome"
DATABASE_HOST = 'localhost'
DATABASE_PORT = '5433'
URL_CONNECTION_TO_DATABASE = 'postgresql://{0}:{1}@{2}:{3}/{4}'\
    .format(DATABASE_USERNAME, DATABASE_PASSWORD, DATABASE_HOST, DATABASE_PORT,
            DATABASE_NAME)