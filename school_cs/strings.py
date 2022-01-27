str = "Python"
vowels = ['a','e','i','o','u'] 
n_vowels = 0
n_consonents = 0
n_upper = 0
n_lower = 0

for i in str:
     if i.isupper():
          n_upper +=1
     else:
          n_lower +=1
     
     if i.lower() in vowels:
          n_vowels +=1
     else:
          n_consonents+=1

print(f'''
      There are {n_vowels} vowels in "{str}"
      There are {n_consonents} consonents in "{str}"
      There are {n_upper} upper case in "{str}"
      There are {n_lower} lower case in "{str}"
      ''')
