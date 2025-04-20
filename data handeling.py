# # file = open("data.txt", "r")
# # text = file.read()
# # print(text)
# # file.close()

# # file = open("data.txt", "r")
# # file.write("Hello this is changed")
# # file.close()
# # file = open("data.txt", "r")
# # text = file.read()
# # print(text)
# # file.close()


# file = open("data.txt", 'a')
# file.write("\nhello this is changed by append mode")
# file.close()
# file = open("data.txt", 'r')
# text = file.read()
# print(text)


# with open("data.txt", "r"):
#     file.write("hello\n")
#     file.write("Python\n")

# with open("data.txt", "r"):
#     print("reading file content")
#     print(file.read())

# with open("data.txt", "a"):
#     file.write("Adding line\n")


# with open("data.txt", "r"):
#     print("\nupdated file")
#     print(file.read())



file = open("data.txt", "r")
counter = 0

Content = file.read()



coList = Content.split("\n")

for i in coList:
    if i:
        counter +=1

print("this is no. of files")
print(counter)