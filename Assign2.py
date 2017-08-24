a = raw_input("Provide sentence with multiple words")

def reverse(a):
    B = a.split()
    B_reversed = B[::-1]  
    print B_reversed      
    return' '.join(B_reversed)

print reverse(a)