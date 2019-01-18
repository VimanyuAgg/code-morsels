# BEFORE SOLUTION
# def get_earliest(date1,date2):
#     date1_mon, date1_date, date1_year = date1.split("/")
#     date2_mon, date2_date, date2_year = date2.split("/")
#     standard_date1 = date1_year+date1_mon+date1_date
#     standard_date2 = date2_year + date2_mon + date2_date
#
#     if standard_date1 < standard_date2:
#         print("{} < {}".format(standard_date1,standard_date2))
#         return date1
#     else:
#         print("{} < {}".format(standard_date2, standard_date1))
#         return date2
#
# def get_earliest_bonus(*args):
#     date_dict = {} #maps standard date format to given date format
#     for a in args:
#         a_mon, a_date, a_year = a.split("/")
#         standard_a = a_year + a_mon + a_date
#         date_dict[standard_a] = a
#
#
#     return date_dict[sorted(date_dict.keys())[0]]

# AFTER SOLUTION
def get_earliest(date1,date2):
	m1,d1,y1 = date1.split("/")
	m2,d2,y2 = date2.split("/")
	if (y1,m1,d1) < (y2,m2,d2):
		return date1
	else:
		return date2

def get_earliest_bonus(*dates):
	def convert_to_standard(date):
		m1,d1,y1 = date.split("/")
		return (y1,m1,d1)
	return min(dates, key=convert_to_standard)

# newer = "03/21/1946"
# older = "02/24/1946"
#
# print(get_earliest_bonus(newer,older))