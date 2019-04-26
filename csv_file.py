import csv

from settings import FILE_NAME_CSV

class CSVFile:
    def __init__(self):
        self.csv_file = open(FILE_NAME_CSV)

    def read_emails(self):
        emails = [row[0] for row in csv.reader(self.csv_file)]
        return emails

    def __del__(self):
        self.csv_file.close()

if __name__ == "__main__":
    csv_file = CSVFile()
    print(csv_file.read_emails())
