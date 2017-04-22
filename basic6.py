print ("Enter the Money amount in ($) :")
moneyPound= int(input())

moneyEuro= moneyPound * 1.1949

print("in Pound : {0}  money in Euro :: {1}" .format(moneyPound,moneyEuro))

note50= int(moneyPound / 50);
remaining= moneyPound % 50
note20= int(remaining / 20);
remaining= moneyPound % 20
note10= int(remaining / 10);
remaining= moneyPound % 10
note5= int(remaining / 5);
remaining= moneyPound % 5


print ( " note50 : {0} :note20 : {1} : note10 : {2} :note5 : {3}".format(note50,note20,note10,note5))
print ( " remain : {0}".format(remaining))

# print ("total No Of Notes :: 50 :{0}  ")
