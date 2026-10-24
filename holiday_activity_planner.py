print("=============== Holiday Activity Planner===============")
print("I'm gonna ask you a few questions to plan your holiday")
choice = int(input("Enter 1 for beach holiday and 2 for mountains holiday: "))
if choice == 1:
    activity = int(input("chose an activity enter 1 for swimming or 2 for building sandcastles: "))
    if activity == 1:
        print("Activity: Swimming; Don't forget to pack your bathing suit")
    else:
        print("Activity: Building Sandcastles ; Bring a shovel")
elif choice == 2:
    activity2 = int(input("Enter 1 for hiking or 2 for camping: "))
    if activity2 == 1:
        print("Activity: Hiking; You should probabaly bring two pairs of shoes")
    else:
        print("Activity: Camping; Get bug repellent just in case")
else:
    print("That was not a valid choice")
print("=============== Enjoy your holiday ================")