store_name = "Stan's Store" #anything inside of double or single quotes is called text, and is called as string
print(store_name) # the quotes are only used to tell Python that anything inside them is a String
# double quotes are useful if a single quote is literally part of the String.
# store_name = 'Stan's Store ' -> this would cause an error because the second single quote would end the String and Python doesn't know what to do with the rest

hello = "Hello" 
name = "Stan" 
my_name = input("What's your name?\n") # use \n - enter the name on the next line - \n is a special character for a new line
greeting = hello + " " + my_name # concatenate two Strings with a +
print(greeting)