from data.datapack import getDataset
import plotly
from plotly import tools
import plotly.graph_objs as go
def getCategoryByDate(dataset):
    bydate = dict()
    for category in dataset:
        for lst in dataset[category]:
            date = lst['Air Date']
            if date in bydate:
                bydate[date] += 1
            else:
                bydate[date] = 1
    return list(bydate.keys()), list(bydate.values())


def getCategoryAmount(dataset):
    categories = dict()
    for category in dataset:
        categories[category] = len(category)
    return list(categories.keys()), list(categories.values())

def getMaxPrice(dataset):
    val = dict()
    for category in dataset:
        val[category] = 0
        for lst in dataset[category]:
            if lst['Value'] > val[category]:
                val[category] = lst['Value']
    return list(val.keys()), list(val.values())

dataset = getDataset('JEOPARDY_CSV.csv')

dates, counter = getCategoryByDate(dataset)
categ, amount = getCategoryAmount(dataset)
categoryMax, price = getMaxPrice(dataset)


figure = {'data': [
    {
        'x': dates,
        'y': counter,
        'type': 'scatter'
    },
    {
        "x": categoryMax,
        "y": price,
        "type": "bar",
        "xaxis": "x2",
        "yaxis": "y2"
    },
    {
        'labels': categ,
        'values': amount,
        'type': 'pie',
        'domain': {'x': [0.25, 0.71], 'y': [0.5, 1]}
    }
                    ], "layout": go.Layout(
            xaxis=dict(domain=[0, 0.45]), yaxis=dict(domain=[0, 0.5]),
            xaxis2=dict(domain=[0.55, 1]), yaxis2=dict(domain=[0, 0.5], anchor='x2'))
          }
plotly.offline.plot(figure, filename='JeopardyAll Charts.html')
