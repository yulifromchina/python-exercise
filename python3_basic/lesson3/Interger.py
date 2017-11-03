#!/usr/bin/env python3
days = int(input("Enter days:"))
# months = days // 30
# day = days % 30
# print("Month = {} Days = {}".format(months, day))
print("Month = {} Days = {}".format(*divmod(days, 30)))
