
try:
    age = int(input('Enter Your Age : '))

    if age >= 18:
        print('Your Are Eligible For Voting')
    else:
        print('Your Are Not Eligible For Voting')
except ValueError:
    print("Try Again ! Only Whole Numbers Are Allowed")