''' Read input from STDIN. Print your output to STDOUT '''
# Use input() to read input from STDIN and use print to write your output to STDOUT

def main():
    N = int(input("Enter the number of range : "))
    lst_num = []
    for i in range(N):
        lst_num.append(input("Enter the range with space. (ex:1 10) : "))

    for i in range(N):
        ran = lst_num[i]
        lower = int(ran.split(" ")[0])
        upper = int(ran.split(" ")[1])
        lst = []
        print("Prime Number Between ", lower, " and ", upper)
        for num in range(lower, upper + 1):
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    print(num)
                    lst.append(num)


main()
