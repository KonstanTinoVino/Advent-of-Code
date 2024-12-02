import requests
from collections import Counter

cookie = '' # Add your cookie here

def calculate_total_distance(left_list, right_list):
    # Sort both lists
    left_list.sort()
    right_list.sort()
    
    # Calculate the total distance
    total_distance = 0
    for left, right in zip(left_list, right_list):
        total_distance += abs(left - right)
    
    return total_distance

# Fetch the input data from the URL
url = 'https://adventofcode.com/2024/day/1/input'
headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-encoding': 'gzip, deflate, br, zstd',
    'accept-language': 'en-US,en;q=0.9,bg;q=0.8,es-ES;q=0.7,es;q=0.6,pt;q=0.5',
    'cache-control': 'max-age=0',
    'cookie': f'{cookie}',
    'dnt': '1',
    'priority': 'u=0, i',
    'referer': 'https://adventofcode.com/2024/day/1',
    'sec-ch-ua': '"Google Chrome";v="131", "Chromium";v="131", "Not_A Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
input_data = response.text.strip()
print(input_data)
# Parse the input data into two separate lists
left_list = []
right_list = []
for line in input_data.split('\n'):
    left, right = map(int, line.split())
    left_list.append(left)
    right_list.append(right)

# Calculate the total distance
total_distance = calculate_total_distance(left_list, right_list)
print(f"Total distance: {total_distance}")

def calculate_similarity_score(left_list, right_list):
    # Count the occurrences of each number in the right_list
    right_counter = Counter(right_list)
    
    # Calculate the similarity score
    similarity_score = 0
    for number in left_list:
        similarity_score += number * right_counter[number]
    
    return similarity_score

# Calculate the similarity score
similarity_score = calculate_similarity_score(left_list, right_list)
print(f"Similarity score: {similarity_score}")