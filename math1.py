import math

print ("Enter the redious ")
circleRedius= int(input())
circleAera= (math.pi * circleRedius * circleRedius  )
circleCircumference= (math.pi * 2 * circleRedius  )

print ("input  is :{0} , Aera : {1} ,Circumference :{2} ".format(circleRedius, round(circleAera,2), round(circleCircumference,2)))
