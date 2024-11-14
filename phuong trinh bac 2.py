#!/usr/bin/env python
# coding: utf-8

# In[25]:


a = float(input('a='))
b = float(input('b='))
c = float(input('c='))
d = b**2-4*a*c
if a != 0:
    if d > 0:
        x = (-b-(d**0.5))/(2*a)
        y = (-b+(d**0.5))/(2*a)
        print (f'phương trình có 2 nghiệm phân biệt x1 = {x}, x2 = {y}')
    elif d == 0:
        x = y = (-b)/(2*a)
        print(f'phương trình có nghiệm kép là x = y = {x or y }')
    else:
        print ('phuong trình vô nghiệm')
else:
    print('phương trình k hợp lệ')

