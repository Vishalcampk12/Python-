c = float(input("Enter the temperature in degree Celcius: "))
f = c * 1.8 + 32
print("%.1f degree celcius is %.1f degree fahrenheit" %(c, f))
if(f >= 104):
    print("It's hot")
elif(f <= 50):
    print("It's cold")
else:
    print("It's a nice day")