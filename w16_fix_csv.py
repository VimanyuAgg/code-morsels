

# ----------------------after 2-----------------------------------------------------
import csv
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument('old_filename')
parser.add_argument('new_filename')
parser.add_argument('--in-delimiter', dest='delim')
parser.add_argument('--in-quote', dest='quote')
args = parser.parse_args()

with open(args.old_filename, newline='') as old_file:
	arguments = {}
	if args.delim:
		arguments['delimiter'] = args.delim
	if args.quote:
		arguments['quotechar'] = args.quote

	if not args.delim and not args.quote:
		arguments['dialect'] = csv.Sniffer().sniff(old_file.read())
		old_file.seek(0)
	reader = csv.reader(old_file, **arguments)
	rows = list(reader)

with open(args.new_filename, newline='', mode='wt') as new_file:
	writer = csv.writer(new_file)
	writer.writerows(rows)






# ----------------------after 1-----------------------------------------------------
# import csv
# from argparse import ArgumentParser
#
#
# parser = ArgumentParser()
# parser.add_argument("old_filename")
# parser.add_argument("new_filename")
# parser.add_argument("--in-delimiter", dest='delim', default="|")
# parser.add_argument("--in-quote", dest='quote', default=",")
# args = parser.parse_args()
#
# with open(args.old_filename, newline='') as old_file:
# 	reader = csv.reader(old_file, delimiter=args.delim, quotechar=args.quote)
# 	rows = list(reader)
#
# with open(args.new_filename, newline='', mode='wt') as new_file:
# 	writer = csv.writer(new_file)
# 	writer.writerows(rows)



# --------------------- original 1----------------------------------------------------
# import sys
# from csv import reader, writer

# original_filename = sys.argv[1]
# new_filename = sys.argv[2]
#
# original_csv = open(original_filename,"rt")
# new_csv = open(new_filename, "wt")
# read = reader(original_csv, delimiter = "|")
# out = writer(new_csv, delimiter = ",")
# for line in read:
# 	out.writerow(line)
#
# original_csv.close()
# new_csv.close()
