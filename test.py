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


assert Date(31, 1, 2000).is_valid()
assert Date(28, 2, 2000).is_valid()
assert Date(29, 2, 2000).is_valid()
assert Date(28, 2, 2001).is_valid()
assert not Date(29, 2, 2001).is_valid()
assert Date(28, 2, 2100).is_valid()
assert not Date(29, 2, 2100).is_valid()


assert (Date(29, 2, 2000) < Date(1, 3, 2000))
assert not (Date(29, 2, 2000) > Date(1, 3, 2000))

assert (Date(28, 2, 2000) < Date(29, 2, 2000))
assert not (Date(28, 2, 2000) > Date(29, 2, 2000))

assert (Date(1, 2, 2000) < Date(1, 2, 2001))
assert not (Date(1, 2, 2000) > Date(1, 2, 2001))
