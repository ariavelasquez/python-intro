#import your libraries
from bs4 import BeautifulSoup
import requests
import csv

#find the URL you want to scrape
url = "https://report.boonecountymo.org/mrcjava/servlet/RMS01_MP.I00030s"

#tell the server to go get what is at the above URL
response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})

#grabs just the HTML from the response variable above and stores it in 'html'
html = response.content

#organizes the HTML into something less chaotic
soup = BeautifulSoup(html)

#print(soup.prettify()) makes the HTML more readable

#tells the code to pull the table, but it will only pull the first instance, which is not helpful if there's more than 1 table on a page. "attrs" means "attributes," which allows you to be more specific about what you want to pull
table = soup.find("tbody", attrs={"class":"stripe"})

all_data = [] #this has to go outside of the loop so it doesn't get erased when your loops run.

#findAll will always return a list. If it can't find anything, it will return a blank list []
all_rows = table.findAll("tr")

#create a for loop. If you create a for loop within a for loop, the nested loop must exhaust itself before the end of the 
for row in all_rows:
	all_cells = row.findAll("td")
	temporary_list = []
	for cell in all_cells:
		temporary_list.append(cell.text)
	all_data.append(temporary_list)

print(all_data[1])

#OK now you have all of your requested data printed in your console! Congrats, you've scraped a thing. But only the first page of the table, which is a problem for this particular site because the URL doesn't change when you advance pages within the table. (In other words, the URL for Page 1 of the table is the same as the URL for Page 6.) Solving that problem is too advanced for my skills right now.

#print(table.prettify())

outfile = open("inmates.csv","w") #outfile creates a new file, w means write, r means read
writer = csv.writer(outfile)
writer.writerows(all_data)