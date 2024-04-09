#!/usr/bin/env python3
import gzip
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn import metrics


def spam_detection(random_state=0, fraction=1.0):
    # Read lines from ham and spam files
    
    with gzip.open('src/ham.txt.gz') as f1, gzip.open('src/spam.txt.gz') as f2:
        h = f1.readlines()
        s = f2.readlines()
        ham_lines = h[:int(len(h)*fraction)]
        spam_lines = s[:int(len(s)*fraction)]

    # Combine lines
    all_lines = ham_lines + spam_lines
    
    # Create labels (0 for ham, 1 for spam)    
    # Initialize CountVectorizer with some preprocessing options
    vectorizer = CountVectorizer()
    
    # Create feature matrix
    X = vectorizer.fit_transform(all_lines)
    y = np.concatenate((np.zeros(len(ham_lines)), np.ones(len(spam_lines))))
    # Check if vocabulary is empty
    if not vectorizer.vocabulary_:
        raise ValueError("Empty vocabulary; documents may only contain stop words or be too short.")
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, train_size=0.75, test_size=0.25, random_state=random_state)
    model = MultinomialNB()
    model.fit(X_train, y_train)
    y_predict = model.predict(X_test)
    acc = metrics.accuracy_score(y_predict, y_test)
    size = len(y_test)
    misclassified = np.sum(y_predict != y_test)
    print(type(y_test), len(y_predict))
    return acc, size, misclassified

# model solution
# def load_ham(filename="src/ham.txt.gz"):
#     with gzip.open(filename) as f:
#         lines = f.readlines()
#     return lines
 
# def load_spam(filename="src/spam.txt.gz"):
#     with gzip.open(filename) as f:
#         lines = f.readlines()
#     return lines
 
# def spam_detection(random_state=0, fraction=1.0):
#     vec = CountVectorizer()
#     ham = load_ham()
#     spam = load_spam()
#     ham = ham[:int(fraction*len(ham))]
#     spam = spam[:int(fraction*len(spam))]
#     X = vec.fit_transform(ham+spam)
#     n1 = len(ham)
#     n2 = len(spam)
#     if False:   # Print some info. From first two (ham) messages, show counts of common words.
#         print(X.shape)
#         temp = X[0:2, :].toarray()   # Vectorizer returns sparse array, convert to dense array
#         idx = temp[:, :] != 0
#         idx = temp.all(axis=0)
#         names = vec.get_feature_names()
#         df = pd.DataFrame(temp[:, idx], columns=np.array(names)[idx])
#         print(df.T)
#     y = np.hstack([[0]*n1, [1]*n2])
 
#     X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=random_state, train_size=0.75, test_size=0.25)
#     model = MultinomialNB()
#     model.fit(X_train, y_train)
#     y_fitted = model.predict(X_test)
#     acc = model.score(X_test, y_test)
#     return acc, len(y_test), (y_test != y_fitted).sum()

def main():
    accuracy, total, misclassified = spam_detection()
    print("Accuracy score:", accuracy)
    print(f"{misclassified} messages miclassified out of {total}")

if __name__ == "__main__":
    main()
