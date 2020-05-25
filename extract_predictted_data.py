import sys
def main(arg):
	file1 = open('result.txt', 'r') 
	Lines = file1.readlines() 

	count = 0
	# Strips the newline character 
	for line in Lines: 
		# print(line)
		if "%" in line:
			if ":" in line:
				res = line.split(':')
				# print(res[0])
				per = res[0]
				if(per == "person"):
					count = count + 1
	print(count)    

if __name__ == "__main__":
    main(sys.argv[0])