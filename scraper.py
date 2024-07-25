import requests
from bs4 import BeautifulSoup

# URL to scrape
url = 'https://resttesttest.com/'

# Fetch the content from the URL
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract data (e.g., all paragraph texts)
    paragraphs = soup.find_all('p')
    for p in paragraphs:
        print("success", p.get_text())
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
