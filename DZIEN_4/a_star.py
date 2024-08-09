from heapq import heappop, heappush


def heuristic(a, b):
    # Używamy odległości Manhattan jako funkcji heurystycznej
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


def astar(grid, start, goal):
    # Ruchy (góra, dół, lewo, prawo)
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    # Koszt od startu do danego punktu
    g_score = {start: 0}
    # Szacowany całkowity koszt przejścia przez dany punkt do celu
    f_score = {start: heuristic(start, goal)}

    # Kolejka priorytetowa open set (lista węzłów do zbadania)
    open_set = []
    heappush(open_set, (f_score[start], start))

    # Mapa ścieżek (skąd przyszliśmy do danego węzła)
    came_from = {}

    while open_set:
        # Węzeł z najniższym kosztem
        current = heappop(open_set)[1]

        # Sprawdzamy, czy dotarliśmy do celu
        if current == goal:
            # Rekonstruujemy ścieżkę
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        for dx, dy in neighbors:
            neighbor = (current[0] + dx, current[1] + dy)

            # Sprawdzamy, czy sąsiad jest w granicach siatki i czy nie jest przeszkodą
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]) and grid[neighbor[0]][neighbor[1]] == 0:
                # Obliczamy nowy koszt dotarcia do sąsiada
                tentative_g_score = g_score[current] + 1

                if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                    # Aktualizujemy najlepszy znany koszt i ścieżkę
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                    heappush(open_set, (f_score[neighbor], neighbor))

    return None  # Jeśli nie znaleziono ścieżki


# Przykład użycia:
grid = [
    [0, 1, 0, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 0, 0, 0, 0]
]

start = (0, 0)  # Początek (górny lewy róg)
goal = (4, 4)  # Cel (dolny prawy róg)

path = astar(grid, start, goal)
print("Znaleziono ścieżkę:", path)
