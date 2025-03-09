age = int(input("How old are you ?\n")) #ask the user for input and save the input to a variable
decades = age // 10 # calculate decades and years
years = age % 10
print("You are " + str(decades) 
      + " decades and " + str(years) + " years old.") # convert these numbers to text
