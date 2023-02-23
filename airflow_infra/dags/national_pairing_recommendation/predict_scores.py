from copy import deepcopy


def predict(operational_domain_id: str):
    def make_flat(lst: list) -> list:
        return [i for item in lst for i in ([item] if not isinstance(item, list) else item)]

    def avg(lst: list) -> float:
        lst = [item for item in make_flat(lst) if item is not None]
        if not lst:
            return None
        return sum(lst) / len(lst)

    with open(f'{operational_domain_id}.csv', 'rt') as file:
        rows = [row.split(',') for row in file.read().split('\n')[1:] if row]

    matrix = [[None for j in range(50)] for i in range(50)]

    for consumer_id, provider_id, score in rows:
        matrix[int(consumer_id)][int(provider_id)] = float(score) / 100

    orig = deepcopy(matrix)

    for _ in range(100):
        result = deepcopy(matrix)

        for i in range(50):
            for j in range(50):
                if matrix[i][j] is None:
                    result[i][j] = avg(
                        [int(matrix[i][c] * 10) * [avg(
                            [matrix[r][j] * matrix[r][c] for r in range(50)
                             if matrix[r][j] is not None and matrix[r][c] is not None]
                        )]
                         for c in range(50) if
                         matrix[i][c] is not None]
                    )
                else:
                    result[i][j] = matrix[i][j]

        matrix = deepcopy(result)

    data = []
    for i in range(2, 47):
        for j in range(2, 47):
            if result[i][j] is None:
                continue

            if orig[i][j] is None:
                data.append(f'{i},{j},{operational_domain_id},{80 * result[i][j]}')
            else:
                data.append(f'{i},{j},{operational_domain_id},{100 * result[i][j]}')

    with open(f'{operational_domain_id}.csv', 'wt') as file:
        file.write('\n'.join(data))
