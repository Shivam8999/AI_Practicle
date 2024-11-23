import nltk 
from nltk.corpus import stopwords 

f1 = open("file1.txt", "r")
f2 = open("file2.txt", "w")
stop = stopwords.words('english')
for line in f1:
    w = line.split()
    for word in w:
        if word not in stop:
            f2.write(word + " ")
f1.close()
f2.close()
