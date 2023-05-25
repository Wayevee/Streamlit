import streamlit as slt
import pandas as pd


slt.set_page_config(
page_title = "Multipage App",
page_icon = ":dizzy:",
layout = "wide"
)
slt.title("Main Page")
slt.sidebar.success("Select a Page above.")

x = slt.slider("Select an integer x", 0, 10, 1)
y = slt.slider("Select an integer y", 0, 10, 1)
df = pd.DataFrame({"x": [x], "y": [y] , "x + y": [x + y]}, index = ["addition row"])
slt.write(df)

if "my_input" not in slt.session_state:
    slt.session_state["my_input"] = " "

my_input = slt.text_input("What is your Name? ", slt.session_state["my_input"])
submit = slt.button("Submit")
if submit:
    slt.session_state["my_input"] = my_input
    slt.write("Welcome!  ",my_input,", we are happy to have you...")
