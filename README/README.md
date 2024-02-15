# Protein Sequence Converter: NPY to FASTA

This Python script converts protein sequences stored in a NumPy file (.npy) into the FASTA format (.fasta). It is a convenient tool, particularly useful for bioinformatics applications, and specifically intended for use with the Alphamode Multimer AI model.

## Usage

1. **Prepare Your NumPy File:**
   Place your NumPy file containing protein sequences in the `CONVERTER` folder.

2. **Update Input File Path:**
   Open the `npy-to-fasta.py` script and locate the `convert_to_fasta()` function. Inside this function, update the `input_npy_file` variable to point to your NumPy file. If your file is named differently than `protein_sequences.npy`, make sure to update the file name accordingly.

3. **Run the Script:**
   Simply execute the `npy-to-fasta.py` script. It will automatically convert the protein sequences in your NumPy file to FASTA format and save the output in the same directory.

```bash
python npy-to-fasta.py
