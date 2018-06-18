#PROJECT        : ------  Modernizing Vote Counting Process of a Town  -------
#INPUT/DATA     : ------  CSV file "election_data.csv"
#WHAT THE ASK?  : ------  Analyse the csv file, and determine the following
#-------------------------------------------------------------------------------------------------
                #   A) The total number of votes cast
                #   B) A complete list of candidates who received votes
                #   C) The percentage of votes each candidate won
                #   D) The total number of votes each candidate won
                #   E) The winner of the election based on popular vote.
#-------------------------------------------------------------------------------------------------

#Step 1: Import the necessary packages
import csv 
from collections import defaultdict #this package is imported to make use of dictonary and store the result

#Step 2: Declare the necessary variables
result = defaultdict(list) #This declarations creates a default dictionary variables, with list values
totalVotes = 0 #this variable is to calculate the total votes by each candidate
#Declaring the lists to store the candidates & the votes count 
candidateList = []
candidateVotes = []
winnerName = '' #Finding the winner
winningVote = 0 #Storing the winning vote
#Step 3: Open the csv file
with open("election_data.csv", "r") as openCSVFile:
    csvReader = csv.reader(openCSVFile,delimiter = ',')
    next(csvReader) #Don't consider the header

#Step 4: Iterate the csv files rows and store the Candidte as Key, Voter ID (as list appended) as values
    for row in csvReader:
        #Pull the 3rd column (Candidates ID) as key and
        #append first column (Voter ID) as values , in the list format
        #Sample format ---> result = {"Candidate 1", ["ID 1", "ID 2"], "Candidate 2", ["ID 3", "ID 4"]}
        result[row[2]].append(row[0]) 

#Step 5: Iterate the result dictionary to group the values by,
# Candidate ---> Count of Votes ( the length of the list [values], will give the result)
for key, value in result.items() :
    candidateList.append(key)
    candidateVotes.append(len(value))
    totalVotes = totalVotes + len(value) #Logic to sum up the total votes

#Step 6: Print the output in the required format & Storing it in a text file

with open("Output.txt", "w") as text_file:
    print("----------------------")
    text_file.write("---------------------\n")

    print("Election Results")
    text_file.write("Election Results\n")

    print("----------------------")
    text_file.write("---------------------\n")

    for i in range(int(len(candidateList))): #It can be either candidateList or candidateVote, since both should be same
        print(str(candidateList[i]) +  " : " +  "{:.2%}".format(candidateVotes [i]/totalVotes) + " (" + str(candidateVotes [i])  + ")")
        text_file.write(str(candidateList[i]) +  " : " +  "{:.2%}".format(candidateVotes [i]/totalVotes) + " (" + str(candidateVotes [i])  + ")" )
        text_file.write("\n")
    print("----------------------")
    text_file.write("---------------------\n")

#Getting the max index position from candidatesVotes to find the winner names ( the lists were store in same order)
    print("Winner: " + candidateList[candidateVotes.index(max(candidateVotes))])
    text_file.write("Winner: " + candidateList[candidateVotes.index(max(candidateVotes))])
    text_file.write("\n")
    

    print("----------------------")
    text_file.write("---------------------\n")


    