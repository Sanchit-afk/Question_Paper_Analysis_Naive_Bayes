#STEP 3
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from joblib import load
import os
from sklearn import svm
from collections import Counter
import csv
import pandas
#import matplotlib.pyplot as plt

def make_dict():
    direc = "aoasyllabus/"
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
    #print(words)
    for i in range(len(words)):
        if not words[i].isalnum():
            words[i] = ""
    dictionary = Counter(words)
    del dictionary[""]
    return( dictionary.most_common(1000))


def classify():
    clf = load('text-classifier.joblib')
    d = make_dict()

            
    modules = [['INTRODUCTION','TO','ALGORITHMS'],['DYNAMIC','PROGRAMMING','APPROACH'],
                ['GREEDY','METHOD','APPROACH'],['BACKTRACK','AND','BRANCH-AND-BOUND'],['STRING','MATCHING','ALGORITHMS'],
                ['NON','DETERMINISTIC','POLYNOMIAL','ALGORITHMS']]
    modDict = {1:0,2:0,3:0,4:0,5:0,6:0}

    filename = 'comp_ques_AOA.txt'
    file1 = open(filename, 'r',encoding="utf-16") 
    Lines = file1.readlines() 


    for line in Lines:
        features = []
        inp = line.lower()
        stop_words = set(stopwords.words('english'))
        stop_words = stop_words | set(['write','explain','detail','short note','short notes',
                        'short','notes','note','algorithm','algorithms',
                        'prove','problem','understand','answer','following'])  
        word_tokens = word_tokenize(inp)
        inp = [w for w in word_tokens if  w not in stop_words]
        for i in range(len(inp)):
            if '-' in inp[i]:
                inp[i] = " ".join(inp[i].split('-'))
            elif not inp[i].isalpha() or inp[i] == ',':
                inp[i] = ""
        text = " "
        inp = (text.join(inp)).lower()
        if(len(inp.replace(' ', '')) > 4):
            print('Question: '+ line)
            print("Modified Question: "+inp)
            for word in d:
                features.append(inp.count(word[0]))
            res = clf.predict([features])
            modDict[int(res+1)]+=1
            print(modules[int(res)])
            print("\n\n")
        else:
            pass

    print("\n\n\nAnalysis:")
    
    print(modDict)
    return modDict,modules

def custom_classify(filename):
    clf = load('text-classifier.joblib')
    d = make_dict()

            
    modules = [['INTRODUCTION','TO','ALGORITHMS'],['DYNAMIC','PROGRAMMING','APPROACH'],
                ['GREEDY','METHOD','APPROACH'],['BACKTRACK','AND','BRANCH-AND-BOUND'],['STRING','MATCHING','ALGORITHMS'],
                ['NON','DETERMINISTIC','POLYNOMIAL','ALGORITHMS']]
    modDict = {1:0,2:0,3:0,4:0,5:0,6:0}

    
    file1 = open(filename, 'r') 
    Lines = file1.readlines() 


    for line in Lines:
        features = []
        inp = line.lower()
        stop_words = set(stopwords.words('english'))
        stop_words = stop_words | set(['write','explain','detail','short note','short notes',
                        'short','notes','note','algorithm','algorithms',
                        'prove','problem','understand','answer','following'])  
        word_tokens = word_tokenize(inp)
        inp = [w for w in word_tokens if  w not in stop_words]
        for i in range(len(inp)):
            if '-' in inp[i]:
                inp[i] = " ".join(inp[i].split('-'))
            elif not inp[i].isalpha() or inp[i] == ',':
                inp[i] = ""
        text = " "
        inp = (text.join(inp)).lower()
        if(len(inp.replace(' ', '')) > 4):
            # print('Question: '+ line)
            # print("Modified Question: "+inp)
            for word in d:
                features.append(inp.count(word[0]))
            res = clf.predict([features])
            modDict[int(res+1)]+=1
            # print(modules[int(res)])
            # print("\n\n")
        else:
            pass

    # print("\n\n\nAnalysis:")

    return modDict,modules

classify()   

# dictlist = []
# for mod in modDict:
#     temp = [mod,modDict[mod]]
#     dictlist.append(temp)

