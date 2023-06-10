import time

print("")
print("THIS IS A FIT BODY CHECKER USING BMI.")
print("")
your_name = str(input("Can you tell me your name: "))
age = str(input("What about your age: "))

h = float(input("Enter your height: "))
w = float(input("Enter your weight: "))

h2 = h*h
bmi = w/h2

time.sleep(2)
print("So " + your_name + " !" + str(bmi) + " is your bmi number")
time.sleep(2)

if bmi < 18.5:
    print("You are skinny!!!")
elif bmi >= 18.5 and bmi <= 24.9:
    print("YOU are fit!!!")
elif bmi >= 25 and bmi < 30:
    print("You are little overweight!!!")
elif bmi <= 30 and bmi < 35:
    print("You are fat level 1")
elif bmi <= 35 and bmi < 40:
    print("You are fat level 2")
elif bmi >= 40:
    print("WARNING: YOU ARE FAT LEVEL 3!")
time.sleep(1)

print("")


ask = "no"
while len(ask) == 2:
    print("How is your body? Fat, skinny, or normal? We will give you advice!!! You can type: fat, normal, skinny.")
    q = ""
    while len(q) < 1:
        q = str(input("Type here: "))
    print("Your question is: 'What do I do? , I'm " + q + "', right?")
    ask = str(input("Yes or no: "))

if ask == "yes":
    print("")
    print("giving advice...")
    time.sleep(3)
    print("")
    if q == "fat":
        time.sleep(2)
        print("You should exercise regularly and eat a variety of vegetables.")
        time.sleep(2)
        print("You should also limit fat in grease, fast food.")
        time.sleep(2)
        print("Jogging, playing sports or hitting the gym are the methods to make you lose weight and get back to normal!!!")
    elif q == "skinny":
        time.sleep(2)
        print("You need additional food.")
        time.sleep(2)
        print("Exercising or hitting the gym can make your muscles stronger.")
        time.sleep(2)
        print("Try to supplement breakfast.")
    else:
        time.sleep(2)
        print("Wow, it's good that you have a healthy body!")
        time.sleep(2)
        print("But don't be subjective...")
        time.sleep(2)
        print("you still need to eat healthy and exercise regularly!!!")

time.sleep(2)

print("So " + your_name + ", it is my advice!!!")
time.sleep(2)
print("Try to keep your body healthy!")
time.sleep(2)

print("END")