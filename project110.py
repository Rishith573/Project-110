import random
import pandas as pd
import csv
import statistics
import plotly.figure_factory as ff

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

fig = ff.create_distplot([data], ["Readting time"], show_hist= False)
fig.show()

print("Population mean:", statistics.mean(data))

def randomSet(counter):
    dataSet = []
    for i in range(0, counter):
        randomIndex = random.randint(0, len(data))
        value = data[randomIndex]
        dataSet.append(value)
    mean = statistics.mean(dataSet)
    return mean

def showFig(meanList):
    df = meanList
    fig = ff.create_distplot([df], ["Reading time"], show_hist=False)
    fig.show()

def setup():
    meanList = []
    for i in range(0, 100):
        setMean = randomSet(10)
        meanList.append(setMean)
    showFig(meanList)
    print("sampling mean: ", statistics.mean(meanList))

setup()