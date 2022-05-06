# tanimoto_extraction
Simple extraction of a subset of molecules using Tanimoto similarity metric.

# Set-up
To run this extraction, follow these steps:
  1. Ensure that all of the relevant packages are installed. This is most easily accomplished using [Anaconda]{https://www.anaconda.com/products/distribution}.
  2. Create a new conda environment by executing 
      > <code>conda create --name tanimoto_extraction</code>
      
      > <code>conda activate tanimoto_extraction</code>
  4. Install the necessary python packages by executing
      > <code>conda install -c conda-forge ase pandas numpy</code>
      
      > <code>conda install -c rdkit rdkit</code>
  5. Clone the repository
      > <code>git clone https://github.com/austin-mroz/tanimoto_extraction/ </code>

  6. Run the extraction code by
      > <code>python extract_by_tanimoto.py /path/to/csv/smiles.txt num2extract </code>

      > Where <code>/path/to/csv/smiles.txt</code> is the path to your text file containing the smiles strings
      > and <code>num2extract</code> is the number of molecular systems you want to extract from your bulk dataset
      
      > For example, (to run the example script)
      > <code>python extract_by_tanimoto.py example/example_chem_set.csv 23</code>
