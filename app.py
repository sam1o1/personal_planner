# app.py

import streamlit as st
from datetime import datetime
from helper import get_tasks, add_task, filter_tasks_by_priority, mark_task_completed

# Page title and sidebar
st.title('Personal Planner')
st.sidebar.title('Task Management')

# Get task data from helper.py
tasks_data = get_tasks()

# Display priority filter dropdown
priority_filter = st.sidebar.selectbox('Filter by Priority', ['All', 'High', 'Medium', 'Low'])

# Function to display task details
def display_task_details(task):
    st.subheader(task['title'])
    st.write(f"**Description:** {task['description']}")
    st.write(f"**Due Date:** {task['due_date']}")
    st.write(f"**Priority:** {task['priority']}")
    if task['completed']:
        st.write("**Status:** Completed")
    else:
        st.write("**Status:** Pending")

# Main content area
st.subheader('Task List')
if priority_filter != 'All':
    filtered_tasks = filter_tasks_by_priority(priority_filter)
    for task in filtered_tasks:
        display_task_details(task)
else:
    for task in tasks_data:
        display_task_details(task)

# Add new task section
st.sidebar.title('Add New Task')
new_task_title = st.sidebar.text_input('Task Title')
new_task_description = st.sidebar.text_area('Task Description')
new_task_due_date = st.sidebar.date_input('Due Date')
new_task_priority = st.sidebar.selectbox('Priority', ['High', 'Medium', 'Low'])

if st.sidebar.button('Add Task'):
    if new_task_title and new_task_description and new_task_due_date and new_task_priority:
        add_task(new_task_title, new_task_description, new_task_due_date.strftime('%Y-%m-%d'), new_task_priority)
        st.sidebar.success('Task added successfully!')
    else:
        st.sidebar.error('Please fill in all task details.')

# Mark task as completed section
st.sidebar.title('Mark Task as Completed')
task_to_complete = st.sidebar.selectbox('Select Task', [task['title'] for task in tasks_data if not task['completed']])
if st.sidebar.button('Mark as Completed'):
    if task_to_complete:
        mark_task_completed(task_to_complete)
        st.sidebar.success(f'Task "{task_to_complete}" marked as completed!')
    else:
        st.sidebar.error('Please select a task to mark as completed.')
