def get_earliest(date1, date2):
    m1,d1,y1 = date1.split("/")
    m2,d2,y2 = date2.split("/")
    return date1 if (y1,m1,d1) < (y2,m2,d2) else date2

def get_earliest_bonus(*dates):
    def get_dates(date):
        m1,d1,y1 = date.split("/")
        return (y1,m1,d1)
    return min(dates,key=get_dates)