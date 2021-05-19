def count_substring(string, sub_string):
    count = 0
    for i in range(0, len(string)+1):
        if string[0+i:len(sub_string)+i]==sub_string:
            count+=1
    print(count)

count_substring("ABCDCDC", "CDC")