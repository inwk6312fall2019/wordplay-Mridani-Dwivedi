
#9.4 uses_all

 def uses_all(word,string):
    for lett in string:
      if not(lett in word):
        print(lett)
        return False
    return True
 print(uses_all('mridai','mrdan'))
