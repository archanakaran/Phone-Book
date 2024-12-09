# x='hii'
# le=len(x)
# print(le)
# for i in x:
#     print(i)
x=int(input('enter the first number'))
y=int(input('enter the last nummber'))
sum=0
for i in range(x,y):
    if i%2!=0:
      sum=sum+i
print(sum)

