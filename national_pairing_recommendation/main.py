from config import NATIONS, get_coefficient, read_year_results

YEAR_2021_RESULTS = read_year_results('data/2021.csv')
YEAR_2022_RESULTS = read_year_results('data/2022.csv')

YEAR_2023_RESULTS = []

for i in NATIONS:
    for j in NATIONS:
        year_2023_score = get_coefficient(
            score2021=YEAR_2021_RESULTS[i][j],
            score2022=YEAR_2022_RESULTS[i][j],
        )
        YEAR_2023_RESULTS.append((i, j, year_2023_score))

with open('data/2023.csv', 'wt') as file:
    file.write('\n'.join(
        map(','.join, (
            map(str, row)
            for row in [('consumer_id', 'provider_id', 'score')] + YEAR_2023_RESULTS
        ))
    ))
