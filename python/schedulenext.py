import datetime
import calendar


date = datetime.datetime.today().strftime('%A')

print("")
print("Today is {}".format(date))
print("")

if date == ("Sunday"):
    print("---------")
    print("Tommorow you have:")
    print("Business 2x")
    print("Philo 2x")
    print("His 2x")
    print("BG 1x")

if date == ("Monday"):
    print("---------")
    print("Tommorow you have:")
    print("Geo 2x")
    print("Esp 2x")
    print("Eng 2x")
    print("Chem 1x")

if date == ("Tuesday"):
    print("---------")
    print("Tommorow you have:")
    print("His 2x")
    print("BG 2x")
    print("Math 1x")
    print("Esp 2x")

if date == ("Wednesday"):
    print("---------")
    print("Tommorow you have:")
    print("Chem 2x")
    print("Bio 2x")
    print("Phys 1x")
    print("Eng 2x")

if date == ("Thursday"):
    print("---------")
    print("Tommorow you have:")
    print("Phys 2x")
    print("Maths 2x")
    print("PE 2x")

if date == ("Friday"):
    print("YOU'RE FREE")

if date == ("Saturday"):
    print("YOU'RE FREE")


print("---------")
