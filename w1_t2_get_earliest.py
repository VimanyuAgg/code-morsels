def get_earliest(date1,date2):
    date1_mon, date1_date, date1_year = date1.split("/")
    date2_mon, date2_date, date2_year = date2.split("/")
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
        a_mon, a_date, a_year = a.split("/")
        standard_a = a_year + a_mon + a_date
        date_dict[standard_a] = a


    return date_dict[sorted(date_dict.keys())[0]]