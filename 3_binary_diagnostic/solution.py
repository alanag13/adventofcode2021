input_file = __file__.split("/")
input_file[-1] = "input.txt"

def to_int(byte_arr):
    byte_str = "".join(byte_arr)
    return int(byte_str, base=2)

def get_most_common_bit_in_pos(byte_array, i):
    
    count = 0
    
    for _byte in byte_array:
        if _byte[i] == "0":
            count -= 1
        else:
            count += 1

    if count == 0:
        return -1

    return 0 if count < 0 else 1

def reduce_byte_arrays(byte_array, idx, tiebreaker):
    if len(byte_array) == 1:
        return byte_array[0]

    to_keep = get_most_common_bit_in_pos(byte_array, idx)

    # for co2, use the least common bit instead of the most common
    if to_keep != -1 and tiebreaker == 0:
        to_keep = 1 if to_keep == 0 else 0

    # if there is an equal number of 0s and 1s, keep the tiebreaker value
    to_keep = to_keep if to_keep != -1 else tiebreaker

    # eliminate bitmaps that don't have the desired bit in this position
    byte_array = list(filter(lambda x: x[idx] == str(to_keep), byte_array))
    return reduce_byte_arrays(byte_array, idx + 1, tiebreaker)    


with open("/".join(input_file)) as f:
    byte_arrays = [entry.strip() for entry in f]

gamma = 0
invert_mask = to_int(["1"] * len(byte_arrays[0]))

for i in range(len(byte_arrays[0])):
    most_common = get_most_common_bit_in_pos(byte_arrays, i)
    gamma <<= 1

    if most_common == 1:
        gamma |= 1

epsilon = gamma ^ invert_mask

oxygen = to_int(reduce_byte_arrays(byte_arrays, 0, 1))
co2 = to_int(reduce_byte_arrays(byte_arrays, 0, 0))

print(f"Part one: {gamma * epsilon}")
print(f"Part two: {oxygen * co2}")