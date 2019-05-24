
dates = ['1/2/3', '3/20/1']

def get_date(a, b, c):
    results = [
        # is_valid_date
    ]


class Date(object):
    def __init__(self, day, month, year):
        self.day = int(day)
        self.month = int(month)
        self.year = int(year)

        if year < 2000:
            year = 2000 + year

    # def get_unix_timestamp(day, month, year):
    #     day_seconds = 24 * 3600
    #     month_seconds = day_seconds &


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


    def is_valid_date(self):
        if self.day < 1 or self.day > 31:
            return False

        if self.month < 1 or self.month > 12:
            return False

        if self.year < 2000 or self.year > 2999:
            return False


# for date in dates:
#     pass