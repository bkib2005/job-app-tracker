import csv
import datetime
import pytest

from services.csv_utils import load_application_data, export_application_data
from models.company import Company
from models.position import Position
from models.application import Application


def test_load_application_data():
    file_path = 'data/TestData.csv'
    applications = load_application_data(file_path)

    assert applications is not None, "Expected applications to be loaded from the test data file."
    assert len(applications) >= 5, "Expected at least 5 applications in the test data file."

    expected_values = [
        {
            "company": "Kwideo",
            "position": "Nuclear Power Engineer",
            "type": "Part-time",
            "status": "Rejected",
            "date_applied": datetime.date(2025, 1, 11),
            "wage": 15.0,
            "phone": "198-339-4555",
            "email": "ebalfour0@elpais.com",
            "link_start": "http://theguardian.com/"
        },
        {
            "company": "Zoozzy",
            "position": "Account Coordinator",
            "type": "Part-time",
            "status": "Interviewing",
            "date_applied": datetime.date(2024, 8, 23),
            "wage": 23.0,
            "phone": "966-823-6517",
            "email": "omaingot1@4shared.com",
            "link_start": "http://homestead.com/"
        },
        {
            "company": "Cogilith",
            "position": "Research Nurse",
            "type": "Part-time",
            "status": "Accepted",
            "date_applied": datetime.date(2025, 4, 3),
            "wage": 16.0,
            "phone": "658-978-0631",
            "email": "lfairley2@webeden.co.uk",
            "link_start": "https://constantcontact.com/"
        },
        {
            "company": "Reallinks",
            "position": "Environmental Specialist",
            "type": "Part-time",
            "status": "Interviewing",
            "date_applied": datetime.date(2024, 6, 23),
            "wage": 21.0,
            "phone": "527-947-7075",
            "email": "ngarrettson3@fotki.com",
            "link_start": "https://examiner.com/"
        },
        {
            "company": "Oyope",
            "position": "General Manager",
            "type": "Internship",
            "status": "Interviewing",
            "date_applied": datetime.date(2025, 1, 21),
            "wage": 23.0,
            "phone": "747-535-3893",
            "email": "kplain4@nytimes.com",
            "link_start": "http://spotify.com/"
        },
    ]

    for i in range(5):
        app = applications[i]
        expected = expected_values[i]

        assert app.position.company.name == expected["company"]
        assert app.position.title == expected["position"]
        assert app.position.type == expected["type"]
        assert app.status == expected["status"]
        assert app.date_applied == expected["date_applied"]
        assert app.position.wage == expected["wage"]
        assert app.position.company.phone == expected["phone"]
        assert app.position.company.email == expected["email"]
        assert app.website.startswith(expected["link_start"])


def test_export_application_data(tmp_path):
    # Create mock application
    company = Company("Test Inc", "999-888-7777", "contact@testinc.com")
    position = Position("DevOps Engineer", 85000.0, "Full-time", company)
    application = Application(
        position=position,
        status="Interview",
        website="https://jobs.testinc.com",
        date_applied=datetime.date(2025, 6, 15)
    )

    export_file = tmp_path / "TestExport.csv"
    export_application_data([application], file_name=export_file)

    # Verify CSV output
    with open(export_file, newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    assert len(rows) == 1
    row = rows[0]

    assert row['company'] == "Test Inc"
    assert row['position'] == "DevOps Engineer"
    assert row['type'] == "Full-time"
    assert row['status'] == "Interview"
    assert row['date_applied'] == "2025-06-15"
    assert row['wage'] == "85000.0"
    assert row['phone_number'] == "999-888-7777"
    assert row['email_address'] == "contact@testinc.com"
    assert row['application_link'] == "https://jobs.testinc.com"