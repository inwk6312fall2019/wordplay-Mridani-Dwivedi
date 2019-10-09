 
#9.3 abcedarian
def is_abcedarian(word):
  i=0
  while i<len(word)-1:
      if word[i+1]<word[i]:
        print(word[i])
        return False
      i=i+1
  return True
print(is_abcedarian('mrszi'))


