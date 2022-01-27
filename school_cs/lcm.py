
def lcm(x, y):

   if x > y:
       greater = x
   else:
       greater = y

   while(True):
       if((greater % x == 0) and (greater % y == 0)):
           r = greater
           break
       greater += 1

   return r

print(lcm(2,2))