def nonRepeating(string):
    # Dictionary to Store Counts of each Character in String Input
    counts = {}
    # Array to store the orders of Characters.
    charOrder = []
    # Replacing Empty spaces and converting it to lower case
    string = string.replace(" ", "").lower()
    # Iterating String
    for char in string:
        # If char is already present in Counts dict, increasing the count by 1
        if char in counts:
            counts[char] += 1
        # Else, Keeping the count as '1' for the character & adding it to array
        else:
            counts[char] = 1
            charOrder.append(char)
    # Finally, Iterating the array to check the first charcter whose count is '1'
    for var in charOrder:
        if counts[var] == 1:
            # Returning the first character if it's count is '1'
            return var
    # If there are no repeated characters.
    return "No repeated characters are present !!!"


userInput = input("Enter Your Input String to fetch first non-repeating character :")
print(nonRepeating(userInput))