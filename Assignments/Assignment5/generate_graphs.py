import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Plotting scatter plot for number of firms and offers given

num_firms = [219, 238, 252, 217]
num_offers = [762, 990, 1080, 834]

annotate = ["2017", "2018", "2019", "2020"]
c = ['#55ff33', '#f46d43', '#f73545', '#ff58fd']

plt.xlim(210, 260)
plt.ylim(700, 1100)

for i in range(4):
    plt.scatter(num_firms[i], num_offers[i], color=c[i], label = annotate[i])

for i in range(4):
    plt.annotate("(" + str(num_firms[i]) + "," + str(num_offers[i]) + ")", (num_firms[i], num_offers[i]))

plt.title("Scatter Plot")
plt.xlabel("Number of firms")
plt.ylabel("Number of offers given")
plt.legend()
plt.savefig('image_files/scatter.png')
plt.show()

# Stacked bar graph for showing placed and not-placed

years = ["2017", "2018", "2019", "2020"]
placed = [782, 845, 935, 721]
registered = [1015, 1053, 1174, 1152]
not_placed = []

for i in range(4):
    not_placed.append(registered[i] - placed[i])

index = np.arange(4)
width = 0.40

plt.ylim(0, 1500)

plt.bar(index, placed, width, color = "green", label = "Placed")
plt.bar(index, not_placed, width, color = "orange", label = "Not Placed", bottom = placed)

plt.title("Stacked Bar Graph")
plt.xlabel("Year")
plt.ylabel("Number of registered")
plt.xticks(index, years)

leg = plt.legend(loc='upper right')
plt.savefig("image_files/stacked.png")
plt.show()

# Grouped bar graphs for showing % placed from different programmes

years = ["2018", "2019", "2020"]
ug_placed = [83, 85, 76.9]
pg_placed = [78, 75, 50.6]
dual_placed = [97, 93, 77.5]

index = np.arange(3)
width = 0.20

plt.ylim(0,140)

rects1 = plt.bar(index, ug_placed, width, color = "green", label = "UG Placed")
rects2 = plt.bar(index-width, pg_placed, width, color = "orange", label = "PG Placed")
rects3 = plt.bar(index+width, dual_placed, width, color = 'blue', label = "Dual Degree Placed")

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        plt.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 2),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
plt.title("Grouped Bar Graph")
plt.xlabel("Year")
plt.ylabel("Percentage placed")
plt.xticks(index, years)

leg = plt.legend(loc='upper right')
plt.savefig("image_files/Group.png")
plt.show()

# Pie Chart for showing the placements in various sectors

fields = ["Analytics (33%)", "IT/Consulting (30%)", "Marketing (26%)", "Finance (9%)", "Operation (2%)"]
share = [33, 30, 26, 9, 2]

patches, texts = plt.pie(share, labels=fields, shadow=True, startangle = 45)
plt.axis('equal')
plt.title("Pie Chart", y = -0.1)
plt.savefig("image_files/pie.png")
plt.show()

# Bar Graph for number of professors in various domains (CSE IITK)

areas = ["Algorithm and Data Structures", "Computational Biology", "Computer Architecture and OS", "Cyber-physical Systems", "Cyber Security", "Databases, Big Data", "Formal Methods", "Hardware Security", "High Peformance Computing", "Machine Leaning", "Programming Languages and Compilers", "Software Architecture", "Systems Security", "Theoretical CS"]
num_profs = [4, 1, 4, 2, 3, 2, 2, 1, 2, 8, 3, 1, 3, 9]

map = {}
for i,a in enumerate(areas):
    map[a] = num_profs[i] 

sorted_values = sorted(map.values(), reverse=True) # Sort the values
sorted_dict = {}
done = []
rects = []

def autolabel(rects):
    """Attach a text label above each bar in *rects*, displaying its height."""
    for rect in rects:
        height = rect.get_height()
        plt.annotate('{}'.format(height),
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 1),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')

for i in sorted_values:
    for k in map.keys():
        if map[k] == i and k not in done:
            done.append(k)
            sorted_dict[k] = map[k]
            break

for key in sorted_dict.keys():
    rects.append(plt.bar(key, sorted_dict[key], color = 'green'))

for rect in rects:
    autolabel(rect)

plt.xticks(rotation=90)
plt.yticks(rotation=90)
plt.ylim(0,10)
plt.ylabel("Number of profs")
plt.title("Bar Graph")
plt.savefig("image_files/bar.png", bbox_inches = 'tight')
plt.show()

# Generate line graph of number of publications in conferences/journals done by department

df = pd.read_csv('data_journals.csv', header=None, names=['year', 'num_pub'])

years = df['year']
numbers = df['num_pub']

plt.plot(years[:5], numbers[:5], 'bo-')
plt.plot(years[4:7], numbers[4:7], 'bo--')
plt.plot(years[6:], numbers[6:], 'bo-')
plt.title("Line Graph")
plt.xlabel("Year")
plt.ylabel("Number of publications in journals/conferences")
plt.xticks(range(2001, 2021), rotation=90)
plt.savefig("image_files/line1.png", bbox_inches = 'tight')
plt.show()

# Generate line graph of number of research publications done by department

df = pd.read_csv('data_research.csv', header=None, names=['year', 'num_pub'])

years = df['year']
numbers = df['num_pub']

plt.plot(years[0:2], numbers[0:2], 'ro-')
plt.plot(years[1:3], numbers[1:3], 'ro--')
plt.plot(years[2:], numbers[2:], 'ro-')
plt.title("Line Graph")
plt.ylim(5,50)
plt.xlabel("Year")
plt.ylabel("Number of research publications")
plt.xticks(range(2004, 2017), rotation=90)
plt.savefig("image_files/line2.png", bbox_inches = 'tight')
plt.show()
