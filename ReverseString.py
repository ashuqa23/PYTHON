# Take input from user
string = input("Enter a string :")
# Initialize empty string to store reserved string
revstring = ""
#Loop through the string from last to first
for i in range(len(string) - 1, -1, -1):
    revstring += string[i]
# Print the reversed string
print("Reversed string is :", revstring)