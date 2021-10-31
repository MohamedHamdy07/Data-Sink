# Data-Sink
This program pulls data on the 2021 LCS season. It pulls the data from https://www.factor.gg/players and uses selenium, beautiful soup, requests, and sqlite3 in order to scrape the data from the web. The program connects to an sqlite db and outputs the db file LCS_Summer.db. I have included a batch file with all the required plugins you need to run the program. 
The decription of all the columns is as follows:
Name: 
Average_Gold: The average total amount of gold earned per game.
Average_Gold_at_15: The average total amount of gold earned by 15 minutes into the game.
Average_GD_At_15: The average difference in gold between the player and their mirror on the other team.
Average_Assists: The average amount of assists per game. 
Average_Damage_Per_Teamfight: The average damage dealt by the player per teamfight
Average_Deaths: The average amount of deaths per game
Average_Damage_healed: The average amount of healing done per game.
Average_DPM: The average damage per minute dealt by the player.
Average_Worthless_Deaths: The average amount of times a player dies while getting nothing in return.
Average_Kills: The average kills per game.
Average_CS: The average amount of enemy minions killed per game. 
Average_Minutes_Between_deaths: The average amount of time in minutes between player deaths.
Average_minutes_between_kills: The average amount of time in minutes between player kills.
Average_neutral_minion_kills: The average amount of jungle monsters killed per game. 

