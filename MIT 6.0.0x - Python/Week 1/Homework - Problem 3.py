# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# Paste your code into this box 
s = 'ybzobgnz'
orders = []
ans=s[0]
for ch in range(0, len(s) - 1):
    if(s[ch] <= s[ch+1]):
        ans += s[ch+1]
    else:
            orders.append(ans)
            ans = s[ch+1]
orders.append(ans)
resp = ''
print(orders)
for s in orders:
    if(len(resp) < len(s)):
        resp=s
print("Longest substring in alphabetical order is:", resp)
#for strs in orders:
 #   if(strs.len() > resp.len()):
 #       resp = strs


        
    
