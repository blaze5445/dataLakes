import numpy as np

# Question 1
d_04 = 1/(1+0.081)**4
print('Q1\nThe discount rate is {}'.format(np.round(d_04,3)))

# Question 2
s = [0.07,0.073,0.077,0.081,0.084,0.088] # term structure interest rates
d = [1/(1+s[i])**(i+1) for i in range(len(s))] # discout rates
X = (1-d[5])/np.sum(d[:6])
print('Q2\nThe swap rate is {}%'.format(100*np.round(X,4)))

# Question 3
print('Q3\nShe can formulate a perfect hedge by shorting 10 futures contracts today(total 150000 pounds), so the risk-free price is just 118.65 cent/pound')

# Question 4
cov = 0.7*0.2*0.25 # corr times stdev.
y = 10*(cov/0.2**2)
print('Q4\nShe needs about {} orange futures contracts to minimize hedge vairance'.format(np.round(y)))

# Question 5,6
A = np.array([[105,1.02],[100*(1/1.05),1.02]])
B = np.array([3,0]) # 105x + 1.02y = 3; 100*(1/1.05) + 1.02y = 0
res = np.linalg.inv(A).dot(B)
v = 100*res[0] + res[1]
print('Q5&6\nThe (arbitrage-free) value of the call is {}; you need to invest {} dollar'.format(np.round(v,2),np.round(res[1],3)))