with open("inputs/input6.txt") as f:
    signal = f.read()
    SIGNAL_LENGTH = 14  # 4 for part 1
    
    end_index = SIGNAL_LENGTH
    
    for i in range(len(signal)):
        sub_string = set(signal[i:end_index])

        if len(sub_string) == SIGNAL_LENGTH:
            print(end_index)
            break
        
        end_index += 1