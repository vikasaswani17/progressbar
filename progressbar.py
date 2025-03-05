import streamlit as st

st.title("Editable Progress Checklist")

# Initialize tasks in session_state if not already set
if "tasks" not in st.session_state:
    st.session_state.tasks = [
        {"text": "Task 1", "done": False},
        {"text": "Task 2", "done": False},
        {"text": "Task 3", "done": False},
        {"text": "Task 4", "done": False}
    ]

# Section to add a new task
st.subheader("Add a New Task")
new_task = st.text_input("New task", key="new_task_input")
if st.button("Add Task"):
    if new_task:
        st.session_state.tasks.append({"text": new_task, "done": False})
        st.session_state.new_task_input = ""  # Clear the input field

# Display the checklist with editable tasks
st.subheader("Checklist")
completed = 0

# Use an index-based loop for proper key management and deletion
for i in range(len(st.session_state.tasks)):
    task = st.session_state.tasks[i]
    cols = st.columns([0.1, 0.7, 0.2])
    # Checkbox to mark task as done
    done = cols[0].checkbox("", value=task["done"], key=f"done_{i}")
    # Editable text input for the task
    new_text = cols[1].text_input("", value=task["text"], key=f"text_{i}")
    # Delete button for the task
    if cols[2].button("Delete", key=f"delete_{i}"):
        st.session_state.tasks.pop(i)
        st.experimental_rerun()  # Rerun to update the list

    # Update the task in session_state
    st.session_state.tasks[i]["done"] = done
    st.session_state.tasks[i]["text"] = new_text

    if done:
        completed += 1

# Calculate progress
total_tasks = len(st.session_state.tasks)
progress_percentage = int((completed / total_tasks) * 100) if total_tasks else 0

st.write(f"Progress: {progress_percentage}%")
st.progress(progress_percentage)
