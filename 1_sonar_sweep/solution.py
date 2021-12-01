input_file = __file__.split("/")
input_file[-1] = "input.txt"

with open("/".join(input_file)) as f:
    nums = [int(entry.strip()) for entry in f]

part_one = part_two = 0

for i in range(len(nums)):

    if i > 0 and nums[i] > nums[i-1]:
        part_one += 1

    if i > 2 and nums[i] > nums[i-3]:
        part_two += 1

print(f"Part one: {part_one}")
print(f"Part two: {part_two}")