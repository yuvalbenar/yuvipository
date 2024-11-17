def count_characters(string):
    character_count = {}
    for char in string:
        if char in character_count:
            character_count[char] += 1
        else:
            character_count[char] = 1
    return character_count

# Example usage
input_string = "my oh my"
result = count_characters(input_string)
print(result) 


