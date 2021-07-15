import csv

with open("./data/sample1.csv","r")as f:
    reader = csv.DictReader(f)

    next(reader)

    for c in reader:
        for k,v in c.items():
            print(k,v)
        print()

        # print(c['번호'])