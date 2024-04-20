def register_party(partiesList):
    acceptableNum = 1000
    registered_parties = []

    for party in partiesList:
        if party['member_count'] >= acceptableNum:
            registered_parties.append(party)
            print("The ", party['party_name'], " has successfully registered :) ")
        else:
            print("The ", party['party_name'], " does not meet the minimum member count :(")

    return registered_parties

lastRegNumber = 10003318

newParty = {'party_name': 'MK',
            'reg_number': (lastRegNumber + 1),
            'member_count': 5300
            }

register_party([newParty])

