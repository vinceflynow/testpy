properties = {}
with open('test.properties') as propfile:
	for line in propfile:
		key, value = line.strip().split('=')
		properties[key] = value

with open('othertest.properties', "a") as outfile:
	for akey in properties.keys():
		outfile.write(akey + "=" + properties[key] + "\n")

