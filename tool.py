import csv
output = ""
def loadCSV(path):
	with open(path, newline='', encoding="utf-8-sig") as csvfile:
		return list(csv.DictReader(csvfile, delimiter=','))

def filter_on_field(source_record, source_field, target, target_field):
	global output
	for target_record in target:
		if(' - P' in target_record['Name']):
			continue
		# print(source_record[source_field], target_record[target_field] )
		if ( source_record[source_field] == target_record[target_field] ):
		# 	target_record['Length (in)'] = source_record['Length']
		# 	target_record['Width (in)'] = source_record['Width']
		# 	target_record['Height (in)'] = source_record['Height']
		# 	target_record['Weight (lbs)'] = source_record['Weight']
			return target_record
	return False

source = loadCSV('a.csv')
target = loadCSV('b.csv')

matched = []
unmatched = []

for source_record in source:
	result_record = filter_on_field(source_record, 'SKU', target,'Name')
	if result_record:
		matched.append(result_record)
	else:
		unmatched.append(source_record)

def filterUnmatched(unmatched_entry):
	return not (unmatched_entry['SKU'].strip() == '' or 'composite' in unmatched_entry['Type'] or 'variable' in unmatched_entry['Type'])

unmatched = list(filter(filterUnmatched, unmatched))

with open("matcheda.csv", "w", encoding="utf-8") as f:
	headers = matched[0].keys()
	writer = csv.DictWriter(f,headers, delimiter=',', lineterminator='\n', extrasaction='ignore')
	writer.writeheader()
	writer.writerows(matched)

with open("unmatcheda.csv", "w", encoding="utf-8") as f:
	headers = unmatched[0].keys()
	writer = csv.DictWriter(f,headers, delimiter=',', lineterminator='\n', extrasaction='ignore')
	writer.writeheader()
	writer.writerows(unmatched)