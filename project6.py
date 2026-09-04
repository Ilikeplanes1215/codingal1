# you must ask for today's temperature

temperature = int(input("Enter the temperature in Fahrenheit: "))

# do we do an indoor or outdoor activity
if temperature < 55:
    activity = "Do coding homework"
    print("Do indoor activities, like coding homework")
else:
    activity = "Play outside"
    print("do activities outside")
raining = input("Is it raining? (yes/no):  ")
if raining == "yes":
    print("bring an umbrella or stay indoors")
homework_time = int(input("How long will your homework take in minutes? "))
if homework_time > 40:
    print("It is a good idea to do your homework now.")
else:
    print("Eh...it can be done later")
free_time = input("Do you have free time today? (yes/no): ")
if free_time == "yes":
    final_task = "Time to play video games!"
    print("Ample free time.", final_task)
else:
    final_task = "Sorry you're cooked!"
    print("you do not have free time.", final_task)



print("====== daily activity planner ======")

print("temperature :", temperature)
print("activity chosen :", activity)
print("raining :", raining)
print("homework length in minutes :", homework_time)
print("final task", final_task)