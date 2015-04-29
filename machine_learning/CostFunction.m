x = [1,2,3]
y = [1, 2, 3]
theta1= 0
h=theta1*x
m = length(y)
sqrdiff = (h-y).^2
J=(1/(2*m))* sum (sqrdiff)