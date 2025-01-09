import argparse
import re
from Bio import SeqIO

# Function to find the longest duplicated subsequence
def find_longest_duplicate(sequence):
    n = len(sequence)
    longest_dup = ""

    for length in range(1, n):
        seen = set()
        for i in range(n - length + 1):
            subseq = sequence[i:i + length]
            if subseq in seen:
                longest_dup = subseq
            seen.add(subseq)

    return longest_dup

# Function to calculate GC content
def calculate_gc_content(sequence):
    g_count = sequence.count('G')
    c_count = sequence.count('C')
    gc_content = (g_count + c_count) / len(sequence) * 100
    return gc_content

def main():
    parser = argparse.ArgumentParser(description="Analyze a sequence file for various features.")
    parser.add_argument("file", help="Path to the input file (Fasta or GenBank format).")
    parser.add_argument("--duplicate", action="store_true", help="Find the longest duplicated subsequence.")
    parser.add_argument("--gc_content", action="store_true", help="Calculate the GC content of the sequence.")

    args = parser.parse_args()

    try:
        # Read the sequence from the file
        with open(args.file, "r") as f:
            records = list(SeqIO.parse(f, "fasta" if args.file.endswith(".fasta") else "genbank"))
            if len(records) == 0:
                raise ValueError("No sequences found in the file.")

            sequence = str(records[0].seq).upper()

        if args.duplicate:
            longest_dup = find_longest_duplicate(sequence)
            print(f"Longest duplicated subsequence: {longest_dup}")

        if args.gc_content:
            gc_content = calculate_gc_content(sequence)
            print(f"GC content: {gc_content:.2f}%")

        if not (args.duplicate or args.gc_content):
            print("No analysis option selected. Use --duplicate or --gc_content.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
