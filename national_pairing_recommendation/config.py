from collections import defaultdict

NATIONS = tuple(range(2, 46 + 1))


def read_year_results(filename: str) -> defaultdict:
    results = defaultdict(lambda: defaultdict(lambda: None))

    with open(filename, 'rt') as file:
        for row in file.read().split('\n')[1:]:
            consumer_id, provider_id, score = row.split(',')

            consumer_id = int(consumer_id)
            provider_id = int(provider_id)
            score = float(score)

            results[consumer_id][provider_id] = score

    return results


def get_coefficient_prev(score2021: float | None) -> float:
    if score2021 is None:
        return 1.0
    return {
        75 <= score2021 <= 100: 0.3,
        50 <= score2021 < 75: 0.5,
        0 <= score2021 < 50: 0.9,
    }.get(True)


def get_coefficient(score2022: float | None, score2021: float | None) -> float:
    if score2022 is None:
        return get_coefficient_prev(score2021)
    return {
        75 <= score2022 <= 100: 0.1,
        50 <= score2022 < 75: 0.3,
        0 <= score2022 < 50: 0.7,
    }.get(True)
