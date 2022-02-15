"""
Given an integer list as input. Remove all numbers divisible by 5 as input [except 0). Replace every 0 with 99.
Print this new list as well as its size.
Input-> [10,0,3,4,5]
Output-> Size=3 
99,3,4
"""

def new_fun(n):
  if n%5!=0:
    return n  
  elif n==0:
    return 99

ls = [10,0,3,4,5]
size = 0
ln = len(ls)
nw_ls = []
for i in range(0,ln):
  e = ls[i]
  nw_ls.append(new_fun(e))
  size += 1
print(f"Size: {size}")
print(nw_ls)
