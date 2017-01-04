import re
print('Simple Calculator\n**********************')
print( 'Commands\n >Type quit to exit \n >Type clear to enter new Equation\n')
previous = 0
previousValue=0
run=True
def performMath():
    global run
    global previous
    global previousValue
    equation=""
    if (previous==0):
        equation= input("Enter Equation:")
    else:
        equation = input(str(previous))
        if(equation =="clear"):
            previous=0
            equation=input("Enter Equation:")
    if(equation=='quit'):
        previous = 0
        print('GoodBye')
        run=False
    else:
        equation=re.sub('[a-zA-Z,.:() " "]',' ',equation)
    if equation.isspace():
        equation = input("Enter Equation:")
    else:
        if(previous==0):
            previous= eval(equation)
            print(equation,"=", previous)
        else:
            previousValue=previous
            previous=eval(str(previous)+ equation)
            print(previousValue,equation, "=", previous)

while run:
    performMath()
