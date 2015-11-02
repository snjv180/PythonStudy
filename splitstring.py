#Problem Statement
#
#In Python a string can be split on a delimiter.
#
#Example
#
#>>> a = "this is a string"
#>>> a = a.split(" ") # a is converted to a list of strings. 
#>>> print a
#['this', 'is', 'a', 'string']
#Joining a string is simple
#
#>>> a = "-".join(a)
#>>> print a
#this-is-a-string 
#Task 
#You are given a string. Split the string on " " (space) delimiter and join using a - hyphen.
#
#Input Format 
#The first line contains a string consisting of words separated by space.
#
#Output Format 
#Print the formatted string as explained above.
#
#Sample Input
#
#this is a string   
#Sample Output
#
#this-is-a-string

a = input()
a = "-".join(a.split())
print(a)