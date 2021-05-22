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
			output = output + 'INSERT INTO wpo0_usermeta (user_id, meta_key, meta_value) VALUES (' + source_record['ID'] + ', "pets-name", "' + target_record['Pets Name'] + '");\n'
			output = output + 'INSERT INTO wpo0_usermeta (user_id, meta_key, meta_value) VALUES (' + source_record['ID'] + ', "instagram-handle", "' + target_record['Instagram Handle'] + '");\n'
			output = output + 'INSERT INTO wpo0_usermeta (user_id, meta_key, meta_value) VALUES (' + source_record['ID'] + ', "pets-birthday", "' + target_record['Birthday/Gotchaday'] + '");\n'


			return True
	return False

source = loadCSV('users.csv')
target = loadCSV('emails.csv')

matched = []
unmatched = []

for source_record in source:
	if filter_on_field(source_record, 'user_email', target,'user_email'):
		matched.append(source_record)
	else:
		unmatched.append(source_record)

for matched_entry in matched:
	print(matched_entry)

with open("out.sql", "w") as f:
	f.write(output)