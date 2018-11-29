'''
Convert from F to C, and from C to F
'''
degree = input("Enter c for celsius, or f for Fahreihelt :")
temperature = int(input("Enter the temperature value : "))

if degree =='f':
    C = (temperature - 32)*5/9
    print("The temperature in celsius is ",round(C))
elif degree =='c':
    F = temperature*5/9 +32
    print("The temperature in Fahreiheit is :", round(F))
else:
    print("There is no such type of degree like :", degree)

exit()
