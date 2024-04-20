#The function should update the voter’s information or add a vote if not already voted.
def update_voter_info(votersInfo, voter_id, name, voting_district, has_voted):
    #update the voter’s information
    if voter_id in votersInfo:
        votersInfo[voter_id]['name'] = name
        votersInfo[voter_id]['voting_district'] = voting_district

        #Check if the voter has voted
        if not votersInfo[voter_id]['has_voted'] and has_voted:
            votersInfo[voter_id]['has_voted'] = True
            print('Voter ', voter_id, ' has successfully voted')
        else:
            print('Voter ', voter_id, ' has been already voted')

    #add a vote if not already voted.
    else:
        votersInfo[voter_id] = {'name': name,
                                'voting_district': voting_district,
                                'has_voted': True}

        if votersInfo[voter_id]['has_voted'] == True:
            print('New voter ', voter_id, ' has successfully voted')
        else:
            print('New voter ', voter_id, ' has added')

votersInfo = {'01123765': {'name': 'Aza', 'voting_district': 'District A', 'has_voted': False}}

update_voter_info(votersInfo, '01123765' ,'Aza', 'District A', True)
