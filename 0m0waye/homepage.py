import streamlit as slt
import pandas as pd


slt.set_page_config(
page_title = "Multipage App",
page_icon = ":dizzy:",
layout = "wide"
)
slt.title("Main Page")
slt.sidebar.success("Select a Page above.")


if "my_input" not in slt.session_state:
    slt.session_state["my_input"] = " "

my_input = slt.text_input("What is your Name? ", slt.session_state["my_input"])
submit = slt.button("Submit")
if submit:
    slt.session_state["my_input"] = my_input
    slt.write("Welcome!  ",my_input,", we are happy to have you...")
