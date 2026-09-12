print("======= Smart School Day Planner ========")
print("Can you anwser 3 questions that will help me plan your day?")
day=input("what day is it? (Monday to Sunday) : ")
weather=input("what is the weather? (sunny, rainy, cloudy)  : ")
homework=input("did you do your homework? (yes, no): ")
print()
print(f"===your plan for {day}=== ")  
print("-"*35)

if day in ("Saturday", "Sunday"):
    print("Day type: Weekend : Golf as much as possible.")
elif day ==("Monday"):
    print("Day type: Start of the week. Get prepared to grind through the week!")
elif day in ("Tuesday", "Wednesday", "Thursday"):
    print("Day type: Middle of the week. Regular day--stay focused!")
elif day ==("Friday"):
    print("Day type: Last day of the week. Way to get thru the school week--time for fun")
else:
    print("Error! day type not recognized, maybe capitalize the day")
if (homework=="yes" and weather == "sunny"):
    print(" Go to the park after school.")

if (weather == "rainy" or weather == "cloudy"):
    print("Pack an umbrella")
if not (homework == "yes"):
    print("Your homework is not done yet. Hit the books, son.")
elif weather == "sunny" and homework == "yes" and not (day in ("Saturday", "Sunday")):
    print("You're set for a good school day")
elif day in ("Saturday", "Sunday"):
    print("You're set for a good weekend")
else:
    print("Plan complete!Have a wonderful day")