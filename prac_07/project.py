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
