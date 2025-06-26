class Company:
    """
This class holds information about the company being applied to,
such as the name, contact phone number, and contact email."""

    def __init__(self, name, phone, email):
        """Initialize a Company instance with name, phone, and email."""
        self.name = name
        self.phone = phone
        self.email = email

    def __str__(self):
        return f"Company: {self.name}, Phone: {self.phone}, Email: {self.email}"