#!/usr/bin/env python
import sys
import csv

def read_csv_input(file):
    for row in csv.reader(file):
        yield row

class StreamignMean:
    def __init__(self):
        self._partial_sum = 0
        self._count = 0

    def add_value(self, new_value: float) -> None:
        self._partial_sum += new_value
        self._count += 1

    def mean(self) -> float:
        return self._partial_sum / self._count

    def total_meas(self) -> int:
        return self._count


class StreamingStat:
    def __init__(self) -> None:
        self._streaming_mean = StreamignMean()
        self._partial_square_sum = 0

    def add_value(self, new_value: float) -> None:
        self._streaming_mean.add_value(new_value)
        self._partial_square_sum += new_value ** 2

    def total_meas(self) -> int:
        return self._streaming_mean.total_meas()

    def variance(self) -> float:
        return self._partial_square_sum / self.total_meas() - self._streaming_mean.mean() ** 2

    def mean(self) -> float:
        return self._streaming_mean.mean()

if __name__ == "__main__":
    price_index = 9

    stat = StreamingStat()

    for row in read_csv_input(sys.stdin):
        try:
            price = float(row[price_index])
            stat.add_value(price)
        except ValueError:
            pass
    
    print(stat.total_meas(), stat.mean(), stat.variance())
            
    