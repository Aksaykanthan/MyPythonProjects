
str = 'malayalam'
t = ''
k = -1
for i in str:
    t += (str[k])
    k -= 1

if str == t:
    print("Its a palindrome")
else:
    print("No it is not a palindrome")
