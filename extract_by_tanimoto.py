from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem.rdMolDescriptors import GetMorganFingerprint
from rdkit.SimDivFilters.rdSimDivPickers import MaxMinPicker

from utilities import load_smiles_list, tanimoto_sim, gen_rdmols

# load your smiles data
smiles_path = '/path/to/your/list/of/smiles/system_set.csv'
smiles_list = load_smiles_list(smiles_path)

# convert your smiles to rdkit molecule objects
rdmols = gen_rdmols(smiles_list)

# calculate the Morgan fingerprints
fps = [GetMorganFingerprint(x,3) for x in rdmols] # list of fingerprints
nfps = len(fps) # total number of fingerprints

# this is the money line -- this function extracts the top num2extract candidates
num2extract = 23
dmat_ids=tanimoto_sim(fps,num2extract)

# save subset as an image
img = Draw.MolsToGridImage([rdmols[x] for x in dmat_ids],molsPerRow=4)
img.save('subset.png')

# write subset smiles to a file
n = open('subset.txt','w')
for x in dmat_ids:
    n.write(Chem.MolToSmiles(rdmols[x])+'\n')
n.close()

