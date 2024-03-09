

#que: create a calculator of perfoming addition,substraction,multiplication,division operations and take value by user

x= input('Enter Your first value :')
y= input('Enter Your second value? :')


op= input('what you perform please press your operation key :')
 

match op:
      
    case '+':
      sum = int(x) + int(y)
      print('Your values Addition is: ',sum )
       
    case '-':
      sub = int(x) - int(y)
      print('Your values Substraction is: ',sub )
         
    case '*':
      mul = int(x) * int(y)
      print('Your values multiplication is: ',mul )

    case '/':
      div = int(x) / int(y)
      print('Your values division is: ',div )

    case '%':
      mod = int(x) % int(y)
      print('Your values modulas is: ',mod )

    case _ :
      print('Enter valid choice option')
