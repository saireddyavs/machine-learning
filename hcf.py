def hcf(a,b):
    small=a if a<b else b
    print(a,b)
    h=1
    for i in range(1,small+1):
        if a%i==0 and b%i==0:
            h=i
    return h

       

n1=int(input("enter n1"))
n2=int(input("enter n2"))
print("HCF of {} and {} is {}".format(n1,n2,hcf(n1,n2)))



