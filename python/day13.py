with open("inputs/input13.txt") as f:
    signal_list = []
    
    for line in f.readlines():
        if line != "\n":
            signal_list.append(eval(line.strip("\n")))
            
            
def campare_item(left, right):
    if left < right:
        return True
    if left > right:
        return False
    if left == right:
        return None


def compare_list(left, right):
    l_len = len(left)
    r_len = len(right)
    i = 0
    
    while True:
        if i == l_len and i == r_len:
            return None
        elif i == l_len:
            return True
        elif i == r_len:
            return False
        
        left_item = left[i]
        right_item = right[i]

        if isinstance(left_item, int) and isinstance(right_item, int):
            result = campare_item(left_item, right_item)
        elif isinstance(left_item, int):
            result = compare_list([left_item], right_item)
        elif isinstance(right_item, int):
            result = compare_list(left_item, [right_item])
        else:
            result = compare_list(left_item, right_item)

        if result is not None:
            return result

        i += 1


pair_index = 0
signal_sum = 0

for i in range(0, len(signal_list), 2):
    left_signal = signal_list[i]
    right_signal = signal_list[i + 1]
    pair_index += 1
    
    result = compare_list(left_signal, right_signal)
    if result:
        signal_sum += pair_index 
    
print(signal_sum)

signal_list.append([[2]])
signal_list.append([[6]])


def selection_sort(packets):
    for i in range(0, len(packets) - 1):
        min_index = i

        for j in range(i + 1, len(packets)):
            result = compare_list(signal_list[min_index], signal_list[j])
            if not result:
                min_index = j

        packets[i], packets[min_index] = packets[min_index], packets[i]


selection_sort(signal_list)
decode1 = signal_list.index([[2]]) + 1
decode2 = signal_list.index([[6]]) + 1

print(decode1 * decode2)
