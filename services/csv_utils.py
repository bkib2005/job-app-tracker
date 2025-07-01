import csv
import datetime
import logging
from models.company import Company
from models.position import Position
from models.application import Application


def load_application_data(file_name):
    """
This function loads application data from a given CSV file and returns a list of Applications."""
    applications = []
    try:
        with open(file_name, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                company = Company(row['company'], row['phone_number'], row['email_address'])
                position = Position(row['position'], float(row['wage']), row['type'], company)
                date_applied = datetime.datetime.strptime(row['date_applied'], '%Y-%m-%d').date()
                application = Application(position, row['status'], row['application_link'], date_applied)
                applications.append(application)
        return applications
    except Exception as e:
        logging.error(f"Error loading applications from CSV: {e}")

def export_application_data(applications, file_name='data/ExportData.csv'):
    """
    This function exports a list of application data to a .csv file."""
    try:
        with open(file_name, 'w', newline='') as csvfile:
            fieldnames = ['company', 'position', 'type', 'status', 'date_applied', 'wage', 'phone_number', 'email_address', 
                          'application_link']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for element in applications:
                position = element.position
                company = position.company
                writer.writerow({
                    'company': company.name, 'position': position.title, 'type': position.type, 'status': element.status, 
                    'date_applied': element.date_applied, 'wage': position.wage, 'phone_number': company.phone, 
                    'email_address': company.email, 'application_link': element.website
                })
    except Exception as e:
        logging.error(f"Error exporting applications to CSV: {e}")