# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp


input_file = "./Input/Letters/starting_letter.txt"
input_names = "./Input/Names/invited_names.txt"
output_folder = "./Output/ReadyToSend/"

with open(input_file) as input:
    data = input.read()
    template = data.strip("[]")
    # print(template)

with open(input_names) as names_list:
    names = names_list.readlines()
    # print(names)


for name in names:
    letter = str(template.replace("[name]", name))
    print(letter)
    file = name.strip("\n")
    with open(f"{output_folder}{file}letter.txy", mode="w") as output:
        output.write(letter)
