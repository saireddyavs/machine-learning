n=int(input("enter a number")
      )
div=False;
i=2;
while i<n:
    if n%i==0:
        div=True
        print("{} is divisible by {}".format(n,i))
    i=i+1
if(div):
    print("{} is not a prime number".format(n))
else:
    print("{} is a prime number".format(n))
