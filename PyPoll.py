     
     #Add our dependencies
import csv
import os

    ##Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

    ##Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")


    ## 1. intialize total vote counter to 0
total_votes = 0


    #Declare candidate_options list
candidate_options = []

    #Declare candidate_votes dictionary
candidate_votes = {}

winning_candidate = ""

winning_count = 0

winning_percentage = 0

    ##Open the election results and read the file.
with open(file_to_load) as election_data:

        #Read the file object with the reader function.
    file_reader = csv.reader(election_data)



        #Read and print the header row.
    headers = next(file_reader)
    #print(headers)


        #Print each row in the CSV file.
    for row in file_reader:
            #add to the total vote by 1.
        total_votes += 1

            #print each candidate_name from each row 
        candidate_name = row[2]

            ##if the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:

                #appending candidate_options list by adding name of candidates.
            candidate_options.append(candidate_name)

                #Begin tracking the candidates vote count.
            candidate_votes[candidate_name] = 0

            #Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1

    #Determine the percentage of votes of each candidadte by looping through the vote counts
        #Iterate through the list
    for candidate_name in candidate_votes:

            #Retreive vote count of candidate
        votes = candidate_votes[candidate_name]

            #calculate the percentage of votes that candidate got out of the total count
        vote_percentage = float(votes) / float(total_votes) * 100


            ##To do: print out each candidates name, vote count, and percentage of votes in terminal
        print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

            #Determine winning vote count and candidate
            #determine if votes is greater than winning count
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            
                #If true: set winning_count  = votes and winning_percentage = vote_percentage
            winning_count = votes
            winning_percentage = vote_percentage
                #set winning_candidate to candidates_naem
            winning_candidate = candidate_name

    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
print(winning_candidate_summary)

##To do: Print out winning candidate, vote count,and percentage to terminal

        #print(f"{candidate_name} recieved {vote_percentage}% of the total vote.")

    #print candidate_vote dictionary
#print(candidate_votes)

    #3. Print total number of votes 
#print(total_votes)


