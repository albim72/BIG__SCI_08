import random

# Definiowanie macierzy wypłat dla "Dylematu więźnia"
payoff_matrix = {
    ('C', 'C'): (3, 3),
    ('C', 'D'): (0, 5),
    ('D', 'C'): (5, 0),
    ('D', 'D'): (1, 1)
}


# Generowanie losowej populacji strategii
def generate_population(size):
    return [''.join(random.choice(['C', 'D']) for _ in range(5)) for _ in range(size)]


# Funkcja oceniająca strategię (fitness function)
def evaluate(strategy, opponent):
    score = 0
    for s, o in zip(strategy, opponent):
        score += payoff_matrix[(s, o)][0]
    return score


# Funkcja krzyżowania (crossover) między dwoma strategiami
def crossover(strategy1, strategy2):
    point = random.randint(1, len(strategy1) - 1)
    return strategy1[:point] + strategy2[point:]


# Funkcja mutacji strategii
def mutate(strategy, mutation_rate=0.1):
    strategy = list(strategy)
    for i in range(len(strategy)):
        if random.random() < mutation_rate:
            strategy[i] = 'C' if strategy[i] == 'D' else 'D'
    return ''.join(strategy)


# Algorytm genetyczny
def genetic_algorithm(population_size, generations):
    population = generate_population(population_size)

    for generation in range(generations):
        # Ocena populacji
        opponents = generate_population(population_size)
        fitness_scores = [(strategy, evaluate(strategy, opponents[i])) for i, strategy in enumerate(population)]

        # Sortowanie według fitness
        fitness_scores.sort(key=lambda x: x[1], reverse=True)

        # Wybór najlepszych strategii do krzyżowania
        top_strategies = [strategy for strategy, score in fitness_scores[:population_size // 2]]

        # Krzyżowanie i mutacja
        new_population = top_strategies[:]
        while len(new_population) < population_size:
            parent1, parent2 = random.sample(top_strategies, 2)
            child = crossover(parent1, parent2)
            child = mutate(child)
            new_population.append(child)

        population = new_population

    # Zwróć najlepszą strategię
    best_strategy = max(population, key=lambda strategy: evaluate(strategy, random.choice(opponents)))
    return best_strategy


# Przykładowe użycie algorytmu
best_strategy = genetic_algorithm(population_size=20, generations=100)
print(f"Najlepsza strategia to: {best_strategy}")
