#PROJECT        : ------  Analyzing the financial records of your company -------
#INPUT/DATA     : ------  CSV file "budget_data.csv"
#WHAT THE ASK?  : ------  Analyse the csv file, and determine the following
#-------------------------------------------------------------------------------------------------
                #   A) The total number of months included in the dataset
                #   B) The total net amount of "Profit/Losses" over the entire period
                #   C) The average change in "Profit/Losses" between months over the entire period
                #   D) The greatest increase in profits (date and amount) over the entire period
                #   E) The greatest decrease in losses (date and amount) over the entire period'''
#-------------------------------------------------------------------------------------------------



#Step 1: Import the necessary functions
import csv 

#Step 2: Declare the necessary variables
uniqueMonthList = [] #To store the unique Month entry
totalNetAmount = 0 #To store the total net profit/loss

#Average change in Profit/Loss = [Amount of last row - Amount of first row] / (Total length - 1)

#In the above formula, we dont consider the full length of column, because for the first row, 
# the change will be null, since no reference to compare

amountList = []
amountLastRow = 0
amountFirstRow = 0
avgChange = 0

#Greatest Increase/Decrease of Profit & Lostt

greatestIncMth = ''
greatestDecMth = ''
greatestIncAmt = 0
greatestDecAmt = 0
prevMonth = ''
prevAmt = 0
#Step 3: Import the csv file
with open("budget_data.csv", "r") as openCSVFile:
    csvReader = csv.reader(openCSVFile,delimiter = ',') #Splitting the row of the csv file data on every ','
    next(csvReader) #Exclude the Header variable
    for eachRow in csvReader: #Iterate the .csv file across each rows and perform the following functions
        totalNetAmount = totalNetAmount + int(eachRow[1]) #Cumulative sum of the amount from the 1st index of the row
        amountList.append(int(eachRow[1])) #Storing the amount of each row in list

        if csvReader.line_num == 2: #this will get the line number
            #Assign the first row as default for all greatest Inc/Dec.
            greatestIncMth = eachRow[0]
            greatestDecMth = eachRow[0]
            greatestIncAmt = eachRow[1]
            greatestDecAmt = eachRow[1]
            #If the iterator is greater than 1, do comapraison with previous store value and do a dynamic check
        else:
            if int(eachRow[1]) - int(prevAmt) > int(greatestIncAmt):
                greatestIncAmt = int(eachRow[1]) - int(prevAmt)
                greatestIncMth = eachRow[0]
            elif int(eachRow[1]) - int(prevAmt) < int(greatestDecAmt) :
                greatestDecAmt = int(eachRow[1]) - int(prevAmt)
                greatestDecMth = eachRow[0]

        #Storing the current Month and Amount in previous month variables for calculation
        prevAmt = eachRow[1] 
        prevMonth = eachRow[0]
        if eachRow[0] not in uniqueMonthList: #Checking if the month are repeated? 
            uniqueMonthList.append(eachRow[0]) #if not, store the first index of the row list in ununiqueMonthListi

#Step 4: Calculate the Average change in Profit/Loss
amountFirstRow = amountList[0]
amountLastRow  = amountList[int(len(amountList) - 1)] #Index starts from 0, so we have to subtract by -1 to get last row

avgChange = (amountLastRow - amountFirstRow) / (len(amountList) - 1)

#Step 6: Print the output in the required format
print("----------------------")
print("Financial Analysis")
print("----------------------")
#   A) The total number of months included in the dataset
print("Total Months : " + str(len(uniqueMonthList)))
print("Total: $" + str(totalNetAmount))
print("Avergae Change : " + str(avgChange))
print("Greatest Increase in Profits: " + str(greatestIncMth) + " ($" + str(greatestIncAmt) + ")")
print("Greatest Decrease in Profits: " + str(greatestDecMth) + " ($" + str(greatestDecAmt) + ")")
print("----------------------")