# with open('D:/pbl/python/analysis_of_qp/subset/aoa/aoa/analysis.csv', mode='w') as file:
#     writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
#     writer.writerow(['Module','Questions'])
#     for i in dictlist:
#         writer.writerow(i)

# result = pandas.read_csv('D:/pbl/python/analysis_of_qp/subset/aoa/aoa/analysis.csv', sep=',',usecols=['Module','Questions'])


# result.plot(kind='bar')
# plt.ylabel('Questions')
# plt.xlabel('Module')
# plt.title('Analysis of AOA Question Paper')
# plt.show()
# f = plt.figure(1)
# plt.bar(list(modDict.keys()), modDict.values())
# plt.ylabel('Questions')
# plt.xlabel('Module')
# plt.title('Analysis of AOA Question Paper')
# f.show()

# g = plt.figure(2)
# plt.pie([v for v in modDict.values()], labels=[k for k in modules],
#            autopct=None)
# g.show()

# print(undetermined)
# print(len(undetermined))
# str = input()


# ['3   (a) Let n - 4, (p1, p2, p3, p4) - (100, 10, 15 , 27) and\n', '6. Write note on (any twn)H.\n', 'N=6 W=13,5,7,8,9,15 )&M=20\n', '6. Write short notes on (Any Four)\n', 'e)   \n', 'Q. r$ -...,\n', 'c.--\t\n', '1 \t\n', 'C.:\n', '4.•;\\\t\n', '5.        3                               7\n', 'Q.6     
#     Write a short note on(Any two)\n', '3.Recurrenses.\n', '6.       Write a short note on following (any 4) :\n', 'i) T(n) = 3n + 2\n', 'ii) T(n) = 10n2 + 2n + 1\n', "6. 'Write note on :— (any two)\n", '6. Write note on : (any two)\n', 'Q6. Write note on (any two):\n', '1           18              3\n', '2           25              5\n', '3           27              4\n', '4           10              3\n', '5           15              6\n', 'Q.1 Answer the following\n', 'N=6 W={3,5,7,8,9,15} & M =20 Also write the Algorithm for it.\n', 'Q.6 Write Short Note on (any 2)\n', '1      3
#              1  2   3\n', '6                                   5  8   6\n', '7   8  4                                7  4\n', 'Q.6)  Write short note on any 2.\n', '6. Write note on (Any two)\n', '6. Write note on (Any two)\n', '1) T(n) 4T(n/2)\n', 'ii) T(n) = 2T (n/2) +113\n', '3   (a) Let n - 4, (p1, 
# p2, p3, p4) - (100, 10, 15 , 27) and\n', '6. Write note on (any twn)H.\n', 'N=6 W=13,5,7,8,9,15 )&M=20\n', '6. Write short notes on (Any Four)\n', 'e)  
#  \n', 'Q. r$ -...,\n', 'c.--\t\n', '1 \t\n', 'C.:\n', '4.•;\\\t\n', '5.        3                               7\n', 'Q.6         Write a short note on(Any two)\n', '3.Recurrenses.\n', '6.       Write a short note on following (any 4) :\n', 'i) T(n) = 3n + 2\n', 'ii) T(n) = 10n2 + 2n + 1\n', "6. 'Write 
# note on :— (any two)\n", '6. Write note on : (any two)\n', 'Q6. Write note on (any two):\n', '1           18              3\n', '2           25
#      5\n', '3           27              4\n', '4           10              3\n', '5           15              6\n', 'Q.1 Answer the following\n', 'N=6 W={3,5,7,8,9,15} & M =20 Also write the Algorithm for it.\n', 'Q.6 Write Short Note on (any 2)\n', '1      3                                1  2   3\n', 
# '6                                   5  8   6\n', '7   8  4                                7  4\n', 'Q.6)  Write short note on any 2.\n']


# Analysis:
# INTRODUCTION TO ALGORITHMS:98
# DYNAMIC PROGRAMMING APPROACH:116
# GREEDY METHOD APPROACH:56
# BACKTRACK AND BRANCH-AND-BOUND:68
# STRING MATCHING ALGORITHMS:32
# NON DETERMINISTIC POLYNOMIAL ALGORITHMS:17
# CANNOT DETERMINE MODULE:79