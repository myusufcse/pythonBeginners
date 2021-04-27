def letter_changes(your_text):
    i = 0
    str1 = ""
    while i < len(your_text):
        x = your_text[i]
        if x.isalpha():
            str1 = str1 + str(chr(ord(x) + 1))
        else:
            str1 = str1 + x
        i += 1

    return str1


# keep this function call here
print(letter_changes(str(input('Enter Your Name : '))).strip())
