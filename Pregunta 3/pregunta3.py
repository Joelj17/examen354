import random
import numpy as np
from random import sample
res=[0,2,4,0,0,0]
mat=np.zeros((5,5),int)
ar=[7,9,8,20,10,4,11,11,5,17]
ve=[0,1,2,3,4,5]
c=0
for i in range(5):
  for j in range(i+1,5):
   
    mat[i][j]=mat[j][i]=ar[c]
    c=c+1
print(mat)

def generar_poblacion(poblacion,n_pob):
  for j in range(n_pob):
    a=[np.random.randint(0,5)  for i in range(6)]
    
    poblacion.append(a)
  return poblacion
def llega_meta(ind):

  
  for i in range(len(ind)):
    a=ind[len(ind)-i-1]
    if a==0:
      continue
    elif a==4:
      return True
    else:
      return False
def empieza_cero(ind):
  if ind[0]==0:
    return True
  else:
    return False

def calcular_peso(ind,mat):
  s=0
  meta=False
  if llega_meta(ind):
    for i in range(len(ind)-1,0,-1):
      
      if ind[i]==4 and meta==False:
        meta=True
      if meta:
        s=s+mat[ind[i-1],ind[i]]
      else:
        continue
  return s


def puntaje(individuo,mat):
  p=0
  for i in range(len(individuo)):
    if llega_meta(individuo):
      p=p+100
    if empieza_cero(individuo):
      p=p+100
    p=p+(100-calcular_peso(individuo,mat))
    
  return p

def seleccion(poblacion,n_sel,mat):
  pos=[(puntaje(i,mat),i) for i in poblacion]
  pos=[i[1] for i in sorted(pos)]
  return pos[len(pos)-n_sel:]





def reproduccion(poblacion,selec):
  p=0
  padres=[]
  t=len(poblacion[0])
  for i in range(len(poblacion)):
    p=np.random.randint(1,t-1)
    padres=random.sample(selec,2)
    poblacion[i][:p] = padres[0][:p]
    poblacion[i][p:] = padres[1][p:]
  return poblacion

def mutacion( poblacion,res):
    
    for i in range(len(poblacion)):
        if random.random() <= 0.3:
            p = np.random.randint(len(res))
            new_value = np.random.randint(0, 4)

            while new_value == poblacion[i][p]:
                new_value = np.random.randint(0, 4)
            
            poblacion[i][p] = new_value
        return poblacion
def iniciar(res,mat):
  poblacion=[]
  poblacion=generar_poblacion(poblacion,100)
  for i in range(100):
    #print("generacion",i)
    #print(poblacion)
    selc=seleccion(poblacion,10,mat)
    poblacion=reproduccion(poblacion,selc)
    poblacion=mutacion(poblacion,res)
  
  return poblacion
a=iniciar(res,mat)
print("Poblacion Final")
print(a)


