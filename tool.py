import csv

#Loads the CSV from the path snd returns it as a list
def loadCSV(path):
	with open(path, newline='', encoding="utf-8-sig") as csvfile:
		return list(csv.DictReader(csvfile, delimiter=','))

#Searches for a record in target with the same value in the coinciding field.
def find_match_on_field(source_record, source_field, target, target_field):
	for target_record in target:
		# print(source_record[source_field], target_record[target_field] )
		if ( source_record[source_field] == target_record[target_field] ):
			if target_field == 'SKU':
				target_record['Stock'] = source_record['Variant Inventory Qty']
				target_record['Regular price'] = source_record['Variant Price']

			return target_record
	return False

#Writes the provided list as a csv
def write_results(path, list_to_write):
	if len(list_to_write) == 0:
		print("No records to write to",path)
		return
	with open(path, "w", encoding="utf-8") as f:
		headers = list_to_write[0].keys()
		writer = csv.DictWriter(f,headers, delimiter=',', lineterminator='\n', extrasaction='ignore')
		writer.writeheader()
		writer.writerows(list_to_write)

#Finds matched and unmatched fields from the source in the target
def check_for_matches(source, target, source_field, target_field):
	matched = []
	unmatched = []

	for source_record in source:
		result_record = find_match_on_field(source_record, source_field, target, target_field)
		if result_record:
			matched.append(result_record)
		else:
			unmatched.append(source_record)

	return matched, unmatched

#Finds the matched and unmatched records in both directions.
def process_set(set_name, source, target, source_field, target_field):
	matched, unmatched = check_for_matches(source, target, source_field, target_field);
	write_results("matched_source_" + set_name + ".csv", matched)
	write_results("unmatched_source_" + set_name + ".csv", unmatched)

a_field = 'Variant SKU'
b_field = 'SKU'

source_a = loadCSV('a.csv')
source_b = loadCSV('b.csv')
process_set('a', source_a, source_b, a_field, b_field)
process_set('b', source_b, source_a, b_field, a_field)
