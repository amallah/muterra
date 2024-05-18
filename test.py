from datetime import datetime
from copy import copy
import json, sys, random, os, base64, hashlib

origmap = [
       'Q...4..XX.3.CXXCXXX..4..Q',
       'X.X..XXCXXXXXXXXQ.X....XX',
       '.XXXXX...XXXXXXXX.X...XX.',
       'XXXXXX.5.XXXXXXXXXX2..XC5',
       'X1..........CQX......XXXX',
       'X......2......X.3....XXXX',
       'X..C.......C..X.....Q.XX2',
       'X.............X.......XXX',
       'X....XXXX.....X...XXX...X',
       'X...XXCXXX......C.XXX.3..',
       'X...XXX3XX..1.5...XXX..X.',
       'X.....XXXX........6XX..X.',
       'X......XXC....X.......XXX',
       'X.............X.2.....X4C',
       'X..C.......C..X...XXC.XXX',
       'X......3......X.XXXXX..X.',
       'XQ...........4X.XXXX...X.',
       'XXXXXX.5.XXXXXX.XXXXX....',
       '................X.CX.C..Q',
       'X...X......3...........X.',
       '.X...XXXX.XXX..2..XX..6X.',
       '.XC.X..XXXXXXX..X.....XXX',
       '....X.6XX..1XXXXX.4.XXXXX',
       '4..C..XX.XXX..XCX...QX..C']
       
def mutate_agent(agent_genome):
    num_mutations = random.randint(1, 10)
    letters = "NSEW"
    for mutation in range(num_mutations):
      nreplace = random.randint(2, len(agent_genome))
      agent_genome = agent_genome[:(nreplace-1)] + random.choice(letters) + agent_genome[nreplace:]
    return agent_genome  

def compress(solution):
   letters = "NSEW"
   solution = solution.replace('NS','')
   solution = solution.replace('SN','')
   solution = solution.replace('EW','')
   solution = solution.replace('WE','')
   solution = solution+"".join(random.choice(letters) for i in range(len(solution)-1,steps*3))
   return solution

def generate_random_agent():
   offset = random.randint(0,len(startc)-1)
   new_random_agent = startc[offset]
   y = startsxy[offset*2+1]
   x = startsxy[offset*2]

   for i in range(steps*3):
      letters = ""
      if (y>0) and origmap[y-1][x]!="X":
         letters = letters+"N"
      if y<23 and origmap[y+1][x]!="X":
         letters = letters+"S"
      if x>0 and origmap[y][x-1]!="X":
         letters = letters+"W"
      if x<24 and origmap[y][x+1]!="X":
         letters = letters+"E"
      d = random.choice(letters)
      new_random_agent = new_random_agent + d
      if (d=="N"):
         y=y-1
      elif (d=="S"):
         y=y+1
      elif (d=="E"):
         x=x+1
      elif (d=="W"):
         x=x-1

   return new_random_agent
    

def pretty_print(solution):
   x = 0
   y = 0
   score = 0
   pretty = ""
   map = copy(origmap)
   for d in solution:
      if (startc.find(d)>=0):
         y = startsxy[startc.find(d)*2+1]
         x = startsxy[startc.find(d)*2]
         pretty = pretty+"["+str(starts[startc.find(d)])+"] "
         continue
      if (d=="N"):
         y=y-1
      elif (d=="S"):
         y=y+1
      elif (d=="E"):
         x=x+1
      elif (d=="W"):
         x=x-1
      pretty = pretty+d;
      if map[y][x]=="1":
         pretty = pretty+"4"
      if map[y][x]=="2":
         pretty = pretty+"5"
      if map[y][x]=="3":
         pretty = pretty+"6"
      if map[y][x]=="4":
         pretty = pretty+"7"
      if map[y][x]=="5":
         pretty = pretty+"8"
      if map[y][x]=="6":
         pretty = pretty+"9"
      if map[y][x]=="C":
         pretty = pretty+"C"
      if map[y][x]=="Q":
         pretty = pretty+"Q"
      pretty = pretty+"-";
   hasher = hashlib.sha1(pretty)
   print "%s [%s]"%(pretty,base64.urlsafe_b64encode(hasher.digest()[:10]))


