import argparse

""" Calculator
 Add
 Sub
 Multiply
 Divide
"""
# Command Examples
# cal-cli.py --add 1 2
# cal-cli.py --sub 1 2
# cal-cli.py --mul 1 2
# cal-cli.py --div 1 2

parser = argparse.ArgumentParser(description='Calculates math operations')

parser.add_argument("--add", action="extend", nargs="+", type=float)

args = parser.parse_args()
answer = None

if args.add:
    answer = sum(args.add)

# Check if answer is whole number, if so, set answer to integer
if answer % 1 == 0:
    answer = int(answer)
print(answer)
print("DEBUG:",args)