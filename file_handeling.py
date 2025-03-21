#reading a file
file = open("file.txt", "r")
content = file.read()
print(content)
file.close()

#reading a file in binary mode
file = open("file.txt", "rb")
content = file.read()
print(content)
file.close()

#write functions
file = open("file.txt", "w")
file.write("I work at ImpactQA")
file.close()

#appending a line within the file
#Python code to illustrate append() mode
file = open('file.txt', 'a')
file.write("\nThis will add this line") #\n will allow the text to be appended in new line
file.close()

#Closing a file
file = open("file.txt", "r")
file.close()

#using "with" statement
with open("file.txt", "r") as file:
    content = file.read()
    print(content)

#handeling exceptions (try , finally)
try:
    file = open("file.txt", "r")
    content = file.read()
    print(content)
finally:
    file.close()
