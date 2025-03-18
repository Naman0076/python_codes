#1 capitalize()
txt = "hello, My name is Naman."

x = txt.capitalize()

print (x)

#2 casefold()
txt = "Hello, My name is Naman!"

x = txt.casefold()

print(x)

#3 center()
txt = "banana"

x = txt.center(20)

print(x)


#4 count()
txt = "I love apples, banana is my favourite fruit!!!"

x = txt.count("apple")

print(x)

#5 encode()
txt = "My name is Ståle"

x = txt.encode()

print(x)

#6 endswith()
txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)

#7 expandtabs()
txt = "H\te\tl\tl\to"

x =  txt.expandtabs(2)

print(x)

#8 find()
txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)

#9 format()
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))


#10 format_map()
a = {'x':'John', 'y':'Wick'} 
print("{x}'s last name is {y}".format_map(a))


#11 index()
txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)

#12 isalnum()
txt = "Impact QA 1"

x = txt.isalnum()

print(x)

#13 isalpha()
txt = "ImpactQA"

x = txt.isalpha()

print(x)

#14 isascaii()
txt = "Impact QA 123"

x = txt.isascii()

print(x)

#15 isdecimsl()
txt = "1234"

x = txt.isdecimal()

print(x)

#16 isdigi()
txt = "50800"

x = txt.isdigit()

print(x)

#17 isidentifier()
txt = "naman"

x = txt.isidentifier()

print(x)

#18 islower()
txt = "hello world!"

x = txt.islower()

print(x)

#19 isnumeric()
txt = "565543"

x = txt.isnumeric()

print(x)

#20 isprintable()
txt = "565543"

x = txt.isnumeric()

print(x)

#21 isspace()
txt = " "

x = txt.isspace()

print(x)

#22 istitle()
txt = "Hello, My Name Is Naman Kaushik!"

x = txt.istitle()

print(x)

#23 isupper()
txt = "THIS IS NOW!"

x = txt.isupper()

print(x)

#24 join()
myTuple = ("John", "Peter", "Vicky")

x = "#".join(myTuple)

print(x)

#25 ljust()
txt = "banana"

x = txt.ljust(20)

print(x, "is my favorite fruit.")

#26 lower()
txt = "Hello my FRIENDS"

x = txt.lower()

print(x)

#27 upper()
txt = "Hello my FRIENDS"

x = txt.upper()

print(x)

#28 lstrip()
txt = "     banana     "

x = txt.lstrip()

print("of all fruits", x, "is my favorite")

#29 maketrans()
txt = "Hello Naman!"
mytable = str.maketrans("S", "P")
print(txt.translate(mytable))


#30 partition()
txt = "I could eat Fruits all day"

x = txt.partition("Fruits")

print(x)

#31 replace()
txt = "I like bananas"

x = txt.replace("bananas", "apples")

print(x)

#32 rfind()
txt = "Mi casa, su casa."

x = txt.rfind("casa")

print(x)

#33 rindex()
txt = "Mi casa, su casa."

x = txt.rindex("casa")

print(x)

#34 rjust()
txt = "banana"

x = txt.rjust(20)

print(x, "is my favorite fruit.")

#35 rpartition()
txt = "I could eat bananas all day, apples are my favorite fruit"

x = txt.rpartition("bananas")

print(x)

#35 rsplit()
txt = "apple, banana, cherry"

x = txt.rsplit(", ")

print(x)

#36 rstrip()
txt = "     banana     "

x = txt.rstrip()

print("of all fruits", x, "is my favorite")

#37 split()
txt = "welcome to the jungle"

x = txt.split()

print(x)

#38 splitlines()
txt = "Thank you for the music\nWelcome to the jungle"

x = txt.splitlines()

print(x)

#39 startswith()
txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x)

#40 strip()
txt = "     banana     "

x = txt.strip()

print("of all fruits", x, "is my favorite")

#41 swapcase()
txt = "Hello My Name Is PETER"

x = txt.swapcase()

print(x)

#42 title()
txt = "Welcome to my world"

x = txt.title()

print(x)

#43 translate()
mydict = {83:  80}
txt = "Hello Sam!"
print(txt.translate(mydict))

#44 zfill()
txt = "50"

x = txt.zfill(10)

print(x)