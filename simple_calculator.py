def add_func (x1,x2):
    r= int(x1) +int(x2)
    return r
def sub_func (x1,x2):
    r= int(x1) - int(x2) 
    return r   
def mul_func (x1,x2):
    r= int(x1) *int (x2)
    return r
def div_func (x1,x2):
    r= int(x1)/int(x2)
    return r

op=''


while True:
    x1=input("Please Enter the first number:\n")
    x2=input("Please Enter the second number:\n")
    op= input("Please select which operation you want to perform: '+' or '-' or '*' or '/'\n")
    if x2=='0' and op=='/':
        print("Error : Cannot Divid By Zero !\n")
        
    elif x1.isdigit() and x2.isdigit():
         if(op=='+'):
            print(f"The result of {x1} + {x2} is {add_func(x1,x2)}\n")
         if(op=='-'):
            print(f"The result of {x1} - {x2} is {sub_func(x1,x2)}\n")
         if(op=='*'):
            print(f"The result of {x1} * {x2} is {mul_func(x1,x2)}\n")
         if(op=='/'):
            print(f"The result of {x1} / {x2} is {div_func(x1,x2)}\n") 

    else:
        print("Please Enter valid inputs\n")          
