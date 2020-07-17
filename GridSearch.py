# In this example, we will try to predict the survival rate of passengers using Decision Tree classification
# In addition to this, we will use GridSearch method to find the best predicting model and its parameters.
# added another line to this 
## and another line
# this pull request coming from github for desktop.
import numpy as np
import pandas as pd
in_file = 'titanic_data.csv'
full_data = pd.read_csv(in_file)
outcomes = full_data['Survived']
features_raw = full_data.drop('Survived', axis = 1)
# data pre processing :
features = pd.get_dummies(features_raw)
features = features.fillna(0.0)


# now after importing data into pandas dataframe and isolating y column which is outcomes 
# it is time to split data into train and test
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(features, outcomes, test_size=0.2, random_state=42)
# Import the classifier from sklearn
from sklearn.tree import DecisionTreeClassifier
# Define the classifier, and fit it to the data
model = DecisionTreeClassifier()
## model.fit(features, outcomes) we will not fit it here, since we will look for best model. But if we decided
# not to use gridsearch then we must fit the data to the model here with default hyperparameters.

# Lets import GridSearchCV from sklearn.model_selection
from sklearn.model_selection import GridSearchCV
# lets start tune hyperparameters:
parameters = {"max_depth": [4,5,6,7,8,9], "min_samples_leaf": [3,4,5,6,7]}
# we need to create a scorer :
from sklearn.metrics import make_scorer
from sklearn.metrics import accuracy_score
scorer = make_scorer(accuracy_score)
# now, it is time to create a gridsearch object 
grid_obj = GridSearchCV(model, parameters, scoring = scorer)
# we must fit the data into this gridsearch object
grid_fit = grid_obj.fit(features, outcomes)
# now it is time to retract the best predicting model"
best_est = grid_fit.best_estimator_
# make predictions :
best_train_predictions = best_est.predict(X_train)
best_test_predictions = best_est.predict(X_test)
# now lets find their accuracy scores :
accuracy_best_train = accuracy_score(y_train, best_train_predictions )
accuracy_best_test = accuracy_score(y_test, best_test_predictions )
# Now lets print out their accuracy scores :
print('The best training accuracy is', accuracy_best_train)
print('The best test accuracy is', accuracy_best_test)
# lets get the best hyperparameters of this model.

print("Best hyperparameters are: ", best_est.get_params())



