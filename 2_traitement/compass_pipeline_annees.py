pipeline_annees = [
    {
        '$match': {
            'budget': {
                '$ne': None
            }, 
            'recettes': {
                '$ne': None
            }
        }
    }, {
        '$set': {
            'rentabilite': {
                '$divide': [
                    '$recettes', '$budget'
                ]
            }
        }
    }, {
        '$group': {
            '_id': '$annee', 
            'nb_films': {
                '$sum': 1
            }, 
            'budget_moyen': {
                '$avg': '$budget'
            }, 
            'recettes_moyennes': {
                '$avg': '$recettes'
            }, 
            'rentabilite_mediane': {
                '$median': {
                    'input': '$rentabilite', 
                    'method': 'approximate'
                }
            }
        }
    }, {
        '$sort': {
            '_id': 1
        }
    }, {
        '$out': 'stats_annees_compass'
    }
]