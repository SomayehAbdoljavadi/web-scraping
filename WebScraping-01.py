import requests
from bs4 import BeautifulSoup

# Define the URL of the page you want to scrape
url = "https://www.gitex.com/Speakers2023.aspx"

# Define the headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
}

# Send an HTTP GET request to the URL with headers
response = requests.get(url, headers=headers)

# Check if the request was successful
if response.status_code == 200:
    # Parse the HTML content of the page using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find all the speaker information elements
    #*************class_='speakerboxText'*********************
    speaker_elements = soup.find_all('div', class_='speakerboxText')

    if not speaker_elements:
        print("No speaker information elements found on the page.")
    else:
        # Initialize lists to store the extracted information
        names = []
        positions = []
        companies = []
        countries = []

        # Loop through each speaker element and extract the information
        for speaker in speaker_elements:
            names.append((speaker.find('h3', class_='spname')).text)
            positions.append((speaker.find('p', class_='desg')).text)
            companies.append((speaker.find('span', class_='sppost')).text)
            countries.append((speaker.find('p', class_='countrytxt')).text)


        # Print the extracted information
        for i in range(len(names)):
            print(f"Name: {names[i]}")
            print(f"Position: {positions[i]}")
            print(f"Company: {companies[i]}")
            print(f"Country: {countries[i]}")
            print()

else:
    print("Failed to retrieve the web page.")