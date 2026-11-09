import csv
import sys

def trim_data(raw_data_file):
    cs104_headers=["id", "year", "make", "model", "cylinders","VClass",
                "city08","highway08","comb08","fuelType","atvType", "co2",
                "displ", "trany", "drive"]

    with open(raw_data_file, 'r', newline='') as f,\
        open('trimmed_vehicles.csv', 'w', newline='') as g:
        reader = csv.DictReader(f)
        writer = csv.DictWriter(g, fieldnames=cs104_headers)
        print(reader.fieldnames)#headers
        writer.writeheader()
        for row in reader:
            new_row = {}
            for key in cs104_headers:
                new_row[key] = row[key]
            print(new_row)
            writer.writerow(new_row)
            break

def filter_by_year(csv_file, y):
    rows_year = []
    if __name__ == '__main__':
        raw_data_file = "vehicles.csv"
        trimmed_file = "trimmed_vehicles.csv"

        year = 2025
        filter_by_year(trimmed_file, y)
        with open(trimmed_file, 'r', newline='') as g:
            reader = csv.DictReader(g)
            for row in reader:
                print(row)
                if row["year"] == year:
                    rows_year.append(row)
    return rows_year



###### MAIN #######

print(f"__name__ is {__name__}")
if __name__ == "__main__":
    print(sys.argv)
    if len(sys.argv) != 2:
        print("")
        sys.exit(2)

    data_file = sys.argv[1]
    trimmed = trim_data(data_file)
    sys.exit()