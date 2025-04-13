# class Animal:
#     def make_sound(self):
#         return "some generic animal sound"
    
# class Dog(Animal):
#     def make_sound(self):
#         return "bark"

# class Cat(Animal):
#     def make_sound(self):
#         return "meow"
        


# dog = Dog()
# print(dog.make_sound())   
# cat = Cat()
# print(cat.make_sound())  




# def animal_sound(animal):
#     print(animal.make_sound())


# print("Using animal sound function")
# animal_sound(dog)
# animal_sound(cat)





class Bankaccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def get_balance(self):
        return self.__balance
    
    def deposit(self, amount):
        if amount > 0 :
            self.__balance += amount
            print(f"Deposited: {amount}. New balance:{self.__balance}")
        else:
            print("Invalid amount!")


    def withdraw(self, amount):
            if 0 < amount <= self.__balance :
                self.__balance -= amount
                print(f"Withdrawn: {amount}. Remaining balance:{self.__balance}")
            else:
                print("Insufficient balance or Invalid amount!")

account = Bankaccount("Omar", 5000)

print("Account Owner:", account.owner)

print("Initial balance:", account.get_balance())

account.deposit(2000)
account.withdraw(1000)