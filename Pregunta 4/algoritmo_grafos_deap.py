# -*- coding: utf-8 -*-
"""Algoritmo_grafos_DEAP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1k-cYauSKnEbr0R-qhiyxTKRzqv3JCQCL
"""

import array
import random
import json

import numpy

from deap import algorithms
from deap import base
from deap import creator
from deap import tools
creator.create("FitnessMax",base.Fitness,weights=(1.0,))
creator.create("Individual",array.array,typecode='i',fitness=creator.FitnessMax)
toolbox=base.Toolbox()
toolbox.register("attr_int",random.randint,0,4)
toolbox.register("individual",tools.initRepeat,creator.Individual,toolbox.attr_int,6)
toolbox.register("population",tools.initRepeat,list,toolbox.Individual)
def score(individual):
  s=0
  t=False
  if individual[0]==0:
    s=s+100
  for i in range(len(individual)):
   
    a=individual[len(individual)-i-1]
    if a==0:
      continue
    elif a==4:
      s=s+100
      break
    else:
      break
  for i in range(len(individual)-1):
    a=individual[len(individual)-i-1]
    if a==0 and t==False:

      continue
    elif a==4:
      t=True
      r=mat[individual[i-1]][individual[i]]
      s=s+r
  return s
toolbox.register("evaluate",score)
toolbox.register("mate",tools.cxTwoPoint)
toolbox.register("mutate",tools.mutFlipBit,indpb=0.05)
toolbox.register("select",tools.selTournament,tournsize=3)
def main():
  random.seed(64)
  pop=toolbox.population(n=300)
  hof=tools.HallOfFame(1)
  stats =tools.Statistics(lambda ind:ind.fitness.values)
  stats.register("Avg", numpy.mean)
  stats.register("Std", numpy.std)
  stats.register("Min", numpy.min)
  stats.register("Max", numpy.max)
  algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=100, stats=stats,
                        halloffame=hof, verbose=True)
  return pop,stats,hof
if __name__ == "__main__":
  main()