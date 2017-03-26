def get_data_points_from_line(sheet, row):

    data_points = []

    data_points.append({
        'base': sheet,
        'name': row[1][0],
        'service': 'Amazon',
        'match_score': row[1][1],
        'signal_noise_score': row[1][2]
    })

    data_points.append({
        'base': sheet,
        'name': row[1][0],
        'service': 'Google',
        'match_score': row[1][1 + 2],
        'signal_noise_score': row[1][2 + 2]
    })

    data_points.append({
        'base': sheet,
        'name': row[1][0],
        'service': 'Microsoft',
        'match_score': row[1][1 + 4],
        'signal_noise_score': row[1][2 + 4]
    })

    data_points.append({
        'base': sheet,
        'name': row[1][0],
        'service': 'Clarifai',
        'match_score': row[1][1 + 6],
        'signal_noise_score': row[1][2 + 6]
    })

    data_points.append({
        'base': 'global',
        'name': row[1][0],
        'service': 'Amazon',
        'match_score': row[1][1],
        'signal_noise_score': row[1][2]
    })

    data_points.append({
        'base': 'global',
        'name': row[1][0],
        'service': 'Google',
        'match_score': row[1][1 + 2],
        'signal_noise_score': row[1][2 + 2]
    })

    data_points.append({
        'base': 'global',
        'name': row[1][0],
        'service': 'Microsoft',
        'match_score': row[1][1 + 4],
        'signal_noise_score': row[1][2 + 4]
    })

    data_points.append({
        'base': 'global',
        'name': row[1][0],
        'service': 'Clarifai',
        'match_score': row[1][1 + 6],
        'signal_noise_score': row[1][2 + 6]
    })

    return data_points

