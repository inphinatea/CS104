import csv
import sys

weights = {
    'quiz': 0.1,
    'lab': 0.1,
    'test1': 0.1,
    'test2': 0.1,
    'project': 0.1,
    'final': 0.1
}


def read_csv(filename):
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    score_types = lines[0].strip().lower().split(',')
    score_types.pop(0)
    print(score_types)
    grades = {}

    for line in lines[1:]:
        clean_lines = line.strip().lower()
        items = clean_lines.split(',')
        print(items)
        name = items[0]
        grades[name] = {
            "quiz": int(items[1]),
            "lab": int(items[2]),
            "test1": int(items[3]),
            "test2": int(items[4]),
            "project": int(items[5]),
            "final": int(items[6])
        }
    return grades


def compute_weighted_grade(scores):
    weighted_grade = {}
    score = 0
    for key in scores:
        score += weights[key] * scores[key]
    return score, score2letter(score)


def score2letter(score):
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 70:
        return 'C'
    elif score >= 60:
        return 'D'
    else:
        return 'F'


################## MAIN #####################

file_name = sys.argv[1]

with open(file_name, 'r', newline='') as f:
    reader = csv.DictReader(f)
    print(reader.fieldnames)  # headers
    for row in reader:
        print(row)

grades = read_csv(file_name)
print(file_name)

for key in grades:
    mark, letter_grade = compute_weighted_grade(grades[key])
    print(key, mark, letter_grade)
