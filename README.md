# Election_Analysis

## Overview of Election Audit
### Purpose
- The goal of this analysis was to assist a Colorado board of elections employee, Tom with his audit of the tabulated results for a U.S. Congressional precinct in Colorado using Python coding language, instead of the commonly used Excel program. The idea behind using Python here was to allow our code/ process not only successfully audit and determine the outcome of the Colorado Congressional election, but also be a viable option to be used to audit and analyze other similar elections, or even possibly larger elections with minor adjustments to our code.

- Initially we were asked to report on the four specific data points below that were related to the candidates in the election.
  -  1. Determined the list of candidates that received votes in the election. 
  -  2. The total number of votes cast.
  -  3. Total number of votes cast for each candidate.
  -  4. The percentage of votes for each Candidate out of the total vote count.
  -  5. Determine the winner of the election based on the popular vote. 

- Once the data points above were reported on and determined, we were then tasked with taking our audit further and investigate the data elements below with regards to the county's that voted in the election.
  -  1. Voter Turnout for each county in the election.
  -  2. The percentage of votes from each county out of the total vote count.
  -  3. The county with the highest turnout.

## Election Audit Results
- After a thorough analysis of the election data, see some of the key results listed below. In addition, for reference i have also added the code we applied to the data set to extract that specific result.

    * There were 369,711 total votes cast in this election.  


    * Below is a breakdown of the number of votes for each county and the percentage of total votes for each county in the precinct. The code below the data was used to obtain this information, where ```county_name = row[1]``` was the main variable used to track this data. [(PyPoll_Challenge.py)](https://github.com/Jess-Vannatter/Election_Analysis/blob/main/PyPoll_Challenge.py).
            
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
          ```      
             
    * Denver county had the largest voter turnout. The code referenced below was used to determine the largest county turnout. [(PyPoll_Challenge.py)](https://github.com/Jess-Vannatter/Election_Analysis/blob/main/PyPoll_Challenge.py).
    
         ```
              if (county_vote_count > largest_vote_count):
                largest_county = county_name
                largest_vote_count = county_vote_count
         ```

    * Below is a breakdown of the number of votes for each candidate and the percentage of the total votes each candidate received. The code below the data was used to obtain this information, where ```candidate_name = row[3]``` was the main variable used to track this data. [(PyPoll_Challenge.py)](https://github.com/Jess-Vannatter/Election_Analysis/blob/main/PyPoll_Challenge.py).
            
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
           ```

    * Below is a breakdown of the winning candidate and their percentage of votes. The code referenced below was used to determine the winner of the election. [(PyPoll_Challenge.py)](https://github.com/Jess-Vannatter/Election_Analysis/blob/main/PyPoll_Challenge.py).
        - Winner: Diana DeGette
        - Winning Vote Count: 272,892
        - Winning Percentage: 73.8%
   
        ```
          if (votes > winning_count) and (vote_percentage > winning_percentage):
            winning_count = votes
            winning_candidate = candidate_name
            winning_percentage = vote_percentage
        ```

## Election Audit Summary
- The code script referenced and utilized in the analysis above and that can be seen here [PyPoll_Challenge.py](https://github.com/Jess-Vannatter/Election_Analysis/blob/main/PyPoll_Challenge.py) successfully examined and reported on the tabulated voting data presented to us in the [election_results.csv](https://github.com/Jess-Vannatter/Election_Analysis/tree/main/resources). Please refer to the [election_results.txt](https://github.com/Jess-Vannatter/Election_Analysis/blob/main/analysis/election_results.txt) file to our summary of the election results. But the function of this code script does not end there. Because of the broad capabilities of the python language, this code can be applied to other elections to examine, analyze and determine outcomes that same way it did here. I have listed examples below of how this could be achieved:

  - With the source document for this analysis being [election_results.csv](https://github.com/Jess-Vannatter/Election_Analysis/tree/main/resources), all we would need to do is to replace said source file with another election data set and make some minor adjustments pathways (within the code) to analyze a completely different election. 

  - Depending on the intended information that we would want to extract from the data set for our new analysis, we would just need to change certain variables and data set parameters (column of desired information) to achieve this. 

  - In addition, we would also be able to apply this to a much larger election. IN the instance of applying this code to a state election, again we would need to adjust some of the variables to match the intended variable output. We would be working with a larger data set, but the code should work the same. To add aspects such as voting turnout in all counties within the state, or the winning candidate within each county we could either replace the variable with variables that would represent those outputs or add the variables to new repeating code placed with our original script to get additional analysis outputs (to add to what we already have).



