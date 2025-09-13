import requests  # For making HTTP requests
from bs4 import BeautifulSoup  # For parsing HTML
import csv  # For writing to CSV files
import time  # For adding delays to avoid overwhelming servers


# Step 1: Define the URL to scrape (use a placeholder; do not use Forbes without permission)
# Example: Replace with a public site like https://example.com (which is safe and boring)
url = "https://www.bbc.com"  # Change this to a permitted URL

# Step 2: Set headers to mimic a browser (helps avoid being blocked as a bot)
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

try:
    # Step 3: Send a GET request to the URL
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Check if the request was successful
    
    # Step 4: Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Step 5: Extract data (example: scrape headline elements; adjust based on the site)
    # This is generic—on a real site, inspect the HTML to find the right tags (e.g., <h2> for titles)
    headlines = soup.find_all('h2')  # Assuming we're scraping h2 elements; change as needed
    
    data = []  # List to store the extracted data
    for headline in headlines:
        text = headline.get_text().strip()  # Get the text from the element
        data.append([text])  # Store as a list of lists for CSV
    
    # Step 6: Write the data to a CSV file
    if data:  # Only write if we have data
        with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Headline'])  # Header row
            writer.writerows(data)  # Write the data rows
        print("Data successfully written to output.csv")
    else:
        print("No data found to write.")
    
except requests.exceptions.RequestException as e:
    print(f"Error fetching the page: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

# Step 7: Be polite—add a delay if you're making multiple requests
time.sleep(5)  # Wait 5 seconds; this is a good practice to avoid rate limiting