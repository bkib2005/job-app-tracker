from datetime import date

class Application:
    """
    This class stores information about the application itself, like the position being applied for,
    the status of the application(no response, interviewing, rejected, accepted),
    and a link to the application website."""

    def __init__(self, position, status, website, date_applied: date):
        """Initialize an Application instance with position, status, website, and date applied."""
        self.position = position
        self.status = status
        self.website = website
        self.date_applied = date_applied

    def __str__(self):
        return f"Application for {self.position.title} at {self.position.company.name} - Status: {self.status}, Website: {self.website}, Date Applied: {self.date_applied}"