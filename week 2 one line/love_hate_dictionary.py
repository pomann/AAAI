def read_dictionary(filename, length):
	return [line.strip() for line in open(filename,'r') if len(line.strip()) == length and not (any(x.isupper() for x in line))]