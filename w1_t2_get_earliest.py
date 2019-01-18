def get_earliest(date1,date2):
    date1_mon, date1_date, date1_year = date1.split("/")[0], date1.split("/")[1], date1.split("/")[2]
    date2_mon, date2_date, date2_year = date2.split("/")[0], date2.split("/")[1], date2.split("/")[2]
    standard_date1 = date1_year+date1_mon+date1_date
    standard_date2 = date2_year + date2_mon + date2_date

    if standard_date1 < standard_date2:
        print("{} < {}".format(standard_date1,standard_date2))
        return date1
    else:
        print("{} < {}".format(standard_date2, standard_date1))
        return date2

def get_earliest_bonus(*args):
    date_dict = {} #maps standard date format to given date format
    for a in args:
        a_mon, a_date, a_year = a.split("/")[0], a.split("/")[1], a.split("/")[2]
        standard_a = a_year + a_mon + a_date
        date_dict[standard_a] = a


    return date_dict[sorted(date_dict.keys())[0]]
