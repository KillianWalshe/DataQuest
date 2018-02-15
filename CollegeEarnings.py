import pandas as pd
from pandas.tools.plotting import scatter_matrix as sm
import matplotlib.pyplot as plt

recent_grads = pd.read_csv('Datafiles/recent-grads.csv')
#print(recent_grads.iloc[0])
#print(recent_grads.head())
#print(recent_grads.tail())

#print(recent_grads.describe())

raw_data_count=len(recent_grads)
#print(raw_data_count)
recent_grads=recent_grads.dropna()
raw_data_count=len(recent_grads)
#print(raw_data_count)

#recent_grads.plot(x='Sample_size', y='Median', kind='scatter', title='Median vs. Sample_size')
#plt.show()
#recent_grads.plot(x='Sample_size', y='Unemployment_rate', kind='scatter', title='Unemployment_rate vs. Sample_size')
#plt.show()
#recent_grads.plot(x='Full_time', y='Median', kind='scatter', title='Median vs. Full_time')
#plt.show()
#recent_grads.plot(x='ShareWomen', y='Unemployment_rate', kind='scatter', title='Unemployment_rate vs. ShareWomen')
#plt.show()
#recent_grads.plot(x='Men', y='Median', kind='scatter', title='Median vs. Men')
#plt.show()
#recent_grads.plot(x='Women', y='Median', kind='scatter', title='Median vs. Women')
#plt.show()
print(recent_grads.tail())
#Do students in more popular majors make more money?  No
#recent_grads.plot(x='Total', y='Rank', kind='scatter', title='Rank vs. Total')
#plt.show()

#Do students that majored in subjects that were majority female make more money? no
#recent_grads.plot(x='Full_time', y='Median', kind='scatter', title='Median vs. Full_time')
#plt.show()
#Is there any link between the number of full-time employees and median salary   



#Histograms  dont use range to begin with in future, some of these arent great

#recent_grads['Sample_size'].plot(kind='hist')
#recent_grads['Sample_size'].hist(bins=25, range=(0,500))
#plt.show()
#recent_grads['Median'].hist(bins=25, range=(0,110000))
#plt.show()
#recent_grads['Employed'].hist(bins=25, range=(0,5000))
#plt.show()
#recent_grads['Full_time'].hist(bins=25, range=(0,5000))
#plt.show()
#recent_grads['ShareWomen'].hist(bins=50, range=(0,1))
#plt.show()
#recent_grads['Unemployment_rate'].hist(bins=50, range=(0,0.5))
#plt.show()
#recent_grads['Men'].hist(bins=25, range=(0,20000))
#plt.show()
#recent_grads['Women'].hist(bins=25, range=(0,5000))
#plt.show()


#sm(recent_grads[['Sample_size', 'Median', 'Unemployment_rate']], figsize=(10,10))
#plt.show()


#recent_grads[:10].plot.bar(x='Major',y='ShareWomen')

#plt.show()
#recent_grads[(len(recent_grads)-10):].plot.bar(x='Major',y='ShareWomen')
#plt.show()

#recent_grads[:10].plot.bar(x='Major',y='Unemployment_rate')

#plt.show()
#recent_grads[(len(recent_grads)-10):].plot.bar(x='Major',y='Unemployment_rate')
#plt.show()

recent_grads.plot.hexbin(x='Full_time', y='Median')
plt.show()


