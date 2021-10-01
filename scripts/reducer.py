#!/usr/bin/env python
import sys
import csv

class MeanReducer:
    """mean = (c_1 * m_1 + c_2 * m_2 + ... + c_n * m_n) / (c1 + c2 + ... + cn), where

        c_i is chunk size
        m_i is mean of chunk
    """
    def __init__(self) -> None:
        self._reduced_mean_numerator = 0
        self._count = 0

    def add_chunk_mean(self, chunk_mean: float, chunk_size: int):
        self._count += chunk_size
        self._reduced_mean_numerator += chunk_size * chunk_mean

    def mean(self) -> float:
        return self._reduced_mean_numerator / self._count
    
    def total_values(self) -> int:
        return self._count

class StatReducer:
    """var = sum_{j=1}_{total chunks} (var_j + m_j) * c_j / (c_1 + c_2 + ... + c_j) - MeanCollector ** 2, where
        c_i is chunk size
        var_j is variance of chunk
        m_j is mean of chunk
    """
    def __init__(self):
        self._reduced_mean = MeanReducer()
        self._reduced_variance_part = 0

    def add_chunk_stat(self, chunk_mean: float, chunk_var: float, chunk_size: int):
        self._reduced_mean.add_chunk_mean(chunk_mean, chunk_size)
        self._reduced_variance_part += (chunk_var + chunk_mean ** 2) * chunk_size
    
    def variance(self) -> float:
        return self._reduced_variance_part / self._reduced_mean.total_values() - self._reduced_mean.mean() ** 2

    def mean(self) -> float:
        return self._reduced_mean.mean()
    

if __name__ == "__main__":

    stat_reducer = StatReducer()

    for row in csv.reader(sys.stdin, delimiter=" "):
        chunk_size, chunk_mean, chunk_var = int(row[0]), float(row[1]), float(row[2])
        stat_reducer.add_chunk_stat(chunk_mean, chunk_var, chunk_size)

    print(f"{'MapReduce computation.':<25}", f"{'mean:':<6}", f"{stat_reducer.mean():<18}", f"{'variance:':<9}", f"{stat_reducer.variance():<18}")
            
    