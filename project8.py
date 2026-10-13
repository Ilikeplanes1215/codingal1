#----------- PART 1: what did this week's shop cost per person? -----------
# YOUR CODE HERE
# Store these five values in variables:
rice_price = 12
milk_price = 4
fruit_price = 8
number_of_baskets = 2
family_members = 4
basket_cost_per_person = int((rice_price + milk_price + fruit_price) * number_of_baskets / family_members)
print(basket_cost_per_person)

# ----------- PART 2: Can the items be shared equally? -----------
# YOUR CODE HERE
total_items = int(input("Enter the total number of the grocery items: "))
people = int(input("Enter the total number of people: "))
if people == 0:
    print("You cannot share items between 0 poeple")
else:
    #use % to check divisibility:
    if total_items % people == 0:
        print(total_items, "item divde eqally among", people, "people-", total_items // people, "each")
#  remainder 0  -> say they divide equally, and use // to say how many each=========================
# GROCERY COST COMPARISON TOOL
# ===================================

print("=== GROCERY COST COMPARISON TOOL ===")


# ----------- PART 3: fix the weekly average -----------
# YOUR CODE HERE
recorded_average = 65
total_weeks = 4
wrong_week_cost = 50
correct_week_cost = 80
recorded_total = recorded_average * total_weeks
corrected_total = recorded_total - wrong_week_cost + correct_week_cost
corrected_average = corrected_total / total_weeks


# ----------- PART 4: compare with three stores -----------
store_a_average = 70
store_b_average = 75
store_c_average = 80
if corrected_average < store_a_average and corrected_average < store_b_average and corrected_average < store_c_average:
    verdict = "cheaper than all three stores"
elif corrected_average > store_a_average and corrected_average > store_b_average and corrected_average > store_c_average:
    verdict = "more expensive than all three stores"
else:
    verdict = "somewhere in between the three stores"


# ----------- PART 5: the summary -----------
print("\n=== SUMMARY ===")
print("Cost per person this week:", basket_cost_per_person)
print("Corrected average:", corrected_average)
print("Verdict                  :", verdict)
# **********************************
# GROCERY COST COMPARISON TOOL
# **********************************