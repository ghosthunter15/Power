import argparse

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

def Main():
    parser = argparse.ArgumentParser(description="Find the Fibonacci " \
            "number", prog="FIBN")
    group = parser.add_mutually_exclusive_group()

    group.add_argument("-v", "--verbose", action="store_true", help=\
            "shows more putput")
    group.add_argument("-q", "--quiet", action="store_true", help=\
            "shows less output")
    
    parser.add_argument("num", help="The Fibonacci number you wish to" \
            " calculate.", type=int)
    parser.add_argument("-o", "--output", action="store_true", \
            help="copys output to a file")

    args = parser.parse_args()

    result = fib(args.num)

    if args.verbose:
        print("The "+str(args.num)+"th fib number is "+str(result))
    elif args.quiet:
        print(result)
    else:
        print("fib("+str(args.num)+") = " + str(result))

    if args.output:
        try:
            f = open("fibn.txt", "a")
            f.write(str(result) + "\n")
        except:
            print("ERROR")
            raise

if __name__ == "__main__":
    Main()
