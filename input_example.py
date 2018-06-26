# 6.189 Lecture 1
# replaces raw_input_example.py

name = input("What is your name? ")
city = input("What city do you live in? ")
state = input("What state is that in? ")

print("Hello there! It is so great to meet you,")
# One way to do this is to print(strings on separate lines)
print(name)
print("from")
print(city)
print(state)

# We can also "glue together" pieces of a string by adding commas
#  between them.
print(name, "from", city, state)

# This doesn't work because input returns a string
#age = input("Pardon my rudeness, but how old are you? ")
#print("Wow! You look like you could be", age - (0.15*age), "!!")

age = eval(input("Pardon my rudeness, but how old are you? "))

# Notice that we can "glue together" two strings and one integer into
#  one giant string.
print("Wow! You look like you could be", int(age - (0.15*age)), "!!")

# int(argument) forces the argument to be an integer by rounding down.
# So, int(5.1) = 5 and int(5.9) = 5
