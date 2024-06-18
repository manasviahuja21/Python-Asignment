
# Python Assignment 1
# Manasvi
# Enrolment No. 1100102023
# IGDTUW


#1.
num1=0
num2=0
num1=input("Enter num1:")
num2=input("Enter num1:")
print(int(num1)+int(num2))

#2.
num=int(input("Enter number: "))
if(num%2==0):
    print("even")
else:
    print("odd")

#3.
n= int(input("n:"))
fact=1
for i in range(1,n+1):
    fact=fact*i
print(fact)

#4.
name=input("your name")
print("Hi,{}", name)

#5.
user_input = input("Please enter a string: ")
file_name = "output.txt"

with open(file_name, "w") as file:
    file.write(user_input)

print(f"Your input has been written to {file_name}")

#6.
file_name = "output.txt"

with open(file_name, "r") as file:
    content = file.read()

print("File content:")
print(content)


#7.
s=input("Enter string:")
print(len(s))

#8.
s1=input("String1:")
s2=input("string2:")
print("The result is", s1+s2)

#9.
str=input("String:")
sbstr=input("Substring:")

if sbstr in str:
    print("Found")
else:
    print("Not Found")

#10.
str=input("String:")
print(str.upper())


#11.
fstTrm=0
nxtTrm=1
term=1
n= int(input("N:"))
print(fstTrm)
for i in range(0,n-2):
 print(term)
 term=fstTrm+nxtTrm
 fstTrm=nxtTrm
 nxtTrm=term

#12.
num=input("Number:")
sum=0
for x in num:
    sum=sum+int(x)
print(sum)

#13.
num=int(input("Born in the year:"))
print("Age:",2024-num)

#14.
lines=[]
print("Say something")
while(True):
    x=input()
    if(len(x)==0):
      break
    else:
     lines.append(x)

for i in lines:
  print (i)

#15.
import csv

file_name = "data.csv"

with open(file_name, "r") as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(row)


#16.
str=input()
freq={}
for i in str:
    if(i in freq):
        freq[i]=freq[i]+1
    else:
        freq.update({i:1})
print (freq)

#17.
str=input()
print(str.title())

#18.
str1=input()
str2=input()
lst1=list(str1)
lst2=list(str2)
lst1.sort()
lst2.sort()
if(lst1==lst2):
    print("yes")
else:
    print("no")

#19.
stri=input()
str=list(stri)
for i in str:
   if(i.isalpha() and i!=" "):
      str.remove(i)
print(str)

#20.
sum=0
lst=[input() for i in range(0,5)]
for i in lst:
    
    sum=sum+1
print(sum)

#21.
lst=[input() for i in range(0,5)]
x=input()
count=0
for i in lst:
    if(i==x):
        count=count+1
print(count)

#22.
lst=[input() for i in range(0,5)]
max=0
for i in lst:
   if(i>=max):
      max=i
print(max)


#23.
c=int(input("celsius:"))
f=c*1.8 +32
print(f)

#24.

def add(num1, num2):
	return num1 + num2

def subtract(num1, num2):
	return num1 - num2

def multiply(num1, num2):
	return num1 * num2

def divide(num1, num2):
	return num1 / num2

print("Please select operation -\n" \
		"1. Add\n" \
		"2. Subtract\n" \
		"3. Multiply\n" \
		"4. Divide\n")

select = int(input("Select operations form 1, 2, 3, 4 :"))

number_1 = int(input("Enter first number: "))
number_2 = int(input("Enter second number: "))

if select == 1:
	print(number_1, "+", number_2, "=",
					add(number_1, number_2))

elif select == 2:
	print(number_1, "-", number_2, "=",
					subtract(number_1, number_2))

elif select == 3:
	print(number_1, "*", number_2, "=",
					multiply(number_1, number_2))

elif select == 4:
	print(number_1, "/", number_2, "=",
					divide(number_1, number_2))
else:
	print("Invalid input")

#25.
source_file = "source.txt"
destination_file = "destination.txt"

with open(source_file, "r") as src:
    content = src.read()

with open(destination_file, "w") as dest:
    dest.write(content)

print(f"The contents of {source_file} have been copied to {destination_file}")



#26.
p=input("prefix")
s=input("suffix")
if(str[0]==p):
     print("prefix")
if(str[-1]==s):
     print("suffix")


#27.
str=list(input(str))
print(str)











