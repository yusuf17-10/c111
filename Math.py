import pandas as pd
import plotly.figure_factory as ff
import statistics
import random
import plotly.graph_objects as go

df=pd.read_csv("studentMarks.csv")
data=df["Math_score"].tolist()


fig=ff.create_distplot([data],["Math Score"],show_hist=False)
fig.show()

mean=statistics.mean(data)
standard_dev=statistics.stdev(data)
print("Mean Of Population :"+str(mean))
print("Standard Deveation Of Population :"+str(standard_dev))

def mean_of_random_sample_list(counter):
    data_set=[]
    for i in range(0,counter):
        rand=random.randint(0,len(data)-1)
        data_set.append(data[rand])
    mean=statistics.mean(data_set)
    return mean

mean_list=[]
for i in range(0,1000):
    mean_data=mean_of_random_sample_list(100)
    mean_list.append(mean_data)

mean1=statistics.mean(mean_list)
standard_dev1=statistics.stdev(mean_list)
print("Mean Of sampling distribution :"+str(mean1))
print("Standard Deveation Of sampling distribution :"+str(standard_dev1))


fig1=ff.create_distplot([mean_list],["Math Score"],show_hist=False)
fig1.add_trace(go.Scatter(x=[mean1,mean1],y=[0,0.2],mode="lines",name="MEAN"))


first_standard_deviation_start,first_standard_deviation_end=mean1-standard_dev1,mean1+standard_dev1
second_standard_deviation_start,second_standard_deviation_end=mean1-(standard_dev1*2),mean1+(standard_dev1*2)
third_standard_deviation_start,third_standard_deviation_end=mean1-(standard_dev1*3),mean1+(standard_dev1*3)

fig1.add_trace(go.Scatter(x=[first_standard_deviation_start,first_standard_deviation_start],y=[0,0.2],mode="lines",name="Standard_Deveation1_start"))
fig1.add_trace(go.Scatter(x=[first_standard_deviation_end,first_standard_deviation_end],y=[0,0.2],mode="lines",name="Standard_Deveation1_end"))
fig1.add_trace(go.Scatter(x=[second_standard_deviation_start,second_standard_deviation_start],y=[0,0.2],mode="lines",name="Standard_Deveation2_start"))
fig1.add_trace(go.Scatter(x=[second_standard_deviation_end,second_standard_deviation_end],y=[0,0.2],mode="lines",name="Standard_Deveation2_end"))
fig1.add_trace(go.Scatter(x=[third_standard_deviation_start,third_standard_deviation_start],y=[0,0.2],mode="lines",name="Standard_Deveation3_start"))
fig1.add_trace(go.Scatter(x=[third_standard_deviation_end,third_standard_deviation_end],y=[0,0.2],mode="lines",name="Standard_Deveation3_end"))
fig1.show()

# Mean of first data and plotting it

df=pd.read_csv("data1.csv")
data1=df["Math_score"].tolist()


mean_of_sample1=statistics.mean(data1)
print("mean_of_sample1"+str(mean_of_sample1))

fig_sample1=ff.create_distplot([mean_list],["Math Score"],show_hist=False)
fig_sample1.add_trace(go.Scatter(x=[mean1,mean1],y=[0,0.2],mode="lines",name="MEAN"))

fig_sample1.add_trace(go.Scatter(x=[first_standard_deviation_end,first_standard_deviation_end],y=[0,0.2],mode="lines",name="Standard_Deveation1_end"))

fig_sample1.add_trace(go.Scatter(x=[mean_of_sample1,mean_of_sample1],y=[0,0.2],mode="lines",name="mean_of_sample1"))
fig_sample1.show()
z_score_sample1=(mean_of_sample1-mean1)/standard_dev1
print("z_score_sample1 :"+str(z_score_sample1))


# Mean of second data and plotting it

df=pd.read_csv("data2.csv")
data2=df["Math_score"].tolist()


mean_of_sample2=statistics.mean(data2)
print("mean_of_sample2"+str(mean_of_sample2))

fig_sample2=ff.create_distplot([mean_list],["Math Score"],show_hist=False)
fig_sample2.add_trace(go.Scatter(x=[mean1,mean1],y=[0,0.2],mode="lines",name="MEAN"))

fig_sample2.add_trace(go.Scatter(x=[first_standard_deviation_end,first_standard_deviation_end],y=[0,0.2],mode="lines",name="Standard_Deveation1_end"))
fig_sample2.add_trace(go.Scatter(x=[second_standard_deviation_end,second_standard_deviation_end],y=[0,0.2],mode="lines",name="Standard_Deveation2_end"))

fig_sample2.add_trace(go.Scatter(x=[mean_of_sample2,mean_of_sample2],y=[0,0.2],mode="lines",name="mean_of_sample1"))

fig_sample2.show()
z_score_sample2=(mean_of_sample2-mean1)/standard_dev1
print("z_score_sample2 :"+str(z_score_sample2))

# Mean of third data and plotting it

df=pd.read_csv("data3.csv")
data3=df["Math_score"].tolist()


mean_of_sample3=statistics.mean(data3)
print("mean_of_sample3 :"+str(mean_of_sample3))

fig_sample3=ff.create_distplot([mean_list],["Math Score"],show_hist=False)
fig_sample3.add_trace(go.Scatter(x=[mean1,mean1],y=[0,0.2],mode="lines",name="MEAN"))

fig_sample3.add_trace(go.Scatter(x=[first_standard_deviation_end,first_standard_deviation_end],y=[0,0.2],mode="lines",name="Standard_Deveation1_end"))
fig_sample3.add_trace(go.Scatter(x=[second_standard_deviation_end,second_standard_deviation_end],y=[0,0.2],mode="lines",name="Standard_Deveation2_end"))
fig_sample3.add_trace(go.Scatter(x=[third_standard_deviation_end,third_standard_deviation_end],y=[0,0.2],mode="lines",name="Standard_Deveation3_end"))
fig_sample3.add_trace(go.Scatter(x=[mean_of_sample3,mean_of_sample3],y=[0,0.2],mode="lines",name="mean_of_sample1"))

fig_sample3.show()

z_score_sample3=(mean_of_sample3-mean1)/standard_dev1
print("z_score_sample3 :"+str(z_score_sample3))


