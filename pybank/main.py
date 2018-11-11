import csv
f = open('budget_data.csv')
csv_f = csv.reader(f)
months=[]
p= []
for row in csv_f:

  print(row)
 
  p.append(row[1])
  months.append(row[0])
  revenue_change=[]
 
for x in range(1,len(p)):
  revenue_change.append(p[x+1]) - p[x]
  revenue_average = sum(revenue_change) / len(revenue_change)
  total_months=len(months)
  greatest_increase = max(revenue_change)
  greatest_decrease = min(revenue_change)

print("total_months:" + str(total_months))
print("total:" + "$" + str(sum(p)))
print("average_change:" + "$" + str(revenue_average))
print("greatest increase in profit:" + str(months[revenue_change.index(max(revenue_change))+1]) + "" + "$" + str(greatest_increase))
print("greatest decrease in profit:" + str(months[revenue_change.index(min(revenue_change))+1]) + "" + "$" + str(greatest_decrease))

file= open("output.txt","w")
file.write("total_months:" + str(total_months)+"\n")
file.write("total:" + "$" + str(sum(p)) + "\n")
file.write("average change:" + "$" + str(revenue_average) + "\n")
file.write("greatest increase in profits:" + str(months[revenue_change.index(max(revenue_change))+1]) + "" + "$" + str(greatest_increase) + "\n")
file.write("greatest decrease in profits:" + str(months[revenue_change.index(min(revenue_change))+1]) + "" + "$" + str(greatest_decrease) + "\n")
file.close()