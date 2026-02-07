import argparse

parser = argparse.ArgumentParser(description="testing defaults and flags")


parser.add_argument("--monty", action="store_const", const="Python", default="python")
parser.add_argument("-v", "--verbose", action="store_true", default=False)

args = parser.parse_args()

print(args)
