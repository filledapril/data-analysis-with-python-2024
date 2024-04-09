#!/usr/bin/env python3

from collections import Counter
import urllib.request
from lxml import etree

import numpy as np

from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import cross_val_score
from sklearn import model_selection

alphabet="abcdefghijklmnopqrstuvwxyzäö-"
alphabet_set = set(alphabet)

# Returns a list of Finnish words
def load_finnish():
    finnish_url="https://www.cs.helsinki.fi/u/jttoivon/dap/data/kotus-sanalista_v1/kotus-sanalista_v1.xml"
    filename="src/kotus-sanalista_v1.xml"
    load_from_net=False
    if load_from_net:
        with urllib.request.urlopen(finnish_url) as data:
            lines=[]
            for line in data:
                lines.append(line.decode('utf-8'))
        doc="".join(lines)
    else:
        with open(filename, "rb") as data:
            doc=data.read()
    tree = etree.XML(doc)
    s_elements = tree.xpath('/kotus-sanalista/st/s')
    return list(map(lambda s: s.text, s_elements))

def load_english():
    with open("src/words", encoding="utf-8") as data:
        lines=map(lambda s: s.rstrip(), data.readlines())
    return lines

# return a feature matrix of shape (n, 29), where n is the number of elements of the input array
def get_features(a):
    feature_vectors = []
    
    # Iterate over each word in the input array
    for word in a:
        # Initialize a list to store counts of each letter
        counts = []
        # Iterate over each letter in the alphabet
        for letter in alphabet:
            # Count the occurrences of the current letter in the word
            count = word.count(letter)
            counts.append(count)
        # Append the counts for the current word as a feature vector
        feature_vectors.append(counts)
    
    # Convert the list of feature vectors to a numpy array
    feature_matrix = np.array(feature_vectors)
    
    return feature_matrix

def contains_valid_chars(s):
    for char in s:
        # Check if the character is not in the alphabet
        if char not in alphabet_set:
            # If any character is not in the alphabet, return False
            return False
    
    # If all characters are in the alphabet, return True
    return True

def get_features_and_labels():
    finnish_words = [word.lower() for word in load_finnish() if contains_valid_chars(word.lower())]
    english_words = [word.lower() for word in load_english() if word[0].islower() and contains_valid_chars(word.lower())]

    # Create feature matrix for Finnish and English words
    X_finnish = get_features(finnish_words)
    X_english = get_features(english_words)

    # Create target vectors (labels) for Finnish and English words
    y_finnish = np.zeros(len(X_finnish), dtype=int)
    y_english = np.ones(len(X_english), dtype=int)

    # Combine feature matrices and target vectors
    X = np.concatenate((X_finnish, X_english))
    y = np.concatenate((y_finnish, y_english))

    return X, y


def word_classification():
    X, y = get_features_and_labels()
    # Initialize Multinomial Naive Bayes classifier
    classifier = MultinomialNB()
    
    # Initialize KFold cross-validation generator
    kf = model_selection.KFold(n_splits=5, shuffle=True, random_state=0)
    
    # Perform 5-fold cross-validation and get accuracy scores
    scores = cross_val_score(classifier, X, y, cv=kf)
    
    return scores


def main():
    print("Accuracy scores are:", word_classification())

if __name__ == "__main__":
    main()
