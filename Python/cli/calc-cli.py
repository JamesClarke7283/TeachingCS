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

op_lst = ["add", "sub", "mul", "div"]
for op in op_lst:
    parser.add_argument("--" + op, action="extend", nargs="+", type=float)

args = parser.parse_args()
answer = 0

if args.add:
    answer = sum(args.add)
if args.sub:
    subtract_set = args.sub[1::]
    answer = args.sub[0] - sum(subtract_set)
if args.mul:
    prev_num = 0
    for index in range(0, len(args.mul), 2):
        if index >= 1:
            answer += prev_num * args.mul[index]
        prev_num = args.mul[index]

# Check if answer is whole number, if so, set answer to integer
if answer % 1 == 0:
    answer = int(answer)
print(answer)
print("DEBUG:",args)
