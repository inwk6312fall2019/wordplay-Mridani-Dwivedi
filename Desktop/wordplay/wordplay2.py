#Write a function named avoids that takes a word and a string of forbidden letters, and that returns True if the word doesn’t use any of the forbidden letter

def avoids(word,string):
   for let in word:
     if let in string:
       return False
   print(word)
   return True
print(avoids('mridani','ybc'))
#Write a program that prompts the user to enter a string of forbidden letters and then prints the number of words that don’t contain any of them. Can you find a combination of 5 forbidden letters that excludes the smallest number of words?
def avoiding():
  count=0
  string=input('enter the forbidden string\t')
  fin=open('words.txt')
  for line in fin:
      word=line.strip()
      if(avoids(word,string)):
          
          count+=1

  print(count)
avoiding()