# Simple script to convert decimals into other number systems.

dec = int(input("Please enter the decimal to convert: "))

print("The decimal for", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")
