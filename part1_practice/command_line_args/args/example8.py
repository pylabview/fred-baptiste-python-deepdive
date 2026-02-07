import argparse

parser = argparse.ArgumentParser(
    description="""
                                            Printing the list of numbers, and the cubes of another list of numbers
                                 
                                 """
)

parser.add_argument("--sq", help="list of numbers to square", nargs="*", type=float)
parser.add_argument(
    "--cu",
    help="list of numbers to cubes",
    nargs="+",
    type=float,
    required=True,
    dest="cubes",
)

args = parser.parse_args()

if args.sq:
    squares = [x**2 for x in args.sq]
    print(squares)


cubes = [x**3 for x in args.cubes]
print(cubes)
