import mytemp as t

c=int(input("enter your temp in C and we will provide the F temp: "))

print(c, "celcius is equivalent to", t.celtofeh(c))

f=int(input("enter your temp in F and we will provide the C temp: "))

print(f, "farenheit is equivalent to", t.fehtocel(f))
