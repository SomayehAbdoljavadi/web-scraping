# Import necessary libraries
import requests
from bs4 import BeautifulSoup 

# Function to get search keywords from user input
def get_search_Kye_words():
    # Initialize an empty list to store the input strings
    input_strings = []
    print("Enter Keywords To Search (***press Enter with an empty line to exit***):")

    while True:
        user_input = input()

        # Check if the user input is an empty line
        if not user_input.strip():
            print("Exiting input.")
            break
   
        input_strings.append(user_input)
    return input_strings            

# Function to extract text from a list of BeautifulSoup elements
def fetch_exhibitor_kye_words(Kye_words): 
    Kye_words_list=[]
    for item in Kye_words:
        Kye_words_list.append(item.text.strip())
    return Kye_words_list

# Function to find keywords in a list of target keywords
def finde_kye_word(target_Kye_words, search_Kye_words):
    for target_Kye_word in target_Kye_words:
        for search_string in search_Kye_words:
            if search_string in target_Kye_word:
                return True
    return False

# Function to fetch exhibitor information
def fetch_exhibitor():
    # Get user-defined search keywords
    search_Kye_words = get_search_Kye_words()
    
    # Define the URL for the web scraping
    url = 'https://exhibitors.gitex.com/gitex-global-2023/Exhibitor/fetchExhibitors'
    myobj = {'limit': 300, 'start': 0, 'selected_event_id': 3}

    headers = {
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    }
    
    # Send a POST request to the URL
    response = requests.post(url, data=myobj, headers=headers, verify=False)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract exhibitor information
    exhibitor_list = soup.findAll('div', {'class': 'item_heading'})
    exhibitor_information_list = []
    
    for item in exhibitor_list:
        ps = item.div.div.find_all('p')
        Kye_words = item.find_all('li')

        Kye_words_list = fetch_exhibitor_kye_words(Kye_words)
        
        if (finde_kye_word(Kye_words_list, search_Kye_words)):
            exhibitor_information_list.append([
                (item.h4.text.strip()), (ps[0].text.strip()),
                (ps[1].span.text.strip()), (ps[2].span.text.strip()),
                Kye_words_list
            ])

    print(len(exhibitor_information_list))
    return exhibitor_information_list

# Function to write exhibitor information to a CSV file
def excel_exhibitor(exhibitor_information_list): 
    fd = open("result.csv", "w")
    
    for exhibitor_information in exhibitor_information_list:
        try:
            fd.write(exhibitor_information[0] + ', ' + exhibitor_information[1] + ', ' + exhibitor_information[2] + ', ' + exhibitor_information[3] + "\n")
        except Exception as exp:
            fd.write(
                str(exhibitor_information[0].encode("utf-8")) + ', ' +
                str(exhibitor_information[1].encode("utf-8")) + ', ' +
                str(exhibitor_information[2].encode("utf-8")) + ', ' +
                str(exhibitor_information[3].encode("utf-8")) + "\n"
            )
    
    fd.close()

# Fetch exhibitor information
exhibitor_information_list = fetch_exhibitor()

# Write exhibitor information to a CSV file
excel_exhibitor(exhibitor_information_list)
