# Election_Analysis


# PyPoll with Python

## Overview of Election Audit
### Purpose
- The goal of this analysis was to assist a Colorado board of elections employee, Tom with his audit of the tabulated results for a U.S. Congressional precinct in Colorado using Python coding language, instead of the commonly used Excel program. The idea behind using Python here, instead of excel was to allow our code/ process not only successfully audit and determine the outcome of the Colorado Congressional election, but alo be a viable option to be used to audit and analyze other similer elections, or even possibly larger elections with minor adjustments to our code.

- Initially we were asked to report on the four specific data points below that were related to the cadidates in the election.
  -  1. Determined the list of candidates that recieved votes in the election. 
  -  2. The total number of votes cast.
  -  3. Total number of votes cast for each candidate.
  -  4. The percentage of votes for each Cadidate out of the totel vote count.
  -  5. Determine the winner of the election based on the popular vote. 

- Once the the data points above were reported on and determined, we were then taksked with taking our audit further and investigate the data elements below with regards to the county's that voted in the election.
  -  1. Voter Turn out for each county in the election.
  -  2. The percentage of votes from each county out of the total vote count.
  -  3. The county with the highest turnout.

## Election Audit Results
- After a thourogh analysis of the election data, see some of the key results listed below. In addition, for reference i have also added the code we applied to the data set to exctract that specific result.

    * There were 369,711 total votes cast in this election.(PyPoll.py) 


    * Below is a breakdown of the number of votes for each county and the percentage of total votes for each county in the precinct. The code below the data was used to obtqin this information, where ```county_name = row[1]``` was the main variable used to track this data.(PyPoll.py).
        - County Votes:
            * Jefferson: 10.5% (38,855)
            * Denver: 82.8% (306,055)
            * Arapahoe: 6.7% (24,801)   
            ```
                  
              for county_name in county_dict:
                   
                  county_vote_count = county_dict.get(county_name)
                  
                  county_vote_percentage = float(county_vote_count) / float(total_votes) * 100
                  county_vote_results = (
                      f"{county_name}: {county_vote_percentage:.1f}% ({county_vote_count:,})\n")
                   
                  print(county_vote_results)
             
    * Denver county had the largest voter turnout. The code referenced below was used to determine the largest county turnout.(PyPoll.py).
      ```
              if (county_vote_count > largest_vote_count):
                largest_county = county_name
                largest_vote_count = county_vote_count

    * Below is a breakdown of the number of votes for each candidate and the percentage of the total votes each candidate received.The code below the data was used to obtain this information, where ```candidate_name = row[3]``` was the main variable used to track this data. (PyPoll.py).
        - Votes by Candidate:
            * Charles Casper Stockham: 23.0% (85,213)
            * Diana DeGette: 73.8% (272,892)
            * Raymon Anthony Doane: 3.1% (11,606)
            ```
            
              for candidate_name in candidate_votes:
              
                  votes = candidate_votes.get(candidate_name)
        
                  vote_percentage = float(votes) / float(total_votes) * 100
                  candidate_results = (
                      f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

                  print(candidate_results)


    * Below is a breakdown of the winning candidate and their percentage of votes. The code referenced below was used to determine the winner of the election. (PyPoll.py).
        - Winner: Diana DeGette
        - Winning Vote Count: 272,892
        - Winning Percentage: 73.8%
        ```
          if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage


There are three primary voting methods that you and Tom will take into account, mail-in ballots, punch cards, and direct recording electronic, or DRE, counting machines. Mail-in ballots are typically hand counted at the central office. Punch cards are collected and then fed into a machine that tabulates vote totals and sends the results to the central office. Finally, memory cards from DRE counting machines are sent to the central office and read by a computer.

## Election Audit Summary



