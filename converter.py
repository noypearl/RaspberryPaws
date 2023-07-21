# convert Animal ID to hex data:

# take input from user
animal_id = int(input("Enter the 15 digit animal id: "))

# extract the first 10 digits and the next 38 digits from the combined decimal
last_10_decimal = int(str(animal_id)[:3])
first_38_decimal = int(str(animal_id)[3:])

# convert the decimal numbers to reversed binary
last_10_bits_reversed = bin(last_10_decimal)[2:].zfill(10)[::-1]
first_38_bits_reversed = bin(first_38_decimal)[2:].zfill(38)[::-1]

# concatenate the two binary strings and convert to hexadecimal
binary_num = first_38_bits_reversed + last_10_bits_reversed
hex_num = hex(int(binary_num, 2))[2:].zfill(12)

# add 0001000010 to the end of the 12 digit hex output to get a 22 digit hex output
hex_data = hex_num + "0001000010"

# output the original hexadecimal number
print("Original 22 digits of hex data [FDX-B]: ", hex_data)

