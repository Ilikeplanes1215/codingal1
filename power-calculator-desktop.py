# ===========================
# POWER CALCULATOR           
# ===========================

print("=== Power Calculator===")

#------------ PART 1: ask the two questions
base = int(input("Enter the base number: "))
exponent = int(input("Enter the power (exponent): "))


#------------ PART 2: the running total ------------
result = 1



#------------ PART 3 + 4: the loop that mutiplies ----------

result = 1
for i in range(1, exponent +1):
    result = result * base
    print("step", i, ": result =", result)



#---------- PART 5: the anwser
print("\nAnwser:", base, "to the power", exponent, "=", result)