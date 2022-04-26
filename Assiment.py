# Write Program to Exchange the Values of Two Numbers Without Using a Temporary Variable
a=50 
b=30 
a,b=b,a 
print(a,b)

print("--------------------------------END-1---------------------------------------")

# # Write a Program for computing area and circumference of circle.

PI = 3.14
radius = float(input(' Please Enter the radius of a circle: '))
diameter = 2 * radius
circumference = 2 * PI * radius
area = PI * radius * radius
print(" \nDiameter Of a Circle = %.2f" %diameter)
print(" Circumference Of a Circle = %.2f" %circumference)
print(" Area Of a Circle = %.2f" %area)

print("--------------------------------END-2---------------------------------------")

# Write a Program for note denomination in 2000 , 500 and 100.

notes = (2000,500,200,100,50,20,10,5,2,1)

amount = float(input("Enter Amount to be paid : "))

for C in notes:
    count = amount//C
    print("Note Value : ", C,'\tnumber of notes ',count)
    # amount = amount%C
    
    print("--------------------------------END-3---------------------------------------")

# Write a Program to calculate the simple interest given in all the required values.

principle=float(input("Enter the principle amount:"))
time=int(input("Enter the time(years):"))
rate=float(input("Enter the rate:"))

simple_interest=(principle*time*rate)/100
print("The simple interest is:",simple_interest)

print("--------------------------------END-4---------------------------------------")

# Write a Program to calculate the total and average of 5 subject marks.

  
english = float(input("Please enter English Marks: "))
math = float(input("Please enter Math score: "))
computers = float(input("Please enter Computer Marks: "))
physics = float(input("Please enter Physics Marks: "))
chemistry = float(input("Please enter Chemistry Marks: "))
 
total = english + math + computers + physics + chemistry
average = total / 5
percentage = (total) * 100

 
# print("\nTotal Marks = %.2f"  %total)
# print("Average Marks = %.2f"  %average)
# print("Marks Percentage = %.2f"  %percentage)

print ("total number of subject mark", total)
print ("average number of subject mark", average)
print ("percentage number of subject mark", percentage)

print("--------------------------------END-5---------------------------------------")