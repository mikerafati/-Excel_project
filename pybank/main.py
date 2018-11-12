import os
import csv
budget_data = ("Resources", "budget_data.csv")
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter= ",")
    p= []
    months= []
    for rows in csvreader:
        p.append(int(rows[1]))
        months.append(rows[0])
        print(rows)
revenue_change = []
for x in range(1, len(p)):
  revenue_change.append((int(p[x]) - int(p[x-1])))
  revenue_average = sum(revenue_change) / len(revenue_change)
  total_months = len(months)
  greatest_increase = max(revenue_change)
  greatest_decrease = min(revenue_change)
  print("financial analysis")
  print("total months:" + str(total_months))
  print("total:" + "$" + str(sum(p)))
  print("average change:" + "$" + str(revenue_average))
  print("greatest increase in profits:" + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase))
  print("greatest decrease in profits:" + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease))
  file = open("output.txt". "w")
  file.write("financial analysis" + "\n")
  file.write("....." + "\n")
  file.write("total months:" + str(total months) + "\n")
  file.write("average change:" + "$" + str(revenue_average) + "\n")
  file.write("greatest increase in profits:" + str(months[revenue_change.index(max(revenue_change))+1]) + " " + "$" + str(greatest_increase) + "\n")
  file.write("greatest decrease in profits:" + str(months[revenue_change.index(min(revenue_change))+1]) + " " + "$" + str(greatest_decrease) + "\n")
  file.close()  


    

         