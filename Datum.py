def zeller(day, mon, year, century):
    tot = 0
    if mon == 1 or mon == 2:
        mon = mon + 10
        year = year-1
    else:
        mon = mon - 2
    if year<0:
        year = 99
        century = century-1
    #print(day)
    #print(mon)
    #print(year)
    #print(century)
    tot = (day + int(2.6*mon-0.2) - (2*century) + year + int(year/4) + int(century/4))%7
    return int(tot)

d, m = [int(x) for x in input().split(" ")]
#print(d)
#print(m)
#print(zeller(d, m, 9, 00))
a = {
    1: "Monday",
    2: "Tuesday",
    3: "Wednesday",
    4: "Thursday",
    5: "Friday",
    6: "Saturday",
    0: "Sunday"
}
print(a.get(zeller(d, m, 9, 00)))
