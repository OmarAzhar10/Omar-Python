# # class Animal():
# #     def __init__(self, name):
# #         self.name = name
# #         print(f"{self.name}'s object is created")

# #     def sound(self):
# #         print(f"{self.name} is now making sound")

# #     def walk(self):
# #         print(f"{self.name} is now walking")

# #     def __del__(self):
# #         print(f"{self.name}'s object has been deleted")

# # dog = Animal("Rocky")
# # dog.sound()
# # dog.walk()

# # cat = Animal("Whiskers")
# # cat.sound()
# # cat.walk()

# # del dog
# # del cat

# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#         print(f"Hello, {self.name}! Your age is {self.age} & your account is created successfully")

#     def greet(self):
#         print(f"Welcome, {self.name}! Have a great day")

#     def __del__(self):
#         print(f"Goodbye, {self.name}. Your account is now being deleted")

# print("Creating a person object...")
# person1 = Person("Omar", 12)

# print("Calling thr greet method...")
# person1.greet()

# print("Deleting the persons object...")
# del person1

class BankAccount:

    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = self.balance
        print(f"Account created for {self.name}with account number{account_number}")

    def deposit(self, amount):
        if amount > 0:
            self.balance +=amount
            print(f"{amount} deposited successfully. Current balance:{self.balance}")
        else:
            print("Invalid deposit amount.")

    