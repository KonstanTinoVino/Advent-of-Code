from dotenv import load_dotenv
import os
import requests


cookie = os.getenv('COOKIE')

def gather_input_data(input_url: str):
    print(cookie)
    # Fetch the input data from the URL
    url = input_url
    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-encoding': 'gzip, deflate, br, zstd',
        'accept-language': 'en-US,en;q=0.9,bg;q=0.8,es-ES;q=0.7,es;q=0.6,pt;q=0.5',
        'cache-control': 'max-age=0',
        'cookie': f'session={cookie}',
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
    input_data = response.text
    
    return input_data