#by euclid's theorem , gcd(m,n)=gcd(n,m-n) where m>n
def gcd(m,n):
    if m<n:
        (m,n) =(n,m)
    while (m % n) != 0:

        (m,n) = (n,m%n)
    print(n)

m= int(input("enter no 1 "))
n= int(input("enter no 2 "))
gcd(m,n)
