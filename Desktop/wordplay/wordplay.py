#To print word of length more than 20
fin=open('words.txt')
line=fin.readline()
for line in fin:
    word=line.strip()
    if(len(word)>20):
        print(word)

#program that reads words.txt and prints only the words that have no “e”. Compute the percentage of words in the list that have no “e”
fin=open('words.txt')

def has_no_e():
    total=0
    count=0
    line=fin.readline()
    for line in fin:
        word=line.strip()
        total=total+1
        if not('e' in word):
            print(word)
            count=count+1
    perc=(count/total)*100
    print("Percantage of words that do not have 'e'",perc)
            
has_no_e()

#function named uses_only that takes a word and a string of letters, and that returns True if the word contains only letters in the list.
def uses_only(word,string):
    for letter in word:
        if letter in string:
            return True
        elif letter not in string:
            return False
print("Please enter the word")
wor=input()
print("Please enter the string of letters:")
mys=input()
uses_only(wor,mys)

