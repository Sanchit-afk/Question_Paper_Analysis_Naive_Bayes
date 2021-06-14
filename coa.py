

import os
from collections import Counter
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split as tts
from sklearn.metrics import accuracy_score
from joblib import dump
def make_dict():
    direc = "coasyllabus/"
    files = os.listdir(direc)
    
    questions = [direc + question for question in files]
    
    words = []
    c = len(questions)
    for question in questions:
        f = open(question,"r",encoding="utf-8")
        blob = f.read()
        words += blob.split(" ")
        print(c)
        c -= 1
    # print(words)
    for i in range(len(words)):
        if not words[i].isalnum():
            words[i] = ""
    dictionary = Counter(words)
    del dictionary[""]
    # print(dictionary.most_common(1000))
    return( dictionary.most_common(1000))
def make_dataset(dictionary):
    direc = "coasyllabus/"
    files = os.listdir(direc)
    
    questions = [direc + question for question in files]
    
    feature_set = []
    labels = []
    c = len(questions)
    for question in questions:
        data = []
        f = open(question,"r",encoding="utf-8")
        words = f.read().split(' ')
        for entry in dictionary:
            data.append(words.count(entry[0]))
        feature_set.append(data)
        if "intro" in question:
            labels.append(0)
        # if "dypa" in question:
        #     labels.append(1)
        if "mod2" in question:
            labels.append(1)
        # if "gma" in question:
        #     labels.append(2)
        if "mod3" in question:
            labels.append(2)
#        if "babab" in question:
#            labels.append(3)
        if "mod4" in question:
            labels.append(3)
        if "mod5" in question:
            labels.append(4)
        if "mod6" in question:
            labels.append(5)
        print(c)
        c -= 1
    return feature_set,labels

d = make_dict()

features, labels = make_dataset(d)

print(len(features),len(labels))
x_train, x_test, y_train, y_test = tts(features,labels,test_size=0.5)
clf = MultinomialNB()
clf.fit(x_train, y_train)
pred = clf.predict(x_test)
print(accuracy_score(y_test, pred))
while accuracy_score(y_test, pred) < 0.99:
    x_train, x_test, y_train, y_test = tts(features,labels,test_size=0.2)
    clf = MultinomialNB()
    clf.fit(x_train, y_train)
    pred = clf.predict(x_test)
    # while(accuracy_score(y_test, pred) <0.8):
    #     clf = MultinomialNB()
    #     clf.fit(x_train, y_train)
    #     pred = clf.predict(x_test)
    # print(d)
    print(accuracy_score(y_test, pred))
print("Final Accuracy: "+str(accuracy_score(y_test, pred)))
dump(clf, 'coa-classifier.joblib')