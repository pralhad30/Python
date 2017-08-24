import random

import string


def letters(y):
  
 return ''.join(random.choice(string.ascii_letters) for x in range(y))
  


def Password():
  
 size_let = random.randrange(5, 9)
  
 size_num = random.randrange(1,5)
  
 size_sym = random.randrange(1,3)
  
 let = letters(size_let)
  
 numbers = ''.join(map(str, random.sample(range(1,5), size_num)))
  
 symbols = ''.join(map(str, random.sample('!@#$%^&_-', size_sym)))
  
 merge = list(let + numbers + symbols)
  
 random.shuffle(merge)
  
 password = ''.join(merge)
  
 print(password)
  
 
Password()