import random
l=[]
n=[]
s=[]
lst=[]
#l=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in 'abcdefghijklmnopqrstuvwxyz':
  l.append(i)
for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
  l.append(i)
for i in '1234567890':
  n.append(i)
s=['!','@','#','$','%','&','*']
a=input(("Enter the no of letter: "))
b=input(("Enter the no of digits: "))
c=input(("Enter the no of symbols: "))
for chr in range(1,int(a)+1):
  lst.append(random.choice(l))
for chr in range(1,int(b)+1):
  lst.append(random.choice(n))
for chr in range(1,int(c)+1):
  lst.append(random.choice(s))
random.shuffle(lst)
pas=''
for chr in lst:
  pas=pas +chr
print("Your generated password is: ",pas)