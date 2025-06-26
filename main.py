import datetime
from models.company import Company
from models.position import Position
from models.application import Application
from services.csv_utils import export_application_data

company = Company("Tech Innovations", "123-456-7890", "email@gmail.com")
position = Position("Software Engineer", 80000, "Full-time", company)
application = Application(position, "Interviewing", "https://example.com/apply", datetime.date(2023, 10, 1))

application_list = [application]
export_application_data(application_list)