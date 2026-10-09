# Student App Access Manager
 
# Permission constants asigined a power of 2
CAMERA = 4       # 0100
MICROPHONE = 2   # 0010
STORAGE = 16     # 10000
LOCATION = 8     # 1000
 
# app lists
approved_apps = [
    "coding",
    "calc",
    "reading",
    "sports"
]
 
# Get student input
student_name = input("What is your name? ")
requested_app = input("Which app do you want to use? ").lower()
 
print("\n--- Identity Operator Check ---")
 
# Use 'is' to check the data type
if type(student_name) is str:
    print("The student name is stored as text.")
 
# Use 'is not' to make sure it's not an integer
if type(requested_app) is not int:
    print("The requested app is not stored as an integer.")
 
 
print("\n--- Membership Operator Check ---")
 
# Use 'in' to check whether the app in or not in
if requested_app in approved_apps:
    print(requested_app, "is an approved app for ", student_name + ".")
else:
    print(requested_app, "is not an approved app.")
 
# Use 'not in' to check restricted apps
restricted_apps = [
    "instagram",
    "online",
    "ai"
]
 
if requested_app not in restricted_apps:
    print("The app is not on restricted list.")
else:
    print("This app is restricted.")
 
 
print("\n--- App Permission Settings ---")
 
# Combine Camera, Mike, and Storage permissions using the bitwise OR operator
student_permissions = CAMERA | MICROPHONE | STORAGE
 
# Display the permission number in binary
print("Permission value:", student_permissions)
print("Permission bits:", bin(student_permissions))
 
# Check permissions using the bitwise AND operator
if student_permissions & CAMERA:
    print("Camera permission: Enabled")
 
if student_permissions & MICROPHONE:
    print("Microphone permission: Enabled")
 
if student_permissions & STORAGE:
    print("Storage permission: Enabled")
 
if student_permissions & LOCATION:
    print("Location permission: Enabled")
else:
    print("Location permission: Disabled")
 
 
print("\n--- Bit Shift Demonstration ---")
 
# Shift the CAMERA bit left to create the next permission value
next_permission = CAMERA << 1
 
print("Camera bit:", bin(CAMERA))
print("After left shift:", bin(next_permission))
 
# Shift the STORAGE bit right
previous_permission = STORAGE >> 1
 
print("Storage bit:", bin(STORAGE))
print("After right shift:", bin(previous_permission))
 
 
print("\n--- Final Access Result ---")
 
# Check both app approval and permission availability
if requested_app in approved_apps and requested_app not in restricted_apps:
    print("Access granted to", requested_app)
else:
    print("Access denied to", requested_app)
