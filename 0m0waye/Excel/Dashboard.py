import streamlit as slt
import pandas as pd
import plotly as px

slt.set_page_config(page_title = "Sales DashBoard",
page_icon = ":chart_with_upwards_trend:",
layout = "wide"
)
df = pd.read_excel(r'supermarkt_sales1.xlsx',
     #engine = 'openpyxl',
     #sheet_name = 'Sales'
     #skiprows = 3
     #usecols= "B:R",
     #nrows=1000
)

#slt.title("Sales DashBoard")
slt.sidebar.header("Please Filter Here: ")

slt.write("---")
#slt.dataframe(df)

city = slt.sidebar.multiselect(
"Select the City:",
options = df["City"].unique(),
default=df["City"].unique()
)

Ct = slt.sidebar.multiselect(
"Select the Customer Type:",
options = df["Customer_type"].unique(),
default=df["Customer_type"].unique()
)

G = slt.sidebar.multiselect(
"Select the Gender:",
options = df["Gender"].unique(),
default=df["Gender"].unique()
)
df_selection = df.query(
    "City == @city & Customer_type == @Ct & Gender == @G"
)


#slt.dataframe(df_selection)

slt.title(":bar_chart: Sales DashBoard")

slt.markdown("##")

total_sales = int(df_selection["Total"].sum())
average_rating = round(df_selection["Rating"].mean(),1)
star_rating=":star:" * int(round(average_rating,0))
average_slae_by_transaction = round(df_selection["Total"].mean(),2)

left_column,middle_column,right_column = slt.columns(3)
with left_column:
    slt.subheader("Total Sales: ")
    slt.subheader(f"NG #{total_sales:,}")

with middle_column:
    slt.subheader("Total Sales: ")
    slt.subheader(f"{average_rating}{star_rating}")

with right_column:
    slt.subheader("Average Sales Per Transaction: ")
    slt.subheader(f"NG 3{average_slae_by_transaction}")
slt.markdown("---")

#plotting bar Graph
sales_by_product_line = (
    df_selection.groupby(by=["Product line"]).sum()[["Total"]].sort_values("Total")
)
fig_product_slaes = px.bar(
    sales_by_product_line,
    x = "Total",
    y = sales_by_product_line.index,
    orientation = "h",
    title = "<b>Sales by Product Line</b>",
    color_discrete_sequence = ["#0083B8"] * len(sales_by_product_line),
    template= "plotly_white"
)

fig_product_slaes.update_layout(
    plot_bgcolor= "rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

#slt.plotly_chart(fig_product_slaes)

sales_by_hour=df_selection.groupby(by=["Hour"]).sum()[["Total"]]
fig_hourly_sales = px.bar(
    sales_by_hour,
    x = sales_by_hour.index,
    y = "Total",
    title = "<b>Sales by Hour</b>",
    color_discrete_sequence = ["#0083B8"] * len(sales_by_hour),
    template = "plotly_white"
)
fig_hourly_sales.update_layout(
    xaxis = dict(tickmode ="linear"),
    plot_bgcolor = "rgba(0,0,0,0)",
    yaxis=(dict(showgrid=False)),
)

left_column,right_column= slt.columns(2)
left_column.plotly_chart(fig_hourly_sales,use_container_width=True)
right_column.plotly_chart(fig_product_slaes,uses_container_width=True)



hide_st_style= """
                <style>
                #MainMen {visibility: hidden}
                footer{visibility: hidden}
                header{visibility: hidden}
                </style>
                """

slt.markdown(hide_st_style, unsafe_allow_html = True)
