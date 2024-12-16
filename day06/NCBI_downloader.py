import argparse
import os
import csv
from datetime import datetime
from Bio import Entrez

# Setting email for NCBI usage policy
Entrez.email = "adi.barnoor@weizmann.ac.il"

# Searching NCBI database for a given term and return the list of IDs and the total count of items found
def search_ncbi(database, term, max_results):
    handle = Entrez.esearch(db=database, term=term, retmax=max_results)
    record = Entrez.read(handle)
    handle.close()
    ids = record['IdList']
    total_count = int(record['Count'])
    return ids, total_count

# Downloading NCBI data for a provided list of IDs and save each item as a separate file
def download_ncbi_data(database, ids, output_dir="ncbi_downloads"):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    filenames = []
    for idx, ncbi_id in enumerate(ids):
        handle = Entrez.efetch(db=database, id=ncbi_id, rettype="gb", retmode="text")
        data = handle.read()
        handle.close()
        
        filename = os.path.join(output_dir, f"{database}_{ncbi_id}.txt")
        with open(filename, "w") as file:
            file.write(data)
        filenames.append(filename)
    
    return filenames

# Log the details of the query to a CSV file
def log_query_to_csv(date, database, term, max_results, total_count, csv_filename="ncbi_query_log.csv"):
    log_exists = os.path.isfile(csv_filename)
    with open(csv_filename, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not log_exists:  # Write header if the file does not exist
            writer.writerow(["date", "database", "term", "max", "total"])
        writer.writerow([date, database, term, max_results, total_count])


def main():
    parser = argparse.ArgumentParser(description="Download data from NCBI and log the query.")
    parser.add_argument("--database", type=str, default="nucleotide", help="The NCBI database to search. Default is 'nucleotide'.")
    parser.add_argument("--term", type=str, required=True, help="The search term for the NCBI database.")
    parser.add_argument("--number", type=int, default=10, help="The maximum number of items to download. Default is 10.")
    args = parser.parse_args()
    
    database = args.database
    term = args.term
    max_results = args.number
    
    print(f"Searching NCBI database '{database}' for term '{term}' with a maximum of {max_results} results...")
    
    ids, total_count = search_ncbi(database, term, max_results)
    if not ids:
        print("No records found.")
        return
    
    print(f"ids {ids}")
    print(f"Found {total_count} total items, downloading {len(ids)} items...")
    filenames = download_ncbi_data(database, ids)
    
    print("Downloaded files:")
    for filename in filenames:
        print(f"  {filename}")
    
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_query_to_csv(current_time, database, term, max_results, total_count)
    print(f"Query details logged to 'ncbi_query_log.csv'.")


if __name__ == "__main__":
    main()
