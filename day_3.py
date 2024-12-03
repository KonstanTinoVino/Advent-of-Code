import re
from util import gather_input_data

def extract_and_multiply(memory):
    # Regular expressions to match valid mul(X,Y), do(), and don't() instructions
    mul_pattern = re.compile(r'mul\((\d+),(\d+)\)')
    do_pattern = re.compile(r'do\(\)')
    dont_pattern = re.compile(r"don't\(\)")
    
    total_sum = 0
    enabled = True
    
    pos = 0
    while pos < len(memory):
        # Check for don't() instruction
        dont_match = dont_pattern.match(memory, pos)
        if dont_match:
            enabled = False
            pos = dont_match.end()
            continue
        
        # Check for do() instruction
        do_match = do_pattern.match(memory, pos)
        if do_match:
            enabled = True
            pos = do_match.end()
            continue
        
        # Check for mul(X,Y) instruction
        mul_match = mul_pattern.match(memory, pos)
        if mul_match and enabled:
            x, y = map(int, mul_match.groups())
            total_sum += x * y
            pos = mul_match.end()
        else:
            pos += 1
    
    return total_sum

corrupted_memory = gather_input_data("https://adventofcode.com/2024/day/3/input")
print(corrupted_memory)


result = extract_and_multiply(corrupted_memory)

print(f"Sum of all valid multiplications: {result}")