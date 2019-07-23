# Deploy practice

To refer this tutorial click [here](https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/)

* __PICKLE__ library

> to save the model into a file

```python

import pickle
# let the model1 name be 'NN_model'
NN_model = MLPClassifier(alpha=1, max_iter=1000).fit()
# let the model2 name be 'linear_model'
linear_model = model.fit()
# to load model into a file with .sav extension 
filename = 'NN_Model.sav'
pickle.dump(model, open(filename,'wb'))

filename = 'linear_Model.sav'
pickle.dump(linear_Model, open(filename,'wb'))

```


> to load data from disk file to variable which will act as a model

```python

filename = 'NN_Model.sav'
loaded_model_NueralNetwork = pickle.load(open(filename,'rb'))

prediction1 = loaded_model_NueralNetwork.predict(_value)
print("Result by Neuaral Network :    ", prediction1)

```


* __JOBLIB__ library

[joblib](https://pypi.org/project/joblib/)

```python
# directly import joblib 
# from sklearn.externals import joblib is deprecated  and soon will be removed

import joblib

# to load the data on disk file
# save the model to disk
filename = 'finalized_model.sav'
joblib.dump(model, filename)

# to laod model from the disk file
loaded_model = joblib.load(filename)

# now you use the model as your wishes
loaded_model.predict()
loaded_model.score()
#.... so on

```

