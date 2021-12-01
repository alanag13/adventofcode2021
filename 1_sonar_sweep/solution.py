input_file = __file__.split("/")
input_file[-1] = "input.txt"

with open("/".join(input_file)) as f:
    nums = [int(entry.strip()) for entry in f]

curr_sum = 0
part_one = part_two = 0

for i in range(len(nums)):

    prev_sum = curr_sum
    curr_sum += nums[i]

    if i > 0 and nums[i] > nums[i-1]:
        part_one += 1

    if i > 2:
        curr_sum -= nums[i-3]

        if curr_sum > prev_sum:
            part_two += 1

print(f"Part one: {part_one}")
print(f"Part two: {part_two}")