# helper.py

# Placeholder task data (empty list)
tasks = [
    {'title': 'Complete Python Project', 'description': 'Finish the personal planner project using Python and Streamlit.', 'due_date': '2024-07-15', 'priority': 'High', 'completed': False},
    {'title': 'Prepare for Meeting', 'description': 'Review agenda and prepare notes for the upcoming team meeting.', 'due_date': '2024-07-14', 'priority': 'Medium', 'completed': False},
    {'title': 'Exercise', 'description': 'Go for a 30-minute jog in the morning.', 'due_date': '2024-07-13', 'priority': 'Low', 'completed': True},
    {'title': 'Read Book', 'description': 'Read the latest book from favorite author.', 'due_date': '2024-07-20', 'priority': 'Medium', 'completed': False}
]

def get_tasks():
    """
    Retrieve the list of tasks.
    
    TODO:
    - Return the `tasks` list.
    """
    pass

def add_task(title, description, due_date, priority):
    """
    Add a new task to the list.
    
    Args:
    - title (str): Title of the task.
    - description (str): Description of the task.
    - due_date (str): Due date of the task in 'YYYY-MM-DD' format.
    - priority (str): Priority level of the task ('High', 'Medium', 'Low').
    
    TODO:
    - Create a dictionary representing the new task.
    - Append the task dictionary to the `tasks` list.
    """
    pass

def filter_tasks_by_priority(priority):
    """
    Filter tasks by priority level.
    
    Args:
    - priority (str): Priority level to filter by ('High', 'Medium', 'Low').
    
    Returns:
    - filtered_tasks (list): List of tasks filtered by the specified priority.
    
    TODO:
    - Implement filtering logic to return tasks with matching priority.
    - Use list comprehension or another method to filter `tasks` list.
    """
    pass

def mark_task_completed(title):
    """
    Mark a task as completed.
    
    Args:
    - title (str): Title of the task to mark as completed.
    
    TODO:
    - Search for the task with the given title in the `tasks` list.
    - Update the 'completed' status of the matching task to True.
    - If no task is found with the given title, handle the scenario gracefully.
    """
    pass
