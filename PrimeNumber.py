def check_prime(n,i=2):
    if n==i:
        return True
    elif n%i==0:
        return False
    return check_prime(n,i+1)
n=int(input("Enter the value: "))
if check_prime(n):
    print("Yes!This is prime")
else:
    print("This not prime")