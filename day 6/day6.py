with open("day 6/input.txt") as f:
    signal = f.read()
    SIGNAL_LENGTH = 14  # 4 for part 1
    
    start_index = 0
    end_index = SIGNAL_LENGTH
    
    for i in range(len(signal)):
        sub_string = set(signal[start_index:end_index])

        if len(sub_string) == SIGNAL_LENGTH:
            print(end_index)
            break
        
        start_index += 1
        end_index += 1
