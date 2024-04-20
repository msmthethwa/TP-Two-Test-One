voters = [{'voter_id': '025155', 'name': 'Asanda', 'voter_district': 'District A', 'registered': True},
          {'voter_id': '824254', 'name': 'Yolihle', 'voter_district': 'District B', 'registered': False},
          {'voter_id': '345674', 'name': 'Sihle', 'voter_district': 'District C', 'registered': True},
          ]

registered_voters = filter(lambda x : x.get('registered', True), voters)

for voter in registered_voters:
    print(voter)
