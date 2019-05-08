# https://docs.python.org/3/library/csv.html
import csv


def process_csv(infilename="sample.csv", outfilename="output.csv"):
    infile = open(infilename, "r", newline="", encoding="utf-8")
    outfile = open(outfilename, "w", newline="", encoding="utf-8")
    reader = csv.DictReader(infile)
    writer = csv.DictWriter(outfile, ["First name", "Last name", "User ID"])
    writer.writeheader()

    for row in reader:
        if row["Grade"] in ["9", "10", "11", "12"]:
            new_row = {
                "First name": row["First name"],
                "Last name": row["Last name"],
                "User ID": (row["Last name"] + row["First name"][0]).lower(),
            }
            writer.writerow(new_row)

    infile.close()
    outfile.close()
