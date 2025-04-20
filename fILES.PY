# # with open("sample.txt")as file:
# #     print(file.read(5))
# #     print(file.tell())
# #     print(file.read(5))
# #     print(file.tell())



# # with open("sample.txt", "r")as file:
# #     print(file.read(10))



# # with open("sample.txt", "r")as file:
# #     line = file.readline()
# #     print(line)


# # with open("sample.txt", "r")as file:
# #     print(file.readline())
# #     print(file.readline())
# #     print(file.readline())



# # with open("sample.txt", "r")as file:
# #     lines = file.readlines()
# #     print(lines)    


# with open("sample.txt", "r")as file:
#     for line in file:
#         print(line)


# with open("sample.txt", "r")as file:
#      for line in file.readlines():
#         print(line.strip())






file = open('data.txt', 'r')
print(file.read())
file.close()


file = open('data.txt', 'r')
print("\n Read in parts \n")
print(file.read(8))
file.close()



file = open('data.txt', 'r')
file.write("Hi, I am Omar and i hate maths")
file.close()