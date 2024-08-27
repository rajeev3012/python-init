x="World"

# W   o   r   l   d
# 0   1   2   3   4


# Print word
print("\n1. The word: ", x , "\n")


# Slicing: [start:stop:step]
    # Start: start of slicing
    # Stop: slice upto (but not included)
    # Step: jump size


# Print 3rd letter (Indexing)               //World
print("2. 3rd letter: ", x[2])


# Print starting from 3rd letter            //rld
print("3. Start from 3rd letter: ", x[2::])


# Print skipping one letter                 //Wrd
print("4. Skip 1 letter: ", x[::2])


# From 2nd to 4th letter                    //orl
print("5. 2nd to 4th letter: ", x[1:4])


# Reverse Indexing                          //r
print("6. 3rd letter from last: ", x[-3])


# Word Reverse                              //dlroW
print("7. Word Reverse: ", x[::-1])


# Calculate length                          //5
print("8. Word length: ", len(x))

# Uppercase                                 //WORLD
print("9. Capialize: ", x.upper())

# Replace                                   //Hello
print("10. Replace: ", x.replace("World","Hello"))


# Find character using conditional
if("rld" in x):
    print("Yes, present")
else:
    print("No, absent")