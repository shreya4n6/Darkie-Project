from modules import statics
import csv

def saveOnionLinksToTxtFile(data, filename):
    print(f"{statics.C}Writing onion links to : ", filename)
    print(f"{statics.W}")

    with open(filename, 'w', encoding="utf-8") as f:
        for row in data:
            f.write(str(row) + "\n")

    print(f"{statics.G}Writing done : ", filename)
    print(f"{statics.W}")


def saveOnionLinksToCSVFile(data, filename):
    print(f"{statics.C}Writing onion links to : ", filename)
    print(f"{statics.W}")

    with open(filename, 'w', newline='', encoding="utf-8") as file:
        header = ['Keyword', 'Engine', 'URL']
        writer = csv.DictWriter(file, fieldnames = header)

        writer.writeheader()

        for row in data:
            writer.writerow(row)

    print(f"{statics.G}Writing done : ", filename)
    print(f"{statics.W}")