import csv

# Returns a list of rows from the passed .csv file 
def readCsv(filepath):
    rows = []
    with open(filepath, newline='') as csvfile:
        filereader = csv.reader(csvfile)
        for row in filereader:
            rows.append(row)
    
    return rows


def main():
    print(readCsv("data/test.csv"))


if __name__ == "__main__":
    main()