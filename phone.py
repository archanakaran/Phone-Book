print('1.Create')
print('2.Read')
print('3.Update')
print('4.Delete')
print('5.Delete all')
print('6.view')
print('7.Display all')
print('8.exit')
d={}

while True:
 subd={}
 var1=int(input('enter a number'))
 if var1==1:
   name=input('enter name')
   phno=int(input('enter phno'))
   email=input('enter email')
   subd['name']=name
   subd['phno']=phno
   subd['email']=email
   # print(subd)
   d[name]=subd
   # print(d)
 elif var1==2:
   print(d)
   
 elif var1==3:
    name1=input('enter the student')
    if name1 in d:
      print('1.name')
      print('2.phno')
      print('3.email')
    else:
        print('wrong name')
        break
    var2=int(input('enter the choice')) 
    if var2==1:
      up=input('what do you want to update')
      valu1 = input(f'Enter the new {up}: ')
      d[name1][up]=valu1
    if var2==2:
      up=input('what do you want to update')
      valu1 = input(f'Enter the new {up}: ')
      d[name1][up]=valu1
    if var2==3:
      up=input('what do you want to update')
      valu1 = input(f'Enter the new {up}: ')
      d[name1][up]=valu1
    
 elif var1==4:
              name2=input('enter the name')
              if name2 in d:
                 del1=input('what do you want to delete')
                 del d[name2][del1]
                 
              else:
                 print('wrong name')
 elif var1==5:
    d.clear()

 elif var1==6:
    name3=input('enter the name')
    if name3 in d:
       print(d[name3])
    else:
       print('wrong name')


 elif var1==7:
    print(d)

 
 elif var1==8:
    print('Exit')

 else:
    print('Wrong choice')





   

