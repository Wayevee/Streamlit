
import calendar
from datetime import datetime
import datetime
import streamlit as slt
from streamlit_option_menu import option_menu
import plotly.graph_objects as go
import DataBase as db

slt.set_page_config(
    layout= 'centered',
    page_title = "Income and Expenses Tracker",
    page_icon = ':money_with_wings:',
)

incomes = ["Salary","Blog","Other Inome"]
expenses = ["Rent","Utilities","Car","Other Expense","Saving"]
currency = "USD"
page_title = "Income and Expenses Tracker"

slt.title('Income and Expenses Tracker :money_with_wings: ')

year= [datetime.date.today().year -1 ,datetime.date.today().year]
month = list(calendar.month_name[1:])

def get_all_periods():
    items = db.fetch_all_periods()
    periods = [item["key"]for item in items]
    return periods


hide_slt_style = """
            <style>
            #ManiMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header{visibility: hidden;}
            </style>
            """
slt.markdown(hide_slt_style, unsafe_allow_html = True)


# Navigation Menue
selected  = option_menu(
menu_title = None,
options = ["Data Entry","Data Visualization"],
icons = ["pencil-fill", "bar-chart-fill"],
orientation = "horizontal",
)

if selected =="Data Entry":
    slt.header(f"Date Entry in {currency}")
    form = slt.form("entry form", clear_on_submit = True)
    with  form:
      col1,col2 = slt.columns(2)
      col1.selectbox("Select Month:",month, key = "month")
      col2.selectbox("Select Year:",year,key = "year")

      slt.write("---")
      with slt.expander("Income"):
          for income in incomes:
              slt.number_input(f"{income}:", min_value = 0,format="%i", step = 10,key=income)

      with slt.expander("Expense"):
          for expense in expenses:
              slt.number_input(f"{expense}:", min_value = 0, format ="%i",step=10, key=expense)
      with slt.expander("Comment"):
          comment = slt.text_area("", placeholder = "Enter a coment here ...")
      slt.write("---")
      submitted = form.form_submit_button("Save Data")



    if submitted:
     period = str(slt.session_state["year"]) + "_" + str(slt.session_state["month"])
     incomes = {income: slt.session_state[income] for income in incomes}
     expenses = {expense: slt.session_state[expense] for expense in expenses}
     db.insert_period(period, incomes, expenses,comment)
     slt.success("Data Saved")
if selected == "Data Visualization":
    slt.header("Data Visualization")
    with slt.form("saved_periods"):
        # TODO: Get Periods from database
        period = slt.selectbox ("Select Period:", get_all_periods())
        submitted = slt.form_submit_button("Plot Period")
        if submitted:

    #        TODO: Get data from database
             period_data = db.get_period(period)
             comment = period_data.get("comment")
             expenses = period_data.get("expenses")
             incomes = period_data.get("incomes")
             #Create metrics

             total_income = sum(incomes.values())
             total_expenses = sum(expenses.values())
             remaining_budget = total_income - total_expenses
             col1,col2,col3 = slt.columns(3)
             col1.metric("Total Income",f"{total_income}{currency}")
             col2.metric("Total Expenses",f"{total_expenses}{currency}")
             col3.metric("Remaining Budget",f"{remaining_budget}{currency}")
             slt.text(f"Comment: {comment}")
             #Create sankey plotly_chart
             label = list(incomes.keys()) + ["Total Income"] + list(expenses.keys())
             source = list(range(len(incomes))) + [len(incomes)] * len(expenses)
             target = [len(incomes)]* len(incomes) + [label.index(expense) for expense in expenses.keys()]
             value =list(incomes.values()) + list(expenses.values())

             link = dict(source = source, target = target,value =value)
             node = dict(label = label, pad = 15, thickness = 20, color = "#74b39c")
             data = go.Sankey(link =link, node=node)

             fig = go.Figure(data)
             fig.update_layout(margin = dict(l=0, r=0, t=5, b=5))
             slt.plotly_chart(fig,use_container_width = True)
