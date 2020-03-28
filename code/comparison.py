import pandas
import matplotlib.pyplot as plt
#from scipy.sparse.data import _data_matrix
from sklearn import model_selection

from sklearn.neighbors import KNeighborsClassifier

from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
#from sklearn.model_selection import train_test_split
import os
from sklearn.svm import SVC


path = "F:\\Intenship Project\\march.csv"
names = []

dataframe = pandas.read_csv(path, names=names)
#print(dataframe.head(n=6))
#print(dataframe.dtypes)
array = dataframe.values
X = array[:,0:23]
Y = array[:,1]

seed = 7

models = []
models.append(('Random Forest ', RandomForestClassifier()))
models.append(('KNN', KNeighborsClassifier()))
models.append(('naive_bayes', GaussianNB()))
models.append(('SVM', SVC()))


results = []
names = []
scoring = 'accuracy'
for name, model in models:
	kfold = model_selection.KFold(n_splits=10,shuffle=True, random_state=seed)

	cv_results = model_selection.cross_val_score(model, X, Y, cv=kfold, scoring=scoring)

	results.append(cv_results)
	names.append(name)
	msg = "Accuracy %s: %f " % (name, cv_results.mean() )
	print(msg)

fig = plt.figure()
fig.suptitle('Algorithm Comparison')
ax = fig.add_subplot(111)
plt.boxplot(results)
ax.set_xticklabels(names)
plt.show()