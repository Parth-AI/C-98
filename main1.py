word_count = 0

file1 = open("text.txt","r")
#print(file1.readline())

for i in file1:
     word = i.split(",")
     print(word)
     word_count = word_count+len(word)
     print(word_count)
          