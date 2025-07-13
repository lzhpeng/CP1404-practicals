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
