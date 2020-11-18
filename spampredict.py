import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score

#uploaded = files.upload()
#for fn in uploaded.keys():
#    print('User uploaded files {name} having length {length} in bytes'.format(name = fn,length=len(uploaded[fn])))

# load dataset to pandas dataframe
cols = ['Category','Message']
raw_mail_data=pd.read_csv('spamham.csv',encoding='ANSI')
print(raw_mail_data.head())
# Replace null values with null string
mail_data = raw_mail_data.where((pd.notnull(raw_mail_data)), '')

#Categories the data to binary classification by labelling spam=0 and ham =1
mail_data.loc[mail_data['Category']=='spam','Category',]=0
mail_data.loc[mail_data['Category']=='ham','Category',]=1

#Separate data as text and label
x = mail_data['Message']
y = mail_data['Category']

print(x)
print('....................')
print(y)

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=3)

#Extracting the feature
feature_extraction = TfidfVectorizer(min_df=1,stop_words='english',lowercase='True')
x_train_features = feature_extraction.fit_transform(x_train)
x_test_features = feature_extraction.transform(x_test)

#convert y_test and y_train as int
y_train = y_train.astype('int')
y_test = y_test.astype('int')

model = LinearSVC()
model.fit(x_train_features,y_train)

#Evaluating training models
predict_train = model.predict(x_train_features)
score_train = accuracy_score(y_train,predict_train)

print(score_train)

#Evaluating testing model
predict_test = model.predict(x_test_features)
score_test = accuracy_score(y_test,predict_test)

print(score_test)

sample_data = ['CELEBRATE THE TREASURES OF SOUTH INDIA WITH THE GOLDEN CHARIOT TRAIN']
sample_data_test = feature_extraction.transform(sample_data)
#prediction
predict_sampledata = model.predict(sample_data_test)
if predict_sampledata[0]==0:print('Its Spam mail')
else:print('Its ham mail')
