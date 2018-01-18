from bokeh.layouts import layout, widgetbox, row, column
from bokeh.models import ColumnDataSource, HoverTool, Div, FactorRange, MultiSelect, Range1d
from bokeh.models.widgets import Slider, Select, TextInput, RangeSlider
from bokeh.palettes import Category20_20 as palette
from bokeh.transform import factor_cmap
from bokeh.plotting import figure
from os.path import dirname, join
from bokeh.io import curdoc
import pandas as pd
import itertools

dataz = pd.read_excel('NRC_allegation_stats.xlsx')
site = dataz['Site']
xlsx = pd.ExcelFile('NRC_allegation_stats.xlsx')
file = xlsx.parse(xlsx.sheet_names[0])
data = pd.read_excel('NRC_allegation_stats.xlsx').set_index("Site").fillna(False)
data_substantiated  = pd.read_excel('NRC_allegation_stats.xlsx', sheetname=2).set_index("Site").fillna(False)
data.fillna('')
data_substantiated.fillna('')
fruits = list(dataz['Site'])
years = [str(i) for i in data.columns.values]
palette = list(itertools.islice(palette, len(data.columns.values)))


# this creates [ ("Apples", "2015"), ("Apples", "2016"), ("Apples", "2017"), ("Pears", "2015), ... ]
years_widget = RangeSlider(start=2013, end=2017, value=(2015, 2017), step=1, title="Year[s]")
site_widget = MultiSelect(title="Site[s]", value=["ARKANSAS 1 & 2"], options=open(join(dirname(__file__), 'sites.txt')).read().split('\n'))
site_widget.on_change('value', lambda attr, old, new: update)


# this creates [ ("Apples", "2015"), ("Apples", "2016"), ("Apples", "2017"), ("Pears", "2015), ... ]
x = [ (fruit, year) for fruit in fruits for year in years ]
source = ColumnDataSource(data=dict(x=[], counts=[]))
source2 = ColumnDataSource(data=dict(x=[], counts=[]))

p = figure(x_range=data.index.values.tolist(), plot_height=350, title="Allegations Received from All Sources",
            toolbar_location=None, tools="")
p.vbar(x='x', top='counts', width=0.9,  source=source, line_color="white", fill_color=factor_cmap('x', palette=palette, factors=years, start=1, end=2))
p.y_range.start = 0
p.x_range.range_padding = 0.1
p.xaxis.major_label_orientation = 1
p.xgrid.grid_line_color = None

p2 = figure(x_range=data_substantiated.index.values.tolist(), plot_height=350, title="Substantiated Allegations Received from All Sources",
            toolbar_location=None, tools="")
p2.vbar(x='x', top='counts', width=0.9,  source=source2, line_color="white", fill_color=factor_cmap('x', palette=palette, factors=years, start=1, end=2))
p2.y_range.start = 0
p2.x_range.range_padding = 0.1
p2.xaxis.major_label_orientation = 1
p2.xgrid.grid_line_color = None



def update():
    selected_years = [i for i in range(years_widget.value[0], years_widget.value[1]+1, 1)]
    selected_sites = [i for i in site_widget.value]
    x = [ (fruit, str(year)) for fruit in selected_sites for year in selected_years]
    xx = [dataz[i] for i in selected_years]
    counts = sum(list(zip(*xx)), ())
#    test1 = ['Apples', 'Pears', 'Nectarines']
    test1=site_widget.value
    test2 = selected_years
#    test2 = [2015, 2016]
#    print(test2)
#    test= data3.iloc[0].values
    test = data.loc[test1,test2].values
    test2 = data_substantiated.loc[test1, test2].values
    counts2 = sum(list(zip(*test)), ())
    counts3 = sum(list(zip(*test2)), ())
    p.x_range.factors = x
    p2.x_range.factors = x
    p2.y_range = Range1d(0, max(counts2) )
    source.data = dict(
            x = x, 
            counts = counts2,
            )
    source2.data = dict(
            x = x, 
            counts = counts3,
            )

update()  # initial load of the data

controls = [years_widget, site_widget ]
for control in controls:
    control.on_change('value', lambda attr, old, new: update())

sizing_mode = 'fixed'  # 'scale_width' also looks nice with this example

inputs = widgetbox(*controls, sizing_mode=sizing_mode)
l = row(column(inputs), column(p, p2)) 




curdoc().add_root(l)
curdoc().title = "NRC Allegation Statistics" 