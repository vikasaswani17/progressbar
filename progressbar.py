import streamlit as st

st.title("Progress Checklist")

# Define your tasks
tasks = [
    "Task 1",
    "Task 2",
    "Task 3",
    "Task 4"
]

st.header("Checklist")
completed = 0

# Create a checkbox for each task
for task in tasks:
    if st.checkbox(task):
        completed += 1

# Calculate progress percentage
progress_percentage = int((completed / len(tasks)) * 100)

st.write(f"Progress: {progress_percentage}%")
st.progress(progress_percentage)
