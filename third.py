# # # # def greet(name):
# # # #     print(f"hello {name}")

# # # # greet("omar")

# # # def sum(a, b):
# # #     sum = a + b
# # #     return sum

# # # ans = sum(10, 20)
# # # print(f"the answere is : {ans}")

# # def product(a):
# #     product = a * a
# #     return product

# # ans = product(5)
# # print(f"the answere is : {ans}")

# def countdown(n):
#     if n == 0:
#         print("Time's Up")
#     else:
#         print(n)
#         countdown(n - 1)

# countdown(5)


def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1)
    

answer = factorial(5)
print(answer)