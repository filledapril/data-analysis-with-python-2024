#!/usr/bin/env python3

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import naive_bayes
from sklearn import metrics

# loads the iris dataset using sklearn (sklearn.datasets.load_iris)
# splits the data into training and testing part using the train_test_split function 
#  the training set size is 80% of the whole data (give the call also the random_state=0argument to make the result deterministic)
# use Gaussian naive Bayes to fit the training data
# predict labels of the test data
# the function should return the accuracy score of the prediction performance (sklearn.metrics.accuracy_score)
def plant_classification():
    data = load_iris()
    X, y = data.data, data.target
    # Split the data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)
    model = naive_bayes.GaussianNB()
    model.fit(X_train, y_train)
    labels_predicted = model.predict(X_test)
    # Calculate accuracy score
    acc = metrics.accuracy_score(labels_predicted, y_test)
    return acc

def main():
    print(f"Accuracy is {plant_classification()}")

if __name__ == "__main__":
    main()
