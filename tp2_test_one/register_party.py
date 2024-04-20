def register_party (partiesList):
    acceptableNums = 1000
    registered_parties = []

    if partiesList['member_count'] >= acceptableNums:
        registered_parties.append(party)
        print("The ", partiesList['party_name'], " has successfully registered :)")
    else:
        print("The ", partiesList['party_name'], " does not meet the minimum member count '1000' ")

    return registered_parties

lastRegNumber = 10003318

newParty = {'party_name' : 'MK',
            'reg_number': (lastRegNumber + 1),
            'member_count': 5300}

register_party([newParty])
