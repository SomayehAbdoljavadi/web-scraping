import requests
from bs4 import BeautifulSoup as BS

def fetch_exhibitor():
    url = 'https://exhibitors.gitex.com/gitex-global-2023/Exhibitor/fetchExhibitors'
    myobj = {'limit': 180, 'start': 0, 'selected_event_id': 3}

    headers = {
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
    }

    x = requests.post(url, data=myobj, headers=headers, verify=False )
    soup = BS(x.text)
    elem = soup.findAll('div', {'class': 'item_heading'})
    arr = []
    for item in elem:
        ps = item.div.div.find_all('p')
        arr.append([(item.h4.text.strip()),(ps[0].text.strip()),
                    (ps[1].span.text.strip()),
                    (ps[2].span.text.strip())])
    #print(arr)   

    fd = open("result.csv", "w")
    for i in arr:
        try:
            fd.write(i[0]+', ' + i[1] + ', ' + i[2] + ', ' + i[3] + "\n")
        except Exception as exp:
            fd.write(str(i[0].encode("utf-8")) + ', ' + str(i[1].encode("utf-8")) +
                     ', ' + str(i[2].encode("utf-8")) + ', ' + str(i[3].encode("utf-8")) + "\n")
    fd.close()



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    fetch_exhibitor()
# See PyCharm help at https://www.jetbrains.com/help/pycharm/