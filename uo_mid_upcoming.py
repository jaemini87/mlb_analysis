import os
def run():
	fin = open("raw.txt",'r')
	fout = open("data.txt",'w')
	fin_cnt = 0
	while(1):
		fin_line = fin.readline()
		if not fin_line:
			break
		if fin_line == '\n':
			continue
		for ii in fin_line:
			if ii != '\n':
				fout.write(ii)
		print(fin_line)
		if fin_cnt % 4 == 3:
		 	fout.write("#7.5 1.9 1.9 0 0")
			fout.write('\n')
		elif fin_cnt % 4 == 2:
			fout.write(" 0:0 ")
		else:
			fout.write(" ")
		fin_cnt+=1
	fin.close()
	fout.close()
run()
command = "tac data.txt > data_rev.txt"
os.system(command)



