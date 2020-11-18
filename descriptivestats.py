import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mtcars = pd.read_csv('https://raw.githubusercontent.com/sunnyyashu178/DataScience-Projects/master/mtcars.csv')
#print(mtcars.head())
#print(mtcars.mean(axis=1))
#print(mtcars['mpg'].mean())
#print(mtcars.median())

#checking stats
skew_data =np.random.normal(size=50)
outliers = np.random.normal(15,size=3)
norm_data = pd.DataFrame(np.concatenate((skew_data,outliers)))
norm_data.plot(kind='density',figsize=(8,8),xlim=(-5,20),label='normal plot')
plt.vlines(norm_data.mean(),ymin=0,ymax=0.4,linewidth=5.0,label='mean')
plt.vlines(norm_data.median(),ymin=0,ymax=0.4,linewidth=2.0,color='red',label='median')
plt.legend()
plt.show()

print(max(mtcars['mpg'])-min(mtcars['mpg']))
print(mtcars['mpg'].quantile(0))
print(mtcars['mpg'].quantile(0.25))
print(mtcars['mpg'].quantile(0.50))
print(mtcars['mpg'].quantile(0.75))
print(mtcars['mpg'].quantile(1))
print(mtcars['mpg'].describe())
print(mtcars['mpg'].var())
print(mtcars['mpg'].std())
#IQR
print((mtcars['mpg'].quantile(0.75))-mtcars['mpg'].quantile(0.25))
mtcars.boxplot(column='mpg',figsize=(8,8))
plt.text(x=0.8,y=15.425,s='25% Quantile')
plt.show()
#MAD - Median Absolute Deviation
median_val = abs(mtcars['mpg']-mtcars['mpg'].median())
print(median_val.values)
print(median_val.median()*1.4826)#scaling factor = 1.4826
##descriptive stats
mpg = mtcars['mpg']
cyl = mtcars['cyl']
disp = mtcars['disp']
data = pd.DataFrame({'mpg':mpg,
                     'cylinder':cyl,
                     'displacement':disp})

data.plot(kind='density',figsize=(8,8))
plt.xlabel('X')
plt.ylabel('Y')
plt.show()
