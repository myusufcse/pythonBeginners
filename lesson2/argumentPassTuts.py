import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("number1", help="first number")
    parser.add_argument("--number2", help="second number")
    parser.add_argument("--operation", help="operation", choices=["add", "sub", "mul"])

    args = parser.parse_args()

    print("number1", args.number1)
    print("number2", args.number2)
    print("operation", args.operation)

    n1 = int(args.number1)
    n2 = int(args.number2)
    Result = None

    if args.operation == "add":
        Result = n1 + n2
    elif args.operation == "sub":
        Result = n1 - n2
    elif args.operation == "mul":
        Result = n1 * n2
    print("Result is", Result)
