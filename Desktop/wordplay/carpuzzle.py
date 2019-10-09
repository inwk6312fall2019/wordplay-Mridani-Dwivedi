
#cartalk1puzzller-Mississippi
def fun(word):
  print(word)
  i=0
  
  count=0
  n=len(word)
  print(n)
  while i<len(word)-1:
    
      if word[i]==word[i+1]:
        count+=1
        i+=2
        if count==3:
          print("word has 3 double consec")
      else:
        
        count=0
        i+=1
  
  print(count)

fun('missiippii')