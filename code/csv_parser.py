__author__ = 'David T. Pocock'

import csv


class CSVParser:

    def __init__(self, path):
        self.path = path

    def parse_data(self, is_full_data_set):
        unique_fault_combinations = {}
        test_cases = []
        with open(self.path, newline='') as file:
            matrix_reader = csv.reader(file)
            if not is_full_data_set:
                for row in reversed(list(matrix_reader)):
                    faults_revealed = []
                    for element in row[1:]:
                        inted = int(element)
                        faults_revealed.append(inted)
                    unique_fault_combinations[tuple(faults_revealed)] = row[0]
                for key in unique_fault_combinations.keys():
                    test_case = (unique_fault_combinations.get(key), list(key))
                    test_cases.append(test_case)
            else:
                for row in matrix_reader:
                    faults_revealed = []
                    for element in row[1:]:
                        inted = int(element)
                        faults_revealed.append(inted)
                    test_cases.append((row[0], faults_revealed))
        return test_cases
