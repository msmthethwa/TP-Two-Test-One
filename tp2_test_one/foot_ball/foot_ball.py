#Write a program that will load the “football.csv” dataset into a dataframe called “foot_ball”. 

import pandas as pd

footBall = pd.read_csv("C:/Users/CC/OneDrive/Desktop/dataset - 2020-09-24.csv")

#inspect the dataframe by listing and displaying the last 7 rows of the dataframe using a single python statement.
print("Displaying the last 7 rows of the dataframe.")
print(footBall.tail(7))

#Access and display the "Nationality" and "Club" columns for the first all players.
print('\nDisplaying the "Nationality" and "Club" columns for the first all players.')
print(footBall[["Nationality", "Club"]])

#Access and display the data for the tenth player in the dataset using row index.
print('\nDisplaying the data for the tenth player in the dataset.')
print(footBall.loc[10])

#Access and display the "Goals" and "Appearances" for players with index positions 100 to 110.
print('\nDisplaying the "Goals" and "Appearances" for players with index positions 100 to 110')
print(footBall.loc[100:110, ["Goals", "Appearances"]])

#Add a new column named "Goals per Appearance" that is calculated by dividing "Goals" by "Appearances"; and display the first 5 rows of the updated dataset. 
print('\nDisplaying the first 5 rows of the updated dataset.')

footBall["Goals per Appearance"] = footBall["Goals"] / footBall["Appearances"]
print(footBall.head())

#Select and display a subset of the dataframe containing only the players from "Arsenal" club.
print('\nDisplaying the players from "Arsenal" club')

players = footBall[footBall['Club'] == "Arsenal"]
print(players)

#Perform a filtering operation to display players who have scored more than 5.
print('\nDisplaying players who have scored more than 5.')

highScore = footBall[footBall['Goals'] > 5]
print(highScore)

#Write a command to upgrade the pandas module so that it downloads new dependencies if needed.
pip install --upgrade pandas
















