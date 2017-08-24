string = raw_input("Type sentence to verify ")


Rstring = reversed(string)

if list(string) == list(Rstring):
 
  print("It is palindrome")

else:

   print("It is not palindrome")