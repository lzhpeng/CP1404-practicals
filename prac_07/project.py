import datetime


class Project:
    """Represents a project with name, date, priority, cost and completion"""

    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """Initialize project with all attributes"""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return formatted string representation of project"""
        return (f"{self.name}, start: {self.start_date}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion_percentage}%")

    def __lt__(self, other):
        """Compare projects by priority for sorting"""
        return self.priority < other.priority

    def is_completed(self):
        """Check if project is 100% complete"""
        return self.completion_percentage == 100

    def get_date_object(self):
        """Convert start_date string to datetime.date object"""
        try:
            return datetime.datetime.strptime(self.start_date, "%d/%m/%Y").date()
        except ValueError:
            return None

    def is_after_date(self, date_string):
        """Check if project starts after given date"""
        try:
            project_date = datetime.datetime.strptime(self.start_date, "%d/%m/%Y").date()
            filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            return project_date >= filter_date
        except ValueError:
            return False