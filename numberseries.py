nterms = int(input("How many terms? "))
n1, n2 = 0, 1
count = 0
if nterms <= 0:
   print("Please enter a positive integer")
elif nterms == 1:
   print("Fibonacci sequence upto",nterms,":")
   print(n1)
else:
   print("Fibonacci sequence:")
   res = [0, 1]
   while True:
        nth = n1 + n2
        if nterms < nth:
           break;
        res.append(nth)
        n1 = n2
        n2 = nth
    
print(res)
