input_file = __file__.split("/")
input_file[-1] = "input.txt"

with open("/".join(input_file)) as f:
    actions = [entry.strip().split() for entry in f]

curr_aim = curr_depth = curr_horiz = 0

for direction, num in actions:

    if direction in {"up", "down"}:
        aim_change = int(num) if direction == "down" else int(num) * -1
        curr_aim += aim_change
    else:
        curr_horiz += int(num)
        curr_depth += (curr_aim) * int(num)

print(f"Part one: {curr_aim * curr_horiz}")
print(f"Part two: {curr_depth * curr_horiz}")
