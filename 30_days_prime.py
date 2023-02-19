# # year = int(input("Enter your year : "))


# def is_leap():
#     if year % 4 == 0:
#         if year % 100 == 0:
#             if year % 400 == 0:
#                 print("leap year")
#             else:
#                 print("not leap year")
#         else:
#             print("leap year")
#     else:
#         print("not leap year")


# def days_in_month(years,month):
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if is_leap == "Leap year":
#         month_days[1] = 29
#     print(month_days[month-1])


# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

def is_leap(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year,month):
    if month > 12 and month <1:
        print("Invalid inpu! please enter int value from 1-12")
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year) and month == 2:
        return 29
    else:
        return month_days[month-1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)