def compute_fitness(solution):
   x = 0
   y = 0
   score = 0
   coverage = 0
   map = copy(origmap)
   for d in solution:
      if (startc.find(d)>=0):
         x = startsxy[startc.find(d)*2]
         y = startsxy[startc.find(d)*2+1]
      if (d=="N"):
         y=y-1
      elif (d=="S"):
         y=y+1
      elif (d=="E"):
         x=x+1
      elif (d=="W"):
         x=x-1
      if (x<0) or (x>24) or (y<0) or (y>23) or map[y][x]=="X":
         return 0
      if map[y][x]=="C":
         score = score + 3
         coverage = coverage + 0.01
         map[y]=map[y][:x]+'.'+map[y][(x+1):]
      if map[y][x]=="1":
         score = score + 2.5
         coverage = coverage + 0.01
         map[y]=map[y][:x]+'.'+map[y][(x+1):]
      if map[y][x]=="2":
         score = score + 3.5
         coverage = coverage + 0.01
         map[y]=map[y][:x]+'.'+map[y][(x+1):]
      if map[y][x]=="3":
         score = score + 4.5
         coverage = coverage + 0.01
         map[y]=map[y][:x]+'.'+map[y][(x+1):]
      if map[y][x]=="4":
         score = score + 5.5
         coverage = coverage + 0.01
         map[y]=map[y][:x]+'.'+map[y][(x+1):]
      if map[y][x]=="5":
         score = score + 6.5
         coverage = coverage + 0.01
         map[y]=map[y][:x]+'.'+map[y][(x+1):]
      if map[y][x]=="6":
         score = score + 7.5
         coverage = coverage + 0.01
         map[y]=map[y][:x]+'.'+map[y][(x+1):]
      if map[y][x]=="Q":
         score = score + 10
         coverage = coverage + 0.01
         map[y]=map[y][:x]+'.'+map[y][(x+1):]
   return score+coverage
    
def freeze(d):
    if isinstance(d, dict):
        return frozenset((key, freeze(value)) for key, value in d.items())
    elif isinstance(d, list):
        return tuple(freeze(value) for value in d)
    return d

def unfreeze(d):
    if isinstance(d, frozenset):
        return dict((key, unfreeze(value)) for key, value in d)
    elif isinstance(d, tuple):
        return list(unfreeze(value) for value in d)
    return d

def generate_random_population(pop_size):
   random_population=[]

   for agent in range(pop_size):
      random_population.append(generate_random_agent())

   return random_population
   
def run_genetic_algorithm(generations=50000, population_size=100):
    tic = datetime.now()
    all_route = []
    population_subset_size = int(population_size / 10.)
    
    # Create a random population of `population_size` number of solutions.
    population = generate_random_population(population_size)

    generation = 0
    # For `generations` number of repetitions...
    while generation>=0:
        generation = generation + 1
        # Compute the fitness of the entire current population
        population_fitness = {}

        for agent_genome in population:
            if freeze(agent_genome) in population_fitness:
                continue
            population_fitness[freeze(agent_genome)] = compute_fitness(agent_genome)
            
        new_population = []
        for rank, agent_genome in enumerate(sorted(population_fitness, key=population_fitness.get, reverse=True)[:population_subset_size]):
            if (generation % 1000 == 0 or generation == generations - 1) and rank == 0:
               toc = datetime.now()
               print("Generation %d best: %f | Unique genomes: %d [%0.3f]" % (generation, population_fitness[agent_genome], len(population_fitness), (toc-tic).total_seconds()))
               pretty_print(agent_genome)
               
#                verifydeck(unfreeze(agent_genome))
               tic = datetime.now()
            
            # Create 1 exact copy of each of the top road trips
            new_population.append(unfreeze(agent_genome))
            
            new_population.append(compress(unfreeze(agent_genome)))
            
            for offspring in range(5):
                new_population.append(mutate_agent(unfreeze(agent_genome)))
                
            new_population.append(generate_random_agent()) 
            new_population.append(generate_random_agent()) 

        for i in range(len(population))[::-1]:
            del population[i]

        population = new_population
    return all_route

#24,4 = 55.5 @ 60000
#0,13 = 43.5 @ 60000
#21,23 = 51.5 @ 60000

steps = 20
startc = "A"
starts = [349]
startsxy = [1,10]
result = run_genetic_algorithm()
