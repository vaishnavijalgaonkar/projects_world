import streamlit as st
from datetime import date

st.title("📝 Simple To Do List App")

# Store tasks inside session state (temporary, no file saving)
if "tasks" not in st.session_state:
    st.session_state.tasks = []

if "rating" not in st.session_state:
    st.session_state.rating = None

# ---------------- Add Task Section ----------------
st.subheader("Add a Task")
task = st.text_input("Enter task")
due_date = st.date_input("Due date", value=date.today())

if st.button("Add Task"):
    if task != "":   # conditional
        st.session_state.tasks.append({"task": task, "date": due_date, "done": False})
        st.success("Task added successfully ✅")
    else:
        st.warning("Please enter a task first!")

# ---------------- Active Tasks ----------------
st.subheader("Active Tasks")
count = 1
for t in st.session_state.tasks:
    if not t["done"]:   # conditional
        st.write(f"{count}. {t['task']} (📅 {t['date']})")
        col1, col2 = st.columns(2)
        if col1.button("Mark Done", key=f"done{count}"):
            t["done"] = True
            st.rerun()
        if col2.button("Delete", key=f"delete{count}"):
            st.session_state.tasks.remove(t)
            st.rerun()
        count += 1

if count == 1:
    st.info("No active tasks.")

# ---------------- Completed Tasks ----------------
st.subheader("Completed Tasks")
count = 1
for t in st.session_state.tasks:
    if t["done"]:   # conditional
        st.write(f"{count}. {t['task']} (📅 {t['date']})")
        if st.button("Remove", key=f"remove{count}"):
            st.session_state.tasks.remove(t)
            st.rerun()
        count += 1

if count == 1:
    st.info("No completed tasks.")

# ---------------- Rating Section ----------------
st.subheader("⭐ Rate this App")
rating = st.radio("Select stars:", [1, 2, 3, 4, 5], horizontal=True)

if st.button("Submit Rating"):
    st.session_state.rating = rating
    st.success(f"Thanks! You rated this app: {'⭐' * rating}")

if st.session_state.rating:
    st.write("Your last rating:", "⭐" * st.session_state.rating)