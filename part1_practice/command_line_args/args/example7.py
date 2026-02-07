import argparse
from datetime import UTC, datetime

parser = argparse.ArgumentParser(
    description="Returns and string containing the name and age of the person."
)
parser.add_argument("-f", "--first", help="first name", type=str, required=False, dest="first_name")
parser.add_argument("-l", "--last", help="last name", type=str, required=True, dest="last_name")
parser.add_argument("--yob", help="year of birth", type=int, required=False, dest="birth_year")

args = parser.parse_args()

print(args)
names = []

if args.first_name:
    names = [args.first_name]
else:
    names = []

names.append(args.last_name)
full_name = " ".join(names)
print(full_name)

current_year = datetime.now(UTC).year
print(type(current_year))
age = current_year - args.birth_year
print(age)
print(f"{full_name} is {age} years old!")
