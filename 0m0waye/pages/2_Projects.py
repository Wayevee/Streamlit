import streamlit as slt


slt.title("Projects")

slt.write("Welcome ",slt.session_state["my_input"]," to my Projects Page")

slt.subheader("The Project contains the visual correlation of a collection of Movie Data")
slt.markdown("[Click here to view](https://github.com/Wayevee/My-Projects/blob/main/Python%20Movies%20Project.ipynb)")
