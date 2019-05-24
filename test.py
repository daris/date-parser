from date import Date

assert Date.get_number_of_days_in_month(1) == 31
assert Date.get_number_of_days_in_month(2, 2000) == 29
assert Date.get_number_of_days_in_month(2, 2001) == 28
assert Date.get_number_of_days_in_month(2, 2100) == 28
assert Date.get_number_of_days_in_month(2, 2012) == 29
