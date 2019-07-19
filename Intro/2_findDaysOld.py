daysOfMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):
  if year % 4 == 0 and year % 100 != 0:
    return True
  if year % 400 == 0:
    return True
  return False

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    if y1 > y2:
        return None
    if m1 > m2 and y1 == y2:
        return None

    fullYearsDays = 0
    for i in range(y1, y2 + 1):
        fullYearsDays += 366 if isLeapYear(i) else 365
    fullYearsDays -= (sum(daysOfMonth[0:m1 - 1]) + d1) 
    fullYearsDays -= (sum(daysOfMonth[m2:]) + (daysOfMonth[m2-1] - d2))
    return fullYearsDays

# print(daysBetweenDates(1992, 8, 3, 2019, 5, 27))
# print(daysBetweenDates(2019, 5, 26, 2019, 5, 27))
# print(daysBetweenDates(2013, 1, 24, 2013, 6, 29)) #156
print(daysBetweenDates(1912, 7, 24, 2015, 6, 29))