# Create file paths across operating systems
import os

# Module for reading CSV files
import csv


#get file
election_data = os.path.join( 'Resources', 'election_data.csv')

#Define variables 
totalvotecount = 0
canidatelist = []
Kahn_Vote = 0
Correy_Vote = 0
Li_Vote = 0
OTooley_Vote = 0

# Open csv file
with open(election_data) as csv_file:

    #Skip first row as headers
    csv_reader = csv.reader(csv_file)
    csv_header = next(csv_reader)

    #Dictionary to retrieve values
    csv_dictionary = csv.DictReader(csv_file)

    #Create List 
    
    for row in csv_reader:

        #Advance votecount
        totalvotecount = totalvotecount + 1


#Assign rows of cadidates results using if and elif (elseif) and lists

        if row[2] not in canidatelist:
            canidatelist.append(row[2])
         
        if row[2] == canidatelist[0]:
            Kahn_Vote = Kahn_Vote + 1

        elif row[2] == canidatelist[1]:
            Correy_Vote = Correy_Vote + 1

        elif row[2] == canidatelist[2]:
            Li_Vote = Li_Vote + 1

        elif row[2] == canidatelist[3]:
            OTooley_Vote = OTooley_Vote + 1


#% of votes f”, the number (result) that will be printed will be a floating point type, and the 
#“.2” tells your “print” to print only the first 2 digits after the point.

Kahn = ("%.2f" % (Kahn_Vote/totalvotecount*100))
Li = ("%.2f" % (Li_Vote/totalvotecount*100))
Correy = ("%.2f" % (Correy_Vote/totalvotecount*100))
OTooley = ("%.2f" % (OTooley_Vote/totalvotecount*100))


#Determine winner using if, elif (elseif), else

if max(Kahn_Vote, Correy_Vote, Li_Vote, OTooley_Vote) == Kahn_Vote:
    winner = 'Kahn'

elif max(Kahn_Vote, Correy_Vote, Li_Vote, OTooley_Vote) == Correy_Vote:
    winner = 'Correy'

elif max(Kahn_Vote, Correy_Vote, Li_Vote, OTooley_Vote) == Li_Vote:
    winner = "Li"

else: 
    winner = "O'Tooley"

#Print  answers to terminal

print ("Election Results")
print ("---------------------------")
print (f"Total Votes: {totalvotecount}")
print ("---------------------------")
print(f"Kahn: {Kahn}% {Kahn}")
print(f"Correy: {Correy}% {Correy_Vote}")
print(f"Li: {Li}% {Li_Vote}")
print (f"O'Tooley: {OTooley}% {OTooley_Vote}")
print ("---------------------------")
print (f"Winner: {winner}")
print ("---------------------------")




with open("Analysis/main.txt","w") as file:

    
    file.write("Election Results\n")
    file.write("---------------------------\n")
    file.write("Total Votes: " + str(totalvotecount)+ "\n")
    file.write("---------------------------\n")
    file.write("Kahn: " + str(Kahn) + "% " + str(Kahn_Vote)+ "\n")
    file.write("Correy: " + str(Correy) + "% " + str(Correy_Vote)+ "\n")
    file.write("Li: " + str(Li) + "% " + str(Li_Vote)+ "\n")
    file.write("O'Tooley: " + (OTooley) + "% " + str(OTooley_Vote)+ "\n")
    file.write("---------------------------\n")
    file.write("Winner: " + str(winner)+ "\n")
    file.write("---------------------------\n")


