#!/usr/bin/env python
# coding: utf-8

# In[80]:


import numpy as np
import getpass as gt

n = int(input("n = "))
k = int(input("k = "))
step = int(gt.getpass("""Press zero if you would like to see the steps 
(else, press any other number)
"""))
print(" ")

def first(n, k):
    # a) Creating a list of size n
    a = np.arange(n) + 1
    c = 0
    # Display the original list, if asked
    if step == 0:
        print("Step", c, ":", a)
    
    while n > 1:
        # When size of the list is larger than k
        if n > k-1:
            # c1 gives the index of the kth element
            c1 = k-1
            
            # Changing every kth element to zero
            while c1 < n:
                a[c1] = 0
                # updating c1
                c1 = c1 + k
            
            # Appending the survivors in the original list
            for i in a:
                if i!=0:
                    a = np.append(a, i)
            
            # Finding the largest index among the zeroes
            zero = np.where(a == 0)
            last = np.max(zero)

            # Removing the elements before the last zero
            a = a[last + 1:]
    
            # Removing repeated numbers if any
            a = np.array(list(dict.fromkeys(a)))
            
            # Updating n as the length of the list
            n = len(a)

            # Adding the steps if asked
            if step == 0:
                c += 1
                print("Step", c, ":", a)
                
        # When size of the list is smaller than k
        elif n <= k-1:
            # c2 gives the index of the kth element
            c2 = k - 1 - n
            
            # Reducing c2 in case it becomes larger than length of the list
            while c2 > n - 1:
                c2 = c2 - n   

            # Changing every kth element to zero
            a[c2] = 0

            # Appending all the survivors in the original list
            for i in a:
                if i!=0:
                    a = np.append(a, i)
                    
            # Finding the largest index among the zeroes
            zero = np.where(a == 0)
            last = np.max(zero)

            # Removing the elements before the last zero
            a = a[last + 1:]

            # e) Removing repeated numbers if any
            a = np.array(list(dict.fromkeys(a)))

            # Updating n as the length of the list
            n = len(a)

            # Adding the steps if asked
            if step == 1:
                c += 1
                print("Step", c, ":", a)
    return a[-1]

print("Survivor:",first(n, k))


# In[ ]:




