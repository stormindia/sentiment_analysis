This is a project for classification of sentiments of tweets

This project runs in python 2

There are three models used for this. Navigate to src directory and you will find -
1. knn.py
2. svm.py
3. hybrid.py

You can find all the resources such as AFINN , Emoticons etc in the resources directory.
All the input data is present in data folder. Kindly refer report.pdf for their sources

To run this code all you have to do is -
execute
classifier.py <argument>
Pass in the argumnet - ['svm' , 'knn' , 'hybrid'] without quotes for which ever model you want to run.

The values for labels are -
4.0 for positive
2.0 for neutral
0.0 for negative
