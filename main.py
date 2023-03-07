# Step 0: import required modules for Web Scrapping ( OS module also imported for Creating Directory
import os
import requests
from bs4 import BeautifulSoup

# Step 1: Get the HTML

url = "https://www.ibef.org/economy"

r = requests.get(url)
htmlContent = r.content
# print(type(htmlContent))
# Step 2: parse the HTML

# Creating Object name soup for parsing HTML Data
soup = BeautifulSoup(htmlContent, 'html.parser')
# print(soup.prettify())

# Step 3: HTML Tree Transversal & parsing

# Extracting all URL's from the Website    [Tried this method but was not able to associate this URL's with Names]
'''all_Urls = []
for link in soup.find_all('a'):
    all_Urls.append(link.get('href'))

print(all_Urls)'''

# Extracting all URL's & names
links = soup.find_all('ul', class_='sublinks')
# print(links)
temp_list = str(links)
temp_list = temp_list.split('"')          # This way, I extracted All the URL's
temp_list.pop(0)                          # Filtering Content
temp_list.pop(len(temp_list)-1)           # Filtering Content
temp_list.pop(len(temp_list)-1)           # Filtering Content
# print(temp_list)
for elem in temp_list:                    # Filtering Content
    if elem == 'sublinks':
        temp_list.remove(elem)
for elem in temp_list:                    # Filtering Content
    if elem == '><li><a href=':
        temp_list.remove(elem)

# print(temp_list)

for i in range(len(temp_list)):           # Filtered All the Contents & Sorted Names & Uri's
    if i % 2 != 0:
        # temp_list[i] = temp_list[i][1:(len(temp_list[i])-21)]
        # print(temp_list[i].find('<'))
        temp_list[i] = temp_list[i][1:temp_list[i].find('<')]

print(temp_list)

# Created empty Dict. for Future Use.
url_dict = {}

# Now Associating URLs & Names using Dictionary

# url_dict[temp_list[1]] = temp_list[0]
print(url_dict)
for i in range(0, len(temp_list), 2):
    url_dict[temp_list[i+1]] = temp_list[i]

print(url_dict)

# Creating a directory to Save all the Text files for Parsed Content
try:
    os.mkdir("C:/Parsed_files")
except FileExistsError:
    print("File Already Exists")


# Parsing all url's using requests & bs-4 module & Stroring all the Content files in a folder

for i in url_dict:
    r = requests.get(url_dict[i])
    htmlContent = r.content
    soup = BeautifulSoup(htmlContent, 'html.parser')
    try:
        data = soup.find('section', class_='innerPageContent').text
        file = open(f"C:/Parsed_files/{i}.txt",'w')
        file.write(data)
        file.close()
    # Exception Handling
    except AttributeError:
        print(f"Can't fetch Content for Page= {i}")
    except:
        print("Error Occurred")



