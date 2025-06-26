class Position:
    """
This class holds information about the positon being applied for, like the title,
offered wage, type(part-time, full-time or internship), and company offering the position"""

    def __init__(self, title, wage, type, company):
        """Initialize a Position instance with title, wage, type, and company."""
        self.title = title
        self.wage = wage
        self.type = type
        self.company = company

    def __str__(self):
        return f"Position: {self.title}, Wage: {self.wage}, Type: {self.type}, Company: {self.company.name}"