import csv
import gzip
import argparse
from statistics import mean, pvariance
from mapper import StreamingStat


def price_iterator(file_object):
    reader = csv.reader(file_object)
    header = next(reader)
    price_index = header.index("price")

    for row in reader:
        try:
            yield float(row[price_index])
        except ValueError:
            pass

def main(args):
    stat = StreamingStat()

    with gzip.open(args.file, "rt", encoding="utf-8", newline="") as file:
        mean_value = mean(price_iterator(file))
        file.seek(0)
        var_value = pvariance(price_iterator(file))
        file.seek(0)
        for price in price_iterator(file):
            stat.add_value(price)

    print(f"{'Standard computation.':<25}", f"{'mean:':<6}", f"{mean_value:<18}", f"{'variance:':<9}", f"{var_value:<18}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", type=str, required=True, help="A path to compressed csv")

    args = parser.parse_args()

    main(args)