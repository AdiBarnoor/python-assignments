import sys
from collections import Counter

def analyze_sequence(sequence):
    # Analyzes a nucleotide sequence and returns the counts of each nucleotide and their precentage
    counts = Counter(sequence.upper())
    total = sum(counts.values())
    bases = ['A', 'C', 'G', 'T']
    stats = {base: counts.get(base, 0) for base in bases}
    stats['Unknown'] = total - sum(stats.values())
    stats['Total'] = total
    return stats

def process_file(filename):
    # Reads a file\s with a sequence and returns the combined sequence
    with open(filename, 'r') as f:
        # Remove whitespace and combine all lines
        sequence = ''.join(line.strip() for line in f if not line.startswith('>'))  # Handles FASTA headers
    return sequence

def display_results(stats, total_files):
    # Displays analyzed results for a sequence
    total = stats['Total']
    print(f"Combined results from {total_files} files")
    for base in ['A', 'C', 'G', 'T', 'Unknown']:
        count = stats[base]
        percent = (count / total * 100) if total > 0 else 0
        print(f"{base}: {count:8} {percent:>6.1f}%")
    print(f"Total: {total}\n")

def main(filenames):
    # Main function - analyzes one or more sequence files and combine their statistics
    combined_stats = Counter({'A': 0, 'C': 0, 'G': 0, 'T': 0, 'Unknown': 0, 'Total': 0})
    for filename in filenames:
        sequence = process_file(filename)
        stats = analyze_sequence(sequence)
        combined_stats.update(stats)
    display_results(combined_stats, len(filenames))

if __name__ == "__main__":
    # Example usage: python script.py file1.txt file2.txt
    if len(sys.argv) < 2:
        print("At least one file needed")
    else:
        main(sys.argv[1:])