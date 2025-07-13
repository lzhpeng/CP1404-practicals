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
