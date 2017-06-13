# -*- coding: utf-8 -*-
"""
Created on Mon Jun 12 16:57:57 2017

@author: pedro_2
"""
balance = 320000
annualInterestRate = 0.2
aux_balance = balance
annualInterestRate = 0.2
mIRate=annualInterestRate/12.0
mUnpaidBal = 0
minPay = 0
upper = balance*pow((1+mIRate),12)/12.0
lower = balance/12.0
epsilon = 0.01
while(abs(balance) >= epsilon):
    minPay = (upper+lower)/2
    balance = aux_balance
    for i in range(1,13):
        mUnpaidBal = balance - minPay
        balance = mUnpaidBal + mUnpaidBal*mIRate
    if(balance >0): # Did not pay enough to get balance to zero, the guess of minimum payment is too small.
        lower = minPay
    if(balance <0): # The guess is too big.
        upper = minPay
print("Lowest Payment:", round(minPay,2))