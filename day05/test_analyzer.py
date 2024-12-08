import analyze_seq
from collections import Counter
import os

def analyze_files(file_paths):
    # Analyze sequences from multiple files
    combined_stats = Counter()
    
    for file_path in file_paths:
        if os.path.exists(file_path):  # Ensure file exists
            with open(file_path, 'r') as file:
                sequence = file.read().strip()  # Read sequence from file
                stats = analyze_seq.analyze_sequence(sequence)
                combined_stats.update(stats)  # Combine stats from each file
        else:
            print(f"File {file_path} not found.")
    
    return combined_stats

def test_combined_analysis():
    # Test reading multiple files and combining their stats
    file_paths = ['test1.txt', 'test2.txt']
    combined_stats = analyze_files(file_paths)
    print(f"Combined Stats: {dict(combined_stats)}")
    expected_stats = {'A': 8, 'C': 7, 'G': 12, 'T': 12, 'Unknown': 4, 'Total': 43}
    print(f"Expected Stats: {expected_stats}")
    if dict(combined_stats) == expected_stats:
        print("Test passed!")
    else:
        print("Test failed!")

def test_empty_sequence():
    # Test an empty sequence
    sequence = ""
    stats = analyze_seq.analyze_sequence(sequence)
    print(f"Stats for empty sequence: {dict(stats)}")
    expected_stats = {'A': 0, 'C': 0, 'G': 0, 'T': 0, 'Unknown': 0, 'Total': 0}
    print(f"Expected Stats: {expected_stats}")
    if dict(stats) == expected_stats:
        print("Test passed!")
    else:
        print("Test failed!")

def test_single_nucleotide():
    # Test sequence with one type of nucleotide
    sequence = "AAAAA"
    stats = analyze_seq.analyze_sequence(sequence)
    print(f"Stats for single nucleotide sequence: {dict(stats)}")
    expected_stats = {'A': 5, 'C': 0, 'G': 0, 'T': 0, 'Unknown': 0, 'Total': 5}
    print(f"Expected Stats: {expected_stats}")
    if dict(stats) == expected_stats:
        print("Test passed!")
    else:
        print("Test failed!")

def test_non_nucleotide_characters():
    # Test sequence with non-nucleotide characters
    sequence = "AGXT!"
    stats = analyze_seq.analyze_sequence(sequence)
    print(f"Stats for non-nucleotide sequence: {dict(stats)}")
    expected_stats = {'A': 1, 'C': 0, 'G': 1, 'T': 1, 'Unknown': 2, 'Total': 5}
    print(f"Expected Stats: {expected_stats}")
    if dict(stats) == expected_stats:
        print("Test passed!")
    else:
        print("Test failed!")

def test_file_not_found():
    # Test for non-existing file
    file_paths = ['non_existent_file.txt', 'test1.txt']
    combined_stats = analyze_files(file_paths)
    print(f"Combined Stats: {dict(combined_stats)}")
    expected_stats = {'A': 5, 'C': 5, 'G': 7, 'T': 7, 'Unknown': 3, 'Total': 27}
    print(f"Expected Stats: {expected_stats}")
    if dict(combined_stats) == expected_stats:
        print("Test passed!")
    else:
        print("Test failed!")

if __name__ == "__main__":
    print("Running combined analysis test:")
    test_combined_analysis()

    print("\nRunning empty sequence test:")
    test_empty_sequence()

    print("\nRunning single nucleotide sequence test:")
    test_single_nucleotide()

    print("\nRunning non-nucleotide characters test:")
    test_non_nucleotide_characters()

    print("\nRunning file not found test:")
    test_file_not_found()