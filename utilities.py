"""
This module defines general-purpose objects, functions and classes.
"""

# import the necessary packages
import pandas as pd
from ase.atoms import Atoms
from rdkit import DataStructs
from rdkit import Chem
from rdkit.Chem import AllChem, Draw
from tqdm import tqdm
from rdkit import SimDivFilters
import numpy

def load_smiles_list(filename):
    smiles = pd.read_csv(filename, header=None)
    return smiles # smiles.T
    
def gen_rdmols(smiles_list):
    rdmols = []
    for index, row in smiles_list.iterrows():
        rdmol = Chem.MolFromSmiles(row[0].replace("'",""))
        rdmols.append(rdmol)
    return rdmols

def tanimoto_sim(fps,ntopick):
    ds=[]
    for i in range(1,len(fps)):
         ds.extend(DataStructs.BulkTanimotoSimilarity(fps[i],fps[:i],returnDistance=True))
    mmp =SimDivFilters.MaxMinPicker()
    ids=mmp.Pick(numpy.array(ds),len(fps),ntopick)
    return ids
