import sys
import csv

def main():
    f = open("/tmp/data/Managers.csv")
    dataReader = csv.reader(f, delimiter=',')
    for row in dataReader:
        print(row)

    print("Service finish!")

if __name__ == "__main__":
    main()