from util import gather_input_data

def count_word_occurrences(grid, word):
    rows = len(grid)
    cols = len(grid[0])
    word_len = len(word)
    directions = [
        (0, 1),  # right
        (1, 0),  # down
        (0, -1), # left
        (-1, 0), # up
        (1, 1),  # down-right
        (1, -1), # down-left
        (-1, 1), # up-right
        (-1, -1) # up-left
    ]
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def search_from(x, y, dx, dy):
        for i in range(word_len):
            nx, ny = x + i * dx, y + i * dy
            if not is_valid(nx, ny) or grid[nx][ny] != word[i]:
                return False
        return True
    
    count = 0
    for x in range(rows):
        for y in range(cols):
            for dx, dy in directions:
                if search_from(x, y, dx, dy):
                    count += 1
    
    return count

def count_xmas_occurrences(grid):
    rows = len(grid)
    cols = len(grid[0])
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def search_xmas(x, y):
        patterns = [
            [(0, 0), (1, -1), (1, 1), (2, -2), (2, 2)],  # M.A.S
            [(0, 0), (1, 1), (1, -1), (2, 2), (2, -2)],  # M.S.A
            [(0, 0), (1, -1), (1, 1), (2, 2), (2, -2)],  # S.A.M
            [(0, 0), (1, 1), (1, -1), (2, -2), (2, 2)]   # S.M.A
        ]
        
        for pattern in patterns:
            if all(is_valid(x + dx, y + dy) and grid[x + dx][y + dy] == 'M' for dx, dy in pattern[:1]) and \
               all(is_valid(x + dx, y + dy) and grid[x + dx][y + dy] == 'A' for dx, dy in pattern[1:2]) and \
               all(is_valid(x + dx, y + dy) and grid[x + dx][y + dy] == 'S' for dx, dy in pattern[2:3]) and \
               all(is_valid(x + dx, y + dy) and grid[x + dx][y + dy] == 'M' for dx, dy in pattern[3:4]) and \
               all(is_valid(x + dx, y + dy) and grid[x + dx][y + dy] == 'S' for dx, dy in pattern[4:]):
                return True
        return False
    
    count = 0
    for x in range(rows):
        for y in range(cols):
            if search_xmas(x, y):
                count += 1
    
    return count

corrupted_memory = gather_input_data("https://adventofcode.com/2024/day/4/input")
grid = corrupted_memory.strip().split('\n')
word = "XMAS"

result = count_word_occurrences(grid, word)
print(f"Number of times '{word}' appears: {result}")

corrupted_memory = gather_input_data("https://adventofcode.com/2024/day/4/input")
grid = corrupted_memory.strip().split('\n')

result = count_xmas_occurrences(grid)
print(f"Number of times 'X-MAS' appears: {result}")