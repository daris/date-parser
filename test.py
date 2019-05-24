from date import Date

assert Date.get_number_of_days_in_month(1) == 31
assert Date.get_number_of_days_in_month(2, 2000) == 29
assert Date.get_number_of_days_in_month(2, 2001) == 28
assert Date.get_number_of_days_in_month(2, 2100) == 28
assert Date.get_number_of_days_in_month(2, 2012) == 29
assert Date.get_number_of_days_in_month(3) == 31
assert Date.get_number_of_days_in_month(4) == 30
assert Date.get_number_of_days_in_month(6) == 30
assert Date.get_number_of_days_in_month(7) == 31
assert Date.get_number_of_days_in_month(8) == 31
assert Date.get_number_of_days_in_month(9) == 30
assert Date.get_number_of_days_in_month(11) == 30
assert Date.get_number_of_days_in_month(12) == 31