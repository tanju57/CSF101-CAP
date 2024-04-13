# Name: Tandin Wangchuk
# Section: 1EE
# Student ID Number: 02230080
###################################
# REFERENCES
# https://www.blackbox.ai/chat/expert-python
# https://codeium.com/?gad_source=1&gclid=Cj0KCQjw2uiwBhCXARIsACMvIU3eQRapp1lvo-9iUwvpIQ848gvlBSP6powWtK0C1CqeggIqyQsQ8d8aAnRGEALw_wcB
# https://chatbotapp.ai/gemini?utm_source=GoogleAds&utm_medium=cpc&utm_campaign={campaign}&utm_id=21124457886&utm_term=161063875816&utm_content=695656046080&gad_source=1&gclid=Cj0KCQjw2uiwBhCXARIsACMvIU1jKgTmSCcW3iKJblgaYnbNyCv6vPC471iY4p4eMlCHqZxQQhJYGtAaAsTcEALw_wcB
###################################
# Solution:
# The total solution score = 49894
####################################
# Function to read the input file and return a list of tuples with the opposition's pick and the outcome
def read_input(input_0_cap1):

    game_data = [] # Initialize a list to store the game data.

 
    with open(input_0_cap1, 'r') as file: # Open the input file and read each line.
        for line in file:
            parts = line.strip().split() # Strip and Split each line into components.
            if len(parts) == 2: # This statement ensure the position of two components.
                game_data.append(tuple(parts)) # It adds the input tuple to the game data lists
    return game_data # Return to initial variable


def calculate_score(games): #  This function calculates the score based on the game data given in input lists from question given
    # A,B,C represents opponent's choice
    # X,Y,Z represents the result of the game i.e X = Lose, Y = Draw and Z = Win
    # The value represents sum of each game played
    result_score = {
        ('A', 'X'): 3 + 0, 
        ('B', 'X'): 1 + 0, 
        ('C', 'X'): 2 + 0,
        ('A', 'Y'): 1 + 3,
        ('B', 'Y'): 2 + 3, 
        ('C', 'Y'): 3 + 3,
        ('A', 'Z'): 2 + 6, 
        ('B', 'Z'): 3 + 6, 
        ('C', 'Z'): 1 + 6
    }
    return sum(result_score.get(game, 0) for game in games) # This will add all the game_outcome

if __name__ == "__main__": # It will execute all the functions
    input_file = "input_0_cap1.txt"
    games_played = read_input(input_file) # Calls the first function i.e def read_input()
    total_points = calculate_score(games_played) # calls the second function
    print(f"The total sum of the points: {total_points}") # Shows the total output result
