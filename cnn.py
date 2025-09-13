import requests  
from bs4 import BeautifulSoup  
import csv  
import time  


url = "https://www.cnn.com"  


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
}

try:
   
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Check if the request was successful
  
    soup = BeautifulSoup(response.content, 'html.parser')
    headlines = soup.find_all('h2')
    
    data = []  
    for headline in headlines:
        text = headline.get_text().strip()  
        data.append([text])  
    
    if data:  
        with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Headline'])  
            writer.writerows(data)  
        print("Data successfully written to output.csv")
    else:
        print("No data found to write.")
    
except requests.exceptions.RequestException as e:
    print(f"Error fetching the page: {e}")
except Exception as e:
    print(f"An error occurred: {e}")


time.sleep(5)  