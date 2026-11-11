import csv
import matplotlib.pyplot as plt

def read_data(csv_file):
    with open(csv_file, 'r', newline='') as f:
        reader = csv.DictReader(f)
        data = {}
        for row in reader:
            y = int(row['year'])
            # mpg = int(row['comb08'])
            if y not in data:
                data[y] = []
            data[y].append(row)
    return data

def compute_mgg(data, key):
    sum = 0
    for row in data:
        sum += float(row[key])

    return sum / len(data)


if __name__ == '__main__':
    datafile = 'vehicles1.csv'
    dataset = read_data(datafile)
    #print(dataset)

    year_list = list(dataset.keys())
    year_list.sort()

    print(year_list)
    mpgs_list = []

    for year in year_list:
        mpg = compute_mgg(dataset[year], 'highway08')
        print(mpg)
        mpgs_list.append(mpg)
    print(mpgs_list)

    plt.plot(year_list, mpgs_list)
    plt.show()