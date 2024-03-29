'''
name:Youssef Ehab Maher
ID:20210465
'''
import random

def generate_chromosomes(number,length):
    chromosomes=[]
    for i in range(number):
        chromosomes.append("")
        for j in range(length):
            x= random.randint(0,1)
            chromosomes[i]+=str(x)
    return chromosomes
def calculate_fitness(chromosomes):
    fitness=[]
    for i in range(len(chromosomes)):
        fitness.append(0)
        for j in range(len(chromosomes[i])):
            if chromosomes[i][j]=="1":
                fitness[i]+=1
    return fitness
def calculate_probability(fitness):
    sum=0.0
    probability=[]
    for i in fitness:
        sum+=i
    for i in range(len(fitness)):
        probability.append(fitness[i])
        probability[i]/=sum
    return probability
def calculate_cummulative(probaility):
    cummulativ=[]
    cummulativ.append(probaility[0])
    for i in range(1,len(probaility)):
        cummulativ.append(cummulativ[i-1]+probaility[i])
    return cummulativ
def select(chromosome,cummualtive):
    r = random.random()
    for i in range(len(cummualtive)):
        if r<=cummualtive[i]:
            return chromosome[i]
def crossover(parent1, parent2, pcross, crossover_point):
    if random.random() < pcross:
        offspring1 = parent1[:crossover_point] + parent2[crossover_point:]
        offspring2 = parent2[:crossover_point] + parent1[crossover_point:]
    else:
        offspring1 = parent1
        offspring2 = parent2
    return offspring1, offspring2
def mutation(chromosome, pMut):
    mutated_chromosome = ""
    for bit in chromosome:
        if random.random() < pMut:
            if bit=='0':
                mutated_bit='1'
            else:
                mutated_bit='0'
            mutated_chromosome += mutated_bit
        else:
            mutated_chromosome += bit
    return mutated_chromosome
def choose_elite(chromosome,fitness):
    el =[]
    temp=fitness.copy()
    i =temp.index(max(temp))
    el.append(chromosome[i])
    del(temp[i])
    j=temp.index(max(temp))
    el.append(chromosome[j])
    return el
    
runs=int(input("enter number of runs: "))
ch_length = int(input("enter length of chromosome: "))
pcross= float(input("enter pCross: "))
pmut= float(input("enter pmut: "))
generations=100
for j in range(runs):
    print("run ",j+1)
    chromosomes= generate_chromosomes(20,ch_length)
    best_fitness=[]
    avr_fitness=[] 
    for i in range(generations):
        fitnessess= calculate_fitness(chromosomes)
        best_fitness.append(max(fitnessess))
        avr_fitness.append(sum(fitnessess)/len(fitnessess))
        probabilities=calculate_probability(fitnessess)
        cummulative_prob= calculate_cummulative(probabilities)
        new_population=[]
        while len(new_population)<len(chromosomes):
            selection=[]
            selection.append(select(chromosomes,cummulative_prob))
            selection.append(select(chromosomes,cummulative_prob))
            offspring= crossover(selection[0],selection[1],pcross,int(ch_length/2))
            new_population.append(mutation(offspring[0],pmut))
            new_population.append(mutation(offspring[1],pmut))
        new_population=new_population[0:18]
        best=choose_elite(chromosomes,fitnessess)
        new_population.extend(best)
        chromosomes=new_population.copy()
        if i==generations-1:
            print("final population: \n",chromosomes,"\n")
    print("best fitness history: \n",best_fitness,"\n")
    print("avr fitness history: \n",avr_fitness,"\n")
