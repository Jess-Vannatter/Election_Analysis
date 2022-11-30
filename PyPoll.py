    #The data we need to retreive 
    # 1. The total number of votes cast
    # 2. A Complete list of candidates who recieved votes
    # 3. The percentage of voates each candidate won
    # 4. The total number of votes each candidate won
    # 5. The winner of the electiion based on the popular vote

    #print whole election_results file in terminal
# file_variable = open('resources\election_results.csv','r')
# print(file_variable.read())

    #Direct path to open a file
    #Assign  variable for the file to load and the path.
# file_to_load ='resources/election_results.csv'

#     ##open the electionresults and read it 
# with open(file_to_load) as election_data:

# #to do:preform analysis
#     print(election_data)

#     #close file
# #election_data.close()




 
    #Add our dependencies
import csv
import os

    ##Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

    ##Open the election results and read the file.
with open(file_to_load) as election_data:

    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Read and print the header row.
    headers = next(file_reader)
    print(headers)




# # Using the open() function with the "w" mode we will write data to the file.
# open(file_to_save, "w")


# # Use the open statement to open the file as a text file.
# outfile = open(file_to_save, "w")
# # Write some data to the file.
# outfile.write("Hello World")



# # Close the file
# outfile.close()

# # Create a filename variable to a direct or indirect path to the file.
# file_to_save = os.path.join("analysis", "election_analysis.txt")

# # Using the with statement open the file as a text file.
# with open(file_to_save, "w") as txt_file:

#          ##Write some data to the file. Make sure to add comma and space so output has correct spacing.
#     # txt_file.write("Arapahoe, Denver, Jefferson")

#         ##write the three counties but so each county is on a diffrent line 
#     txt_file.write("Counties in the Election\n------------------------\nArapahoe\nDenver\nJefferson")