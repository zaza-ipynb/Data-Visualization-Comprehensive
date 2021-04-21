# Muhammad Ihza Mahendra
# 1301174682


import pandas as pd
from bokeh.plotting import figure, output_file, show, save
from bokeh.models import ColumnDataSource, Panel, Tabs
from bokeh.models.tools import HoverTool


#Preparing the output file for browser 
output_file('stocks_chart.html')
#load dataset
df = pd.read_csv('stock_market.csv')
#Drop the missing values in the datasets
df.dropna(inplace=True)
#Make sure the format of column Date is data format
df["Date"]= pd.to_datetime(df["Date"])


#Dividing each column of stocks data
df_nikkei = df[df['Name']=='NIKKEI']
df_nasdaq = df[df['Name']=='NASDAQ']
df_hangseng = df[df['Name']=='HANG SENG']


#Creating canvas like as media for plot for Adj Close
grph_adj_close = figure(x_axis_type="datetime",
    x_axis_label="Date",
    y_axis_label="Price (in USD)",
    plot_width=1300,
    plot_height=700,
    title="Stocks Adj Closing Prices"
)

#Get column data source, read the APIs in the bokeh docs
#about ColumnDataSource
src_hangseng = ColumnDataSource(df_hangseng)
src_nikkei = ColumnDataSource(df_nikkei)
src_nasdaq = ColumnDataSource(df_nasdaq)

#Create the line plot for tab Adj Close
grph_adj_close.line(x='Date', y='Adj Close', source=src_nikkei, color='green', legend_label='Nikkei')
grph_adj_close.line(x='Date', y='Adj Close', source=src_hangseng, color='red', legend_label='Hang Seng')
grph_adj_close.line(x='Date', y='Adj Close', source=src_nasdaq, color='blue', legend_label='Nasdaq')

#Hover tool to give lighting of the stocks symbol name and value Adj Close
hover = HoverTool()
hover.tooltips = [('Stock', '@Name'), ('Adj Close', '@{Adj Close}')]
grph_adj_close.add_tools(hover)

grph_adj_close.legend.click_policy="hide"


#Creating canvas like media for Volume plot tab 
grph_Volume = figure(x_axis_type="datetime",
    x_axis_label="Date",
    y_axis_label="",
    plot_width=1300,
    plot_height=700,
    title="Stocks In Volume"
)

grph_Volume.line(x='Date', y='Volume', source=src_nikkei, color='green', legend_label='Nikkei')
grph_Volume.line(x='Date', y='Volume', source=src_hangseng, color='red', legend_label='Hang Seng')
grph_Volume.line(x='Date', y='Volume', source=src_nasdaq, color='blue', legend_label='Nasdaq')

hover = HoverTool()
hover.tooltips = [('Stock', '@Name'), ('Volume', '@Volume')]
grph_Volume.add_tools(hover)

grph_Volume.legend.click_policy="hide"


# Create canvas media like for daily percentage change 
grph_day_perc_change = figure(x_axis_type="datetime",
    x_axis_label="Date",
    y_axis_label="",
    plot_width=1300,
    plot_height=700,
    title="Stocks In Day Perc Change"
)

grph_day_perc_change.line(x='Date', y='Day_Perc_Change', source=src_nikkei, color='green', legend_label='Nikkei')
grph_day_perc_change.line(x='Date', y='Day_Perc_Change', source=src_hangseng, color='red', legend_label='Hang Seng')
grph_day_perc_change.line(x='Date', y='Day_Perc_Change', source=src_nasdaq, color='blue', legend_label='Nasdaq')

hover = HoverTool()
hover.tooltips = [('Stock', '@Name'), ('Day Perc Change', '@Day_Perc_Change')]
grph_day_perc_change.add_tools(hover)

grph_day_perc_change.legend.click_policy="hide"

#create tabs for single plot chart (javascript roles)
tab1 = Panel(child=grph_adj_close, title="Adj Close")
tab2 = Panel(child=grph_Volume, title="Volume")
tab3 = Panel(child=grph_day_perc_change, title="Day Perc Change")


tab = Tabs(tabs=[tab1, tab2, tab3])
show(tab)
save(tab)

