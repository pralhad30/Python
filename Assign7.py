def end_other(a, b):
   a = a.lower()
   b = b.lower()
   return (b.endswith(a) or a.endswith(b))

print end_other('Hiabc', 'abc') 
print end_other('AbC', 'HiaBc')
print end_other('abc', 'abXabcd')
