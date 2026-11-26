# Pipeline "analyse des genres" construit dans MongoDB Compass
# puis exporté en Python (Aggregations > Export Code).
# Collection source : films — Résultat : stats_genres_compass




pipeline =[
    {
        '$unwind': '$genres'
    }, {
        '$group': {
            '_id': '$genres', 
            'nb_films': {
                '$sum': 1
            }, 
            'note_moyenne': {
                '$avg': '$note_moyenne'
            }, 
            'budget_moyen': {
                '$avg': '$budget'
            }, 
            'recettes_moyennes': {
                '$avg': '$recettes'
            }
        }
    }, {
        '$sort': {
            'nb_films': -1
        }
    }, {
        '$out': 'stats_genres_compass'
    }
]