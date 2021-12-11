from bs4 import BeautifulSoup
import requests
import csv

#Making a output dictionary that will be appended with the scraped data of each url and maintaning a count for the same. 

base_url = "https://www.cse.iitk.ac.in/pages/ResearchPublication_"
output = {}
count = 0

for i in range(2):

    url = base_url + str(2005+i) + ".html" 
    year = url[-6:-10:-1]
    year = year[::-1]

    response = requests.get(url)
    data = response.text
    #Parsing the data to desired format for easy extraction of the same.
    soup = BeautifulSoup(data, 'lxml')

    #Targetting the div which contains the required information.
    #info1 = soup.find_all ('div', {'class : funded-projects'})
    info = soup.find_all('i', {'class' : 'fa-li fa fa-square'})
    output[year] = len(info)

for i in range(9):

    url = base_url + str(2008+i) + ".html" 
    year = url[-6:-10:-1]
    year = year[::-1]

    response = requests.get(url)
    data = response.text
    #Parsing the data to desired format for easy extraction of the same.
    soup = BeautifulSoup(data, 'lxml')

    #Targetting the div which contains the required information.
    #info1 = soup.find_all ('div', {'class : funded-projects'})
    info = soup.find_all('i', {'class' : 'fa-li fa fa-square'})
    output[year] = len(info)

file = open("data_research.csv", "w")
writer = csv.writer(file)

for key, value in output.items():
    writer.writerow([key, value])

file.close()