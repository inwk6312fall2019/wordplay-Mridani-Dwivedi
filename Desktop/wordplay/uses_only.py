#9.3 uses_only
def uses_only(word,string):
    for lett in word:
      if lett not in string:
        print(lett)
        return False
    return True
 print(uses_only('mridaaanbr','mridanb'))
