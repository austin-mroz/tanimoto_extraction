:author: Austin Mroz

Overview
========
``tanimoto extraction`` is a simple script to extract a subset of molecules using the Tanimoto similarity metric

Set-up and installation
=======================
To run this extraction, follow these steps:
  1. Ensure that all of the relevant packages are installed. This is most easily accomplished using [Anaconda]{https://www.anaconda.com/products/distribution}.
  2. Create a new conda environment by executing 
    
    $ conda create --name tanimoto_extraction
      
    $ conda activate tanimoto_extraction

  4. Install the necessary python packages by executing

    $ conda install -c conda-forge ase pandas numpy
      
    $ conda install -c rdkit rdkit

  5. Clone the repository
      
    $ git clone https://github.com/austin-mroz/tanimoto_extraction/

  6. Run the extraction code by
    
    $ python extract_by_tanimoto.py /path/to/csv/smiles.txt num2extract

    Where ``/path/to/csv/smiles.txt`` is the path to your text file containing the smiles strings
    and ``num2extract`` is the number of molecular systems you want to extract from your bulk dataset
      
    For example, (to run the example script)
      
    $ python extract_by_tanimoto.py example/example_chem_set.csv 23
