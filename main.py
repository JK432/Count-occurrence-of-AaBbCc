# Write a program that counts the number of times the first three letters of the alphabet (A,a,B,b,C,c) occur in a file. Do not distinguish between the lowercase and uppercase letters 

file = open("file.txt", "r")
data = file.read()
count=0
for i in data:
  
  if(i=="a"or i=="A"or i=="b" or i=="B" or i=="c" or i=="C"):
    count=count+1

print(count)
