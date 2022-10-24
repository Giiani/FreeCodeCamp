from matplotlib.cbook import flatten
import numpy as np
import pandas as pd
from pprint import pprint

def calculate(list):
  
  if len(list)<9:
    raise ValueError('List must contain nine numbers.')

  matrix = np.array(list).reshape(3,3)
  
  mean1=np.mean(matrix,axis=0).tolist()
  mean2=np.mean(matrix,axis=1).tolist()
  meanflat=np.mean(matrix.flatten()).tolist()
  
  var1=np.var(matrix,axis=0).tolist()
  var2=np.var(matrix,axis=1).tolist()
  varF=np.var(matrix.flatten()).tolist()
  
  std1=np.std(matrix,axis=0).tolist()
  std2=np.std(matrix,axis=1).tolist()
  stdF=np.std(matrix.flatten()).tolist()
  
  min1=np.min(matrix,axis=0).tolist()
  min2=np.min(matrix,axis=1).tolist()
  minF=np.min(matrix.flatten()).tolist()
  
  max1=np.max(matrix,axis=0).tolist()
  max2=np.max(matrix,axis=1).tolist()
  maxF=np.max(matrix.flatten()).tolist()
  
  sum1=np.sum(matrix,axis=0).tolist()
  sum2=np.sum(matrix,axis=1).tolist()
  sumF=np.sum(matrix.flatten()).tolist()
  
  calculations = {
    'mean':[mean1,mean2,meanflat],
    'variance':[var1,var2,varF],
    'standard deviation':[std1,std2,stdF],
    'max':[max1,max2,maxF],
    'min':[min1,min2,minF],
    'sum':[sum1,sum2,sumF]
  }
    
  return calculations
