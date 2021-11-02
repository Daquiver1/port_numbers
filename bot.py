url = "https://en.wikipedia.org/wiki/List_of_TCP_and_UDP_port_numbers"
page = requests.get(url)

soup = BeautifulSoup(page.content, "lxml")
#print(soup.prettify())
results = soup.find("table", {"class": "wikitable sortable collapsible"})
rows = results.find_all('tr')
for rows in rows:
    if rows.get_text() in (" ", "Assigned", "Yes") :
        continue
    print(rows.get_text())