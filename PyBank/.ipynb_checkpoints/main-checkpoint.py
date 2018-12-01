# Importing libraries
import csv

# Files used
inputFile = "./budget_data.csv"
outputFile = "./financial_analysis.txt"

# Declare variables
totalMonths = 0
totalRevenue = 0
averageChange = 0
greatestInc = ["", 0]
greatestDec = ["", 9999999999999999999999]

revenue_changes = []

# Read Files
with open(inputFile) as financialAnalysisData:
    reader = csv.DictReader(financialAnalysisData)

    # Loop through all the rows of data we collect
    for row in reader:

        # Calculate the totals
        totalMonths = totalMonths + 1
        totalRevenue = totalRevenue + int(row["Profit/Losses"])
    
    # print output as follows:
    print("")
    print("--------------------------------------------------")
    print("Financial Analysis")
    print("--------------------------------------------------")
    print(f"Total Months: {totalMonths}")
    print(f"Revenue: $ {totalRevenue}")
    #print(f"Average Change: {totalMonths}")
    #print(f"Greatest Increase in Profits: {totalMonths}")
    #print(f"Greatest Decrease in Profits: {totalMonths}")
    print("--------------------------------------------------")
    print("")

        