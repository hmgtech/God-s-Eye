import os
import sys
import subprocess
def main(arg):
	# os.system('cmd /c "darknet detector test cfg/voc.data cfg/yolov3.cfg yolov3.weights -dont_show -ext_output <data/train1.txt> result.txt"')
	#print("Test Successful....")
	
	s2_out = subprocess.check_output([sys.executable, "extract_predictted_data.py"])
	# print (s2_out)
	#os.system('cmd /c "python extract_predictted_data.py"')
	#print("Data Collected...",s2_out)
	string1 = s2_out.decode("utf-8")
	# print(string1)
	integer1 = int(string1)
	print(integer1)
	# print("Sending Alert Message to officials...")
	# return "integer1"
if __name__ == "__main__":
    main(sys.argv[0])