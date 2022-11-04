"""vector nuevo con los tienen un solo digito, los demas con 0"""

import random

n = [random.randint(0,100) for i in range(10)]
print(n)

digito = [x if x < 10 else 0 for x in n]
print (digito)

