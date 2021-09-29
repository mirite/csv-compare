import csv
output = ""
def loadCSV(path):
	with open(path, newline='', encoding="utf-8-sig") as csvfile:
		return list(csv.DictReader(csvfile, delimiter=','))

def filter_on_field(source_record, source_field, target, target_field):
	global output
	for target_record in target:
		# print(source_record[source_field], target_record[target_field] )
		if ( source_record[source_field] == target_record[target_field] ):
			return target_record
	return False

def write_results(path, list_to_write):
	if len(list_to_write) == 0:
		print("No records to write to",path)
		return
	with open(path, "w", encoding="utf-8") as f:
		headers = list_to_write[0].keys()
		writer = csv.DictWriter(f,headers, delimiter=',', lineterminator='\n', extrasaction='ignore')
		writer.writeheader()
		writer.writerows(list_to_write)

source = loadCSV('b.csv')
target = loadCSV('a.csv')

matched = []
unmatched = []

for source_record in source:
	result_record = filter_on_field(source_record, 'Email', target,'Email')
	if result_record:
		matched.append(result_record)
	else:
		unmatched.append(source_record)

for unmatched_entry in unmatched:
	print(unmatched_entry)

write_results("matched.csv", matched)
write_results("unmatched.csv", unmatched)