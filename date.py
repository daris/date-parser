import functools
from os import path
from sys import argv


class Date(object):
    def __init__(self, day, month, year):
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)

        if self.year < 100:
            self.year = 2000 + self.year

    @staticmethod
    def is_leap_year(year):
        return year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0)

    @staticmethod
    def get_number_of_days_in_month(month, year=2000):
        if month == 2:
            return 29 if Date.is_leap_year(year) else 28

        if month <= 7:
            return 30 if month % 2 == 0 else 31

        if month > 7:
            return 31 if month % 2 == 0 else 30

        return None

    def is_valid(self):
        if self.day < 1 or self.day > 31:
            return False

        if self.month < 1 or self.month > 12:
            return False

        if self.year < 2000 or self.year > 2999:
            return False

        num_days_in_month = Date.get_number_of_days_in_month(self.month, self.year)
        if self.day > num_days_in_month:
            return False

        return True

    def format(self):
        return '{:04d}-{:02d}-{:02d}'.format(self.year, self.month, self.day)

    def __str__(self):
        return self.format()

    def __eq__(self, other):
        return self.day == other.day and self.month == other.month and self.year == other.year

    def __gt__(self, other):
        if self.year == other.year:
            if self.month == other.month:
                return self.day > other.day

            return self.month > other.month

        return self.year > other.year

    def __lt__(self, other):
        if self.year == other.year:
            if self.month == other.month:
                return self.day < other.day

            return self.month < other.month

        return self.year < other.year


def get_earliest_date(a, b, c):
    available_dates = [
        Date(a, b, c),
        Date(a, c, b),
        Date(b, a, c),
        Date(b, c, a),
        Date(c, a, b),
        Date(c, b, a),
    ]

    valid_dates = [d for d in available_dates if d.is_valid()]
    if not valid_dates:
        return None

    sorted_dates = sorted(valid_dates, key=functools.cmp_to_key(compare_date))
    return sorted_dates[0]


def compare_date(d1, d2):
    if d1 > d2:
        return 1

    if d1 == d2:
        return 0

    if d1 < d2:
        return -1


def parse_dates(dates):
    for line in dates:
        line = line.strip()
        a, b, c = line.split('/')
        earliest_date = get_earliest_date(a, b, c)

        print('{:<10} => {}'.format(line, earliest_date.format() if earliest_date else 'is illegal'))


if __name__ == "__main__":
    if len(argv) < 2:
        print('Filename argument is required')
        exit()

    filename = argv[1]
    if not path.isfile(filename):
        print('File does not exist')
        exit()

    with open(filename, 'r') as f:
        lines = f.readlines()
        parse_dates(lines)
