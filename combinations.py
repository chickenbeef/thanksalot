def generate_combinations(word):
    if len(word) == 1:
        return [word, word + '.']

    combinations = []
    rest_combinations = generate_combinations(word[1:])
    for rest in rest_combinations:
        combinations.append(word[0] + rest)
        combinations.append(word[0] + '.' + rest)

    return combinations
