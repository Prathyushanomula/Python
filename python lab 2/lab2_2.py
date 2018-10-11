from sklearn.svm import SVC
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split
from sklearn import datasets
#load the iris datasets
data=datasets.load_iris()
#load i/p and o/p data
x=data.data
y=data.target
#splitting train and test data for poly kernel
train_x, test_x, train_y, test_y=train_test_split(x, y, test_size=0.2, random_state=21)
#splitting train and test data for  rbf kernel
train_x1, test_x1, train_y1, test_y1=train_test_split(x, y, test_size=0.2, random_state=23)
#define poly kernel model
polymodel=SVC(kernel='poly', degree=4)
#define rbf kernel
rbfmodel=SVC(kernel='rbf')
#fit training data into poly kernel
polymodel.fit(train_x, train_y)
#test data prediction using poly kernel
prediction=polymodel.predict(test_x)
print("poly kernel Accuracy score is", accuracy_score(prediction, test_y)) # accuracy score for poly kernel
print(prediction)
#fit training data into rbc kernel
rbfmodel.fit(train_x1, train_y1)
#predict the test data for rbc kernel
prediction1=polymodel.predict(test_x1)
#calc accuracy for rbc kernel
print("RBF kernel accuracy score is", accuracy_score(prediction1, test_y1))
print(prediction1)