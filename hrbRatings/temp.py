import numpy as np

a = np.array([[2,1], [1,3]])

print(np.dot(a,a))

print(np.log(0.5))

a = np.random.randn(3,4)
b = np.random.randn(1,4)

c = a + b

print(f'c = {c}')
print(f'c.shape = {c.shape}')

a = np.random.randn(1,3)
b = np.random.randn(3,3)
c = a*b

print(f'c = {c}')
print(f'c.shape = {c.shape}')