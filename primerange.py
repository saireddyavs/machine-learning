n1=int(input("Enter n1"))
n2=int(input("enter n2"))
for i in range(n1,n2):
    if i>1:
        div=False
        for k in range(2,i):
            if i%k==0:
                div=True
        if not div:
            print(i,"is prime")
        else :
            print(i,"is not prime")
