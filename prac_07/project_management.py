"""
Project Management System
Estimated time: 3 hours
"""

import datetime
from project import Project


def load_projects(filename):
    """Load projects from tab-separated file"""
    projects = []
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            # Skip header line
            for line in lines[1:]:
                parts = line.strip().split('\t')
                if len(parts) == 5:
                    name = parts[0]
                    start_date = parts[1]
                    priority = int(parts[2])
                    cost_estimate = float(parts[3])
                    completion_percentage = int(parts[4])
                    
                    project = Project(name, start_date, priority, cost_estimate, completion_percentage)
                    projects.append(project)
        print(f"Loaded {len(projects)} projects from {filename}")
    except FileNotFoundError:
        print(f"File {filename} not found")
    except Exception as e:
        print(f"Error loading projects: {e}")
    return projects


def save_projects(filename, projects):
    """Save projects to tab-separated file"""
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            # Write header
            file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
            # Write projects
            for project in projects:
                file.write(f"{project.name}\t{project.start_date}\t{project.priority}\t"
                          f"{project.cost_estimate}\t{project.completion_percentage}\n")
        print(f"Saved {len(projects)} projects to {filename}")
    except Exception as e:
        print(f"Error saving projects: {e}")


def display_projects(projects):
    """Display projects grouped by completion status"""
    if not projects:
        print("No projects to display")
        return

    # Separate completed and incomplete projects
    incomplete_projects = [p for p in projects if not p.is_completed()]
    completed_projects = [p for p in projects if p.is_completed()]

    # Sort by priority
    incomplete_projects.sort()
    completed_projects.sort()

    print("Incomplete projects: ")
    for project in incomplete_projects:
        print(f"  {project}")

    print("Completed projects: ")
    for project in completed_projects:
        print(f"  {project}")


def filter_projects_by_date(projects):
    """Filter projects by start date"""
    if not projects:
        print("No projects to filter")
        return

    date_string = input("Show projects that start after date (dd/mm/yy): ")
    try:
        filter_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
        filtered_projects = []

        for project in projects:
            project_date = project.get_date_object()
            if project_date and project_date >= filter_date:
                filtered_projects.append(project)

        # Sort by date
        filtered_projects.sort(key=lambda x: x.get_date_object())

        for project in filtered_projects:
            print(project)

    except ValueError:
        print("Invalid date format. Please use dd/mm/yy")


def add_new_project(projects):
    """Add a new project with input validation"""
    print("Let's add a new project")
    name = input("Name: ")

    while True:
        start_date = input("Start date (dd/mm/yy): ")
        try:
            datetime.datetime.strptime(start_date, "%d/%m/%Y")
            break
        except ValueError:
            print("Invalid date format. Please use dd/mm/yy")

    while True:
        try:
            priority = int(input("Priority: "))
            break
        except ValueError:
            print("Please enter a valid number")

    while True:
        try:
            cost_estimate = float(input("Cost estimate: $"))
            break
        except ValueError:
            print("Please enter a valid number")

    while True:
        try:
            completion_percentage = int(input("Percent complete: "))
            if 0 <= completion_percentage <= 100:
                break
            else:
                print("Please enter a percentage between 0 and 100")
        except ValueError:
            print("Please enter a valid number")

    new_project = Project(name, start_date, priority, cost_estimate, completion_percentage)
    projects.append(new_project)
    print("Project added successfully!")


def update_project(projects):
    """Update an existing project's completion and priority"""
    if not projects:
        print("No projects to update")
        return

    # Display projects with indices
    for i, project in enumerate(projects):
        print(f"{i} {project}")

    while True:
        try:
            choice = int(input("Project choice: "))
            if 0 <= choice < len(projects):
                break
            else:
                print("Invalid choice")
        except ValueError:
            print("Please enter a valid number")

    project = projects[choice]
    print(project)

    # Get new completion percentage
    new_percentage = input("New Percentage: ")
    if new_percentage.strip():
        try:
            percentage = int(new_percentage)
            if 0 <= percentage <= 100:
                project.completion_percentage = percentage
            else:
                print("Percentage must be between 0 and 100")
        except ValueError:
            print("Invalid percentage")

    # Get new priority
    new_priority = input("New Priority: ")
    if new_priority.strip():
        try:
            priority = int(new_priority)
            project.priority = priority
        except ValueError:
            print("Invalid priority")


def main():
    """Main program with menu interface"""
    print("Welcome to Pythonic Project Management")

    # Load projects from default file
    projects = load_projects("projects.txt")

    while True:
        print()
        print("- (L)oad projects")
        print("- (S)ave projects")
        print("- (D)isplay projects")
        print("- (F)ilter projects by date")
        print("- (A)dd new project")
        print("- (U)pdate project")
        print("- (Q)uit")

        choice = input(">>> ").lower()

        if choice == 'l':
            filename = input("Enter filename to load from: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter filename to save to: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'f':
            filter_projects_by_date(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'q':
            save_choice = input("Would you like to save to projects.txt? ").lower()
            if save_choice in ['y', 'yes']:
                save_projects("projects.txt", projects)
            else:
                print("no, I think not.")
            print("Thank you for using custom-built project management software.")
            break
        else:
            print("Invalid choice")


if __name__ == "__main__":
    main()