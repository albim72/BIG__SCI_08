import random

from deap import base
from deap import creator
from deap import tools

creator.create("FitnessMax",base.Fitness,weights=(1.0,))
creator.create("Individual",list,fitness=creator.FitnessMax)

toolbox = base.Toolbox()

toolbox.register("attr_bool",random.randint,0,1)

toolbox.register("individual",tools.initRepeat,creator.Individual,toolbox.attr_bool,100)

toolbox.register("population",tools.initRepeat,list,toolbox.individual)

#funkcja przystosowania
def evalOneMax(individual):
    return sum(individual),

#rejestracja funkcji oceny - wykorzystanie funkcji przystosowania
toolbox.register("evaluate",evalOneMax)

#rejestracja operatora krzyżowania
toolbox.register("mate",tools.cxTwoPoint)

#rejestracja operatora mutacji
toolbox.register("mutate",tools.mutFlipBit,indpb = 0.05)

#operator selekcji
toolbox.register("select",tools.selTournament,tournsize=3)

def main():
    random.seed(64)
    #utworzenie populacji 300 osobników
    pop = toolbox.population(n=300)

    #współczyniki operatorów krzyżowania i mutacji
    CXPB, MUTPB = 0.5, 0.2

    print("Start procesu ewolucji....")

    #ocena pierwszej populacji
    fitnesses = list(map(toolbox.evaluate,pop))
    for ind,fit in zip(pop,fitnesses):
        ind.fitness.values = fit

    print(f"Oceniono {len(pop)} osobników")

    #ekstakcja wszystkich ocen
    fits = [ind.fitness.values[0] for ind in pop]

    #numer generacji
    g = 0

    #rozpoczęcie własciwe procesu ewolucji
    while max(fits)<100 and g<1000:
        g=g+1
        print(f"----- GENERACJA {g} ------")

        #selekcja nowej generacji osobników
        offspring = toolbox.select(pop,len(pop))
        offspring = list(map(toolbox.clone,offspring))

        for child1, child2 in zip(offspring[::2],offspring[1::2]):
            if random.random() < CXPB:
                toolbox.mate(child1,child2)

                del child1.fitness.values
                del child2.fitness.values
        for mutant in offspring:
            if random.random() < MUTPB:
                toolbox.mutate(mutant)
                del mutant.fitness.values

        #ocena generacji potomnej
        invalid_ind = [ind for ind in offspring if not ind.fitness.valid]
        fitnesses = map(toolbox.evaluate,invalid_ind)
        for ind,fit in zip(invalid_ind,fitnesses):
            ind.fitness.values = fit

        print(f"Oceniono {len(invalid_ind)} osobników")
        pop[:] = offspring

        #wszystkie oceny i ich analiza
        fits = [ind.fitness.values[0] for ind in pop]

        length = len(pop)
        mean = sum(fits)/length
        sum2 = sum(x*x for x in fits)
        std = abs(sum2/length-mean**2)**0.5

        print(f"Min: {min(fits)}")
        print(f"Max: {max(fits)}")
        print(f"Średnio: {mean}")
        print(f"średnie odchyl std: {std}")


    print(f"koniec ewolucji - osiągnięto zakładane cele....")
    best_ind = tools.selBest(pop,1)[0]
    print(f"Najleszy osobnik: {best_ind}, {best_ind.fitness.values}")

if __name__ == '__main__':
    main()

