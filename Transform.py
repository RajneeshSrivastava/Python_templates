import numpy as np
import pandas as pd
from matplotlib import pyplot as plt 
#my_df = pd.read_csv('Priortized_genes.txt', sep="\t", header=None)
my_df = pd.read_csv('Priortized_genes.txt', sep="\t", header=None, index_col=0)
#print (my_df.head())
#df=my_df.T
print (my_df.head())