partiesList = [{'abbreviation': 'ASC', 'members': 892},
           {'abbreviation': 'ANC', 'members': 13556},
           {'abbreviation': 'EFF', 'members': 11887}
           ]

filteredParties = [p for p in partiesList if p['members'] >= 1000]

print("The list comprehension: \n", filteredParties)

#Rewrite the list comprehension in question 2.4 into a normal list data structure.

normalFilteredParties = []

for party in partiesList:
    if party['members'] >= 1000:
        normalFilteredParties.append(party)

print('\nThe normal list: \n', normalFilteredParties)
