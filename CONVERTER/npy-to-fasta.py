import numpy as np
import os

def convert_to_fasta(input_npy_file=None):
    if input_npy_file is None:
        input_npy_file = "bs_test_protein.npy"

    if not os.path.exists(input_npy_file):
        print(f"Error: File '{input_npy_file}' not found.")
        return

    protein_sequences = np.load(input_npy_file, allow_pickle=True)

    if isinstance(protein_sequences, np.ndarray):
        protein_sequences = protein_sequences.tolist()
    protein_sequences = [sequence.decode() if isinstance(sequence, bytes) else sequence for sequence in protein_sequences]

    output_filename = os.path.splitext(os.path.basename(input_npy_file))[0] + ".fasta"

    with open(output_filename, "w") as fasta_file:
        for i, sequence in enumerate(protein_sequences):
            fasta_file.write(f">Sequence_{i+1}\n")
            fasta_file.write(sequence + "\n")

    print("Conversion to FASTA completed.")

if __name__ == "__main__":
    convert_to_fasta()
