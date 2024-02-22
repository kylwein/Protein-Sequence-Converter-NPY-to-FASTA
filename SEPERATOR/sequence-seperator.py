import numpy as np
import os
import zipfile

def split_sequences(input_npy_file="protein_sequences.npy", output_dir="output"): #REPLACE FILE NAME
    input_npy_file = os.path.abspath(input_npy_file)  # Get absolute path
    output_dir = os.path.abspath(output_dir)  # Get absolute path

    if not os.path.exists(input_npy_file):
        print(f"Error: File '{input_npy_file}' not found.")
        return

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    protein_sequences = np.load(input_npy_file, allow_pickle=True)

    if isinstance(protein_sequences, np.ndarray):
        protein_sequences = protein_sequences.tolist()
    protein_sequences = [sequence.decode() if isinstance(sequence, bytes) else sequence for sequence in protein_sequences]

    zip_filename = os.path.join(output_dir, "sequences.zip")
    with zipfile.ZipFile(zip_filename, 'w') as zip_file:
        for i, sequence in enumerate(protein_sequences):
            output_filename = f"Sequence_{i+1}.fasta"
            with open(os.path.join(output_dir, output_filename), "w") as fasta_file:
                fasta_file.write(f">Sequence_{i+1}\n")
                fasta_file.write(sequence + "\n")
            zip_file.write(os.path.join(output_dir, output_filename), arcname=output_filename)

    print(f"Conversion to FASTA completed. Sequences saved in {zip_filename}")

if __name__ == "__main__":
    split_sequences()
