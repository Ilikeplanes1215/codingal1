# ##########################################
# SWIMMING POOL ENTRY CHECKER
# ##########################################

print("=== Swimming Pool Entry Checker ===")
print("Answer 3 questions and I will tell you which pool you can use.\n")


# --------- collect the three answers ---------
# YOUR CODE HERE
age = int(input("How old are you? "))
can_swim = input("Can you swim 25 metres? (yes / no): ").lower()
adult_here = input("Is an adult with you? (yes / no): ").lower()

print()
print("=== Entry Decision ===")
print("-" * 32)


# --------- PART 1: age group, using if / elif / else on a NUMBER ---------
# YOUR CODE HERE
if age < 4:
    print ("Age group      :toddler - splash pool only, always with an adult")
elif age < 12:
    print("Age group      :Child - main pool with an adult")
elif age < 18:
    print("Age group      :Teen- main pool alone if you can swim")
else:
    print("Adult     : all pools open to you")
# Order matters here in a way it did not in class. The instructions explain why.


# --------- PART 2: did they actually answer yes or no? ---------
# YOUR CODE HERE
if can_swim != "yes" and can_swim != "no":
    print("Input error:please answer the swimming question with yes or no")
    swim_known = False
else:
    swim_known= True
if adult_here != "yes" and adult_here != "no":
    print("Input error: please anwser the swimming question with yes or no")
    adult_known = False
else:
    adult_known = True


# --------- PART 3: AND - the deep pool ---------
# YOUR CODE HERE
if can_swim == "yes" and adult_here == "yes":
    print("Deep pool allowed. You can swim, and adult is present")


# --------- PART 4: OR - the shallow end ---------
# YOUR CODE HERE
if age < 12 or can_swim == "no":
    print("Shallow only: Stay in the shallow end today")

# --------- PART 5: NOT - the lifeguard reminder ---------
# YOUR CODE HERE
if adult_known == "true" and adult_here == "no":
    print("reminder: No adult with you, the life guard must be informed") 


# --------- PART 6: The final verdict ---------
if swim_known == False or adult_known == False:
    print("Cannot decide until both questions are answered properly.")
elif age >= 18 and can_swim == "yes":
    print("Please follow this instruction: Full access. Enjoy your swim.")
elif age >= 12 and can_swim == "yes" and adult_here == "yes":
    print("Please follow this instruction: Main pool access with your adult nearby.")
elif can_swim == "no" and not (adult_here == "yes"):
    print("Please follow this instruction: Shallow end only, and please find an adult first.")
else:
    print("Please follow this instruction: Shallow end today - come back with an adult for more.")
# First: If either answer was not understood, refuse to decide.
# Then work through the real cases with elif, ending in a plain else.


print()
print("Have a safe swim!")