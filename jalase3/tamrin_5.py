
def fibonacci_sequence(m): 
    sequence = [0, 1] 
    for _ in range(2, m): 
        sequence.append(sequence[-1] + sequence[-2]) 
    return sequence[:m] 
m = int(input("tedad adad donbale fibonacci: ")) 
print(fibonacci_sequence(m))