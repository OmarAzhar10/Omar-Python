# # # # #ex 1
# # # # age = input("enter your age : ")
# # # # if age >= '18':
# # # #     print("You can vote")
# # # # else:
# # # #     print("you are not 18 years old yet")

# # # #     #ex 2
# # # # num = int(input("enter a num"))
# # # # if num % 2 == 0:
# # # #     print(f"{num} is even number")
# # # # else:
# # # #     print(f"{num} is odd number") 

# # # #     #elif usage
# # # # number = int(input("enter a number"))
# # # # if number > 90 :
# # # #     print("number is greater than 90")
# # # # elif number > 80 :
# # # #     print("number is greater than 80")
# # # # elif number > 70 :
# # # #     print("number is greater than 70")
# # # # else:
# # # #      print("number is smaller than 70")

# # # marks = 75
# # # if marks >=90:
# # #     print("Grade : A") 
# # # elif marks >=75:
# # #     print("Grade : B") 
# # # elif marks >=50:
# # #     print("Grade : C") 
# # # else:
# # #     print("Grade : F") 

# # number = 10
# # if number > 0:
# #     if number % 2 == 0:
# #         print("Positive Even Number")
# #     else:
# #         print("positive odd number")
# # else:
# #     print("not a positive number")

# import datetime
# currentTime = datetime.datetime.now()
# print("Current Date and Time:", currentTime)

# print("Year:", currentTime.year)
# print("Month:", currentTime.month)
# print("Day:", currentTime.day)
# print("Hour:", currentTime.hour)
# print("Minute:", currentTime.minute)
# print("Second:", currentTime.second)
height = float(input("Enter your height in cm: "))
weight = float(input("Enter your weight in kg: "))
 
BMI = weight / (height/100)**2

print("Your BMI is", BMI)

if BMI <= 18.4:
    print("You are underweight")
elif BMI <= 24.9:
    print("You are healthy")
elif BMI <= 29.9:
    print("You are overweight")
elif BMI <= 34.9:
    print("You are fat")
elif BMI <= 39.9:
    print("You are obese")
else: 
    print("You are severely obese")