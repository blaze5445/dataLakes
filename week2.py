# Question 1
payment = 500000
r_1 = 0.1
result_1 = payment + payment*((1/r_1)-1/(r_1*(1+r_1)**19))
print('Q1\nThe present value is: {}'.format(result_1/1000000))

# Question 2
r_2 = 0.12
discount = 1/(1+r_2)
stay = -1000-(1000*discount)*(1-discount**5)/(1-discount)+1000*(discount**6)
switch = -900 - 900 - (900*discount)*(1-discount**5)/(1-discount)+ 900*(discount**6)
print('Q2\nStay costs {}, switch costs {}, so choose {}'.format(-stay,-switch,'stay' if stay > switch else 'switch'))

# Question 3
d_02 = 1/(1+0.069)**2
print('Q3\nThe discount rate is {}'.format(d_02))

# Question 4
f_12 = ((1+0.069)**2/(1+0.063))-1
print('Q4\nThe forward rate is {}'.format(f_12*100))

# Question 5
d_09 = 1/(1+0.02)**3
F = 400/d_09
print('Q5\nForward price is {}'.format(F))

# Question 6
diff = 10000/0.08-10000/0.1 # discount using two rates
print('Q6\nThe difference between upper and lower bound is {}'.format(diff))

# Question 7
F_0 = 100/(1/(1+0.1/2)**2)
F_t = 125/(1/(1+0.1/2))
f = (F_t-F_0)*(1/(1+0.1/2))
print('Q7\nThe forward value is {}'.format(f))
