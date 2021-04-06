sum=0
num=int(input("Enter a natural number: "))
num2=num
num3=num
while num2>=1:
    num2=num2/10
    sum=sum+1
zero=0
even=0
odd=0

for i in range(sum):
    yekan=num3%10
    if yekan==0:
        zero=zero+1        
    if yekan%2==0 and yekan!=0:
        even=even+1
    else:
        odd=odd+1
    num3=num3//10    

print(num,"","has",sum,"","digit(s).")
print(num,"","has",zero,"","zero(s).")
print(num,"","has",even,"","even digit(s).")
print(num,"","has",odd,"","odd digit(s).")
    
