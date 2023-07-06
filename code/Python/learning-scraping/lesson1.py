
from bs4 import BeautifulSoup


with open("blank/index.html") as file:
    src = file.read()

soup = BeautifulSoup(src,"lxml")

#title = soup.title
#print(title)
#print(title.text)
#print(title.string)

# .find() .find_all()
"""
page_h1 = soup.find("h1")
print(page_h1)

page_all_h1 = soup.find_all("h1")
print(page_all_h1)

for item in page_all_h1:
    print(item.text)
"""

# User_Name
"""
user_name = soup.find("div", class_ = "user__name")
print(user_name.text.strip())

user_name = soup.find("div", class_ = "user__name").find("span").text
print(user_name)

user_name = soup.find("div", {"class" : "user__name", "id" : "aaa"}).find("span").text
print(user_name)
"""

#Find all spans in user info
"""
find_all_spans_in_user_info = soup.find(class_ = "user__info").find_all("span")

for item in find_all_spans_in_user_info:
    print(item.text)
"""

#social Network
"""
social_links = soup.find("div", class_ = "social__networks").find("ul").find_all("a")

print(social_links)

social_links = soup.find_all("a")
print(social_links)

for item in social_links:
    text_item = item.text
    item_url = item.get("href") # В HREF всегда храняться сслыки 
    print(f"{text_item}: {item_url}")
"""


