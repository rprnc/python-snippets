#quick n dirty flatten function to remove nested lists

def flatten(l):
   result = []
   for el in l:
     if isinstance(el, list):
       flat = flatten(el)
       result += flat
     else:
       result.append(el)
   return result