import time
import streamlit as st

# Task List
tasks = ["Reading", "Playing", "Homework"]

# Streamlit UI
st.title("Maya - Smart Scheduler")
rejected_count = {task: 0 for task in tasks}

task = st.selectbox("Choose a task:", tasks + ["Do Nothing"])
if not st.session_state.get("task_running", False):
    if st.button("Start Task"):
        if task == "Do Nothing":
            st.write("Taking a break... No task selected.")
        else:
            st.session_state["task_running"] = True
            st.session_state["start_time"] = time.time()
            st.session_state["current_task"] = task
            st.session_state["elapsed_time"] = 0

if st.session_state.get("task_running", False):
    st.session_state["elapsed_time"] = int(time.time() - st.session_state["start_time"])
    st.write(f"Time elapsed: {st.session_state['elapsed_time']} seconds")
    
    col1, col2 = st.columns(2)
    action = st.radio("Select an action:", ["Done", "Leave"], horizontal=True)
    if st.button("Confirm Action"):
        if action == "Done":
            st.write(f"{st.session_state['current_task']} completed!")
        else:
            st.write(f"{st.session_state['current_task']} abandoned!")
        st.session_state["task_running"] = False
    
    # Force UI update every second
    time.sleep(1)
    st.rerun()