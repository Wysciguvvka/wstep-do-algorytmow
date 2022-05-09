import numpy as np


class Students:
    def __init__(self) -> None:
        self.grades = [2.0, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5]
        self.courses = ['k1', 'k2', 'k3', 'k4', 'k5', 'k6']
        self.studentsCount = 20
        self.students = self.init_students()

    def init_students(self) -> np.array:
        return np.random.choice(self.grades, size=(self.studentsCount, len(self.courses)))

    def highest_avg(self) -> (list, float):
        averages = [sum(row) / len(row) for row in self.students]
        _max = max(averages)
        _students = [self.students[i] for i, v in enumerate(averages) if v == _max]
        return _students, _max

    def lowest_avg(self) -> (list, float):
        averages = [sum(row) / len(row) for row in self.students]
        _min = min(averages)
        _students = [self.students[i] for i, row in enumerate(averages) if row == _min]
        return _students, _min

    def highest_grades(self) -> (list, int, float):
        highest_grade = np.max(self.students)
        max_occurrences = max([list(grades).count(highest_grade) for _, grades in enumerate(self.students)])
        indices = [i for i, row in enumerate(self.students) if
                   list(row).count(highest_grade) == max_occurrences]
        return indices, max_occurrences, highest_grade

    def average_higher_than(self, average: float = 4.5) -> list:
        qualified_students = [(i, grades, sum(grades) / len(grades)) for i, grades in enumerate(self.students) if
                              sum(grades) / len(grades) >= average]
        return qualified_students

    def histogram(self) -> list:
        histogram = []
        for i in range(0, len(self.courses)):
            histogram.append(np.histogram(self.students[:, i].transpose(), bins=self.grades))
        return histogram

    def failed(self, n: int = 2) -> (int, int):
        failed_students = [True if list(row).count(2.0) >= n else False for row in self.students]
        return failed_students.count(True), n

    def __str__(self) -> str:
        __newline = '\n'
        max_students, max_avg = self.highest_avg()
        min_students, min_avg = self.lowest_avg()
        highest_grades = self.highest_grades()
        average_above = self.average_higher_than()
        failed_students, n = self.failed()
        histograms = self.histogram()

        str_max_students = f'Oceny studentów z najwyższą średnią ({max_avg:.2f}):\n' \
                           f'{__newline.join(map(str, max_students))}\n'

        str_min_students = f'Oceny studentów z najniższą średnią ({min_avg:.2f}):\n' \
                           f'{__newline.join(map(str, min_students))}\n'
        # indices, max_occurrences, highest_grade
        str_highest_grades = f'Oceny studentów z najwyższą liczbą ({highest_grades[1]}) ' \
                             f'ocen najwyższych ({highest_grades[2]}):\n'
        for index in highest_grades[0]:
            str_highest_grades += f'Index: {index}; Oceny: {self.students[index]}\n'

        str_average_above = f'Studenci ze średnią >= 4.5:\n'
        for index, grades, average in average_above:
            str_average_above += f'Index: {index}; Oceny: {grades}; Średnia: {average:.2f}\n'

        str_failed_students = f'Liczba studentów, którzy nie zaliczyli co najmniej {n} przedmiotów: {failed_students}'
        str_histograms = f'histogramy:\n'
        for i, histogram in enumerate(histograms):
            str_histograms += f'Histogram kursu {self.courses[i]}: {histogram}\n'

        text = f'{str_max_students}\n{str_min_students}\n{str_highest_grades}' \
               f'\n{str_average_above}\n{str_failed_students}\n{str_histograms} '
        return text


if __name__ == '__main__':
    students = Students()
    print(students)
