pipeline_realisateurs = [
    {
        '$match': {
            'role': 'Director'
        }
    }, {
        '$lookup': {
            'from': 'films', 
            'localField': 'film_id', 
            'foreignField': '_id', 
            'as': 'film'
        }
    }, {
        '$unwind': '$film'
    }, {
        '$group': {
            '_id': '$personne_id', 
            'nom': {
                '$first': '$nom'
            }, 
            'nb_films': {
                '$sum': 1
            }, 
            'note_moyenne': {
                '$avg': '$film.note_moyenne'
            }, 
            'recettes_totales': {
                '$sum': '$film.recettes'
            }, 
            'films': {
                '$push': '$film.titre'
            }
        }
    }, {
        '$match': {
            'nb_films': {
                '$gte': 5
            }
        }
    }, {
        '$sort': {
            'note_moyenne': -1
        }
    }, {
        '$limit': 20
    }, {
        '$out': 'top_realisateurs_compass'
    }
]