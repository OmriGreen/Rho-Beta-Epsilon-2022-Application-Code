import math

class main:
    
    #Input
    robotInput = input()
    allowedNum = input()
    #Postion Variables
    x = 0
    y = 0
    theta = 0
    
    #Seperates all of the variables
    r = 0 #right
    l = 0 #left
    f = 0 #forwards
    b = 0 #backwards
    
    i = 0; #Where you are in the code
    
    invalidInput = ""
    
    
    #The code below dows all of the calculations
    inputLength = len(robotInput)
    
    if(inputLength%2 != 0):
        print("Invalid Entry")
    else:
        for val in robotInput:
            if val == "R":
                if(int(allowedNum) > 2*int(robotInput[i-1])):
                    theta-=math.pi/2*int(robotInput[i-1])
                else:
                    invalidInput += robotInput[i-1]+robotInput[i]
            if val == "L":
                if(int(allowedNum) > 2*int(robotInput[i-1])):
                    theta+=math.pi/2*int(robotInput[i-1])
                else:
                    invalidInput += robotInput[i-1]+robotInput[i]
            if val == "F":
                if(int(allowedNum) > 2*int(robotInput[i-1])):
                    if theta % math.pi == 0:
                        y+=math.cos(theta)*int(robotInput[i-1])
                    else:
                        x+= math.sin(theta)*int(robotInput[i-1])
                else:
                    invalidInput += robotInput[i-1]+robotInput[i]

            if val == "B":
                if(int(allowedNum) > int(robotInput[i-1])):
                    if theta % math.pi == 0:
                        y-=math.cos(theta)*int(robotInput[i-1])
                    else:
                        x-= math.sin(theta)*int(robotInput[i-1])
                else:
                    invalidInput += robotInput[i-1]+robotInput[i]

            i+=1
    
    #Cleans up theta
    while theta >= 2*math.pi:
        theta -= 2*math.pi
    while theta <= -2*math.pi:
        theta += 2*math.pi
        
    #converts theta from radians to degrees
    theta = theta/math.pi * 180
        
    print(str(x) + " " + str(y) + " " + str(theta))
    print(invalidInput)
    
    