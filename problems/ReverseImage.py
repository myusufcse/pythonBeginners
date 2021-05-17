def invertImage(image):
    temp = []
    for i in range(len(image)):
        temp += [image[i][::-1]]

    return temp[::-1]

def main():
    image_rows = int(input().strip())
    image_columns = int(input().strip())

    image = []

    for _ in range(image_rows):
            image.append(list(map(int, input().rstrip().split())))
    print(image)
    result = invertImage(image)
    print(result)
'''
Sample Input
3
3
1 2 3
4 5 6
7 8 9
'''


main()