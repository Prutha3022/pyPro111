import statistics
import pandas as pd
import csv
import plotly.figure_factory as ff
import plotly.graph_objects as go
import random

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

population_mean = statistics.mean(data)
print("Population mean :- ", population_mean)

def random_set_of_means(counter):
    dataset = []
    for i in range(0, len(data)-1):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def setup():
    meanlist = []
    for i in range(0,100):
        set_of_means = random_set_of_means(30)
        meanlist.append(set_of_means)
    
    sample_mean = statistics.mean(meanlist)
    print("mean of samples :-", sample_mean)

    sample_std_deviation = statistics.stdev(meanlist)
    print("standard deviation of samples :-", sample_std_deviation)
    
    first_std_dev_start, first_std_dev_end = sample_mean - sample_std_deviation, sample_mean + sample_std_deviation
    second_std_dev_start, second_std_dev_end = sample_mean - (2*sample_std_deviation), sample_mean + (2*sample_std_deviation)
    third_std_dev_start, third_std_dev_end = sample_mean - (3*sample_std_deviation), sample_mean + (3*sample_std_deviation)

    df = pd.read_csv("medium_data.csv")
    data = df["reading_time"].tolist()
    mean_of_sample1 = statistics.mean(data)

    fig = ff.create_distplot([meanlist], ["Reading time"], show_hist=False)
    fig.add_trace(go.Scatter(x = [mean_of_sample1, mean_of_sample1], y =[0,1], mode="lines", name="MEAN"))
    fig.add_trace(go.Scatter(x = [first_std_dev_start, first_std_dev_start], y =[0,1], mode="lines", name="FIRST STANDARD DEVIATION START"))
    fig.add_trace(go.Scatter(x = [first_std_dev_end, first_std_dev_end], y =[0,1], mode="lines", name="FIRST STANDARD DEVIATION END"))
    fig.add_trace(go.Scatter(x = [second_std_dev_start, second_std_dev_start], y =[0,1], mode="lines", name="SECOND STANDARD DEVIATION START"))
    fig.add_trace(go.Scatter(x = [second_std_dev_start, second_std_dev_start], y =[0,1], mode="lines", name="SECOND STANDARD DEVIATION START"))
    fig.add_trace(go.Scatter(x = [third_std_dev_start, third_std_dev_start], y =[0,1], mode="lines", name="THIRD STANDARD DEVIATION START"))
    fig.add_trace(go.Scatter(x = [third_std_dev_start, third_std_dev_start], y =[0,1], mode="lines", name="THIRD STANDARD DEVIATION START"))
    fig.show()

    z_score = (sample_mean - mean_of_sample1) / sample_std_deviation
    print("Z score :- " ,z_score)
setup()