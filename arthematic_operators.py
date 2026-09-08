#1

a=int(input("enter a:"))
b=int(input("enter b:"))
print("a+b:",a+b)
print("a-b:",a-b)
print("a/b:",a/b)
print("a*b:",a*b)
print("a%b:",a%b)

#2

r=int(input("enter r:"))
area=3.14*r*r
print("area=",area)

#3

p=int(input("enter p:"))
r=int(input("enter r:"))
t=int(input("enter t:"))
s=(p*r*t)/100
print("si=",s)

#4

c=float(input("enter celcius="))
f=(c*9/5)+32
print("farhenheit=",f)
cel=(f-32)*5/9
print("cel=",cel)

#5

n=int(input("enter a no:"))

if n%3==0 and n%5==0:
    print("divisible by 3 and 5")
elif n%3==0:
    print("divisible by 3")
elif n%5==0:
    print("divisible by 5")
else:
    print("division not possible")

      

