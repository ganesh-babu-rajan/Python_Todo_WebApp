import streamlit as st
import fileReader as files

todos = files.get_todos()

def add_todo():
    todo = st.session_state["new_todo"]
    todo = todo + "\n"
    todos.append(todo)
    files.write_todos(todos)

st.title("My Todo App")
st.header("This is my simple TODO app")
st.write("This appis to increase your productivity")

for index, item in enumerate(todos):
    checkbox = st.checkbox(item, key="box"+str(index))
    if checkbox:
        todos.pop(index)
        files.write_todos(todos)
        del st.session_state["box"+str(index)]
        st.rerun()

st.text_input(label="enter your todo item",
              placeholder="Add new todo...",
              on_change=add_todo,
              key="new_todo")