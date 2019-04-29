class Foo(object): 
    def __nonzero__(self): 
       print('Foo is evaluated to a boolean!')
       return True
       #return False


x = Foo() 

if x: 
   print('if x') 
if x is not None: 
   print('if x is not None')
   

