import array
import array as arr

a = arr.array("f",[1,2,3,4,5,6])

b = arr.array("f",[11,12,13,14,15,16])

c = arr.array("f")

a.append(8)  # to add a number

a.extend([9,8,7])  # to add multiple numbers

a.insert(2,6) # to insert a number in middle (index)

a.remove(1) # to remove a number

a.pop() # to pop out a number  using index

print(a[0:4]) # sliceing a array




