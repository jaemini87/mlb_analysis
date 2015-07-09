__author__ = 'jaemin'
from collections import Counter
import numpy as np
import pykov
import os
import sys
from scipy.stats import pearsonr

from matplotlib.colors import LogNorm
import pylab as pl
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import milk
import milk.supervised.tree
import milk.supervised.adaboost
import milk.supervised.multi
line_black = []
line_red = []

yy = Counter()
yj = Counter()
nj = Counter()
ny = Counter()
WIN_H_J = Counter()
WIN_H_Y = Counter()
WIN_A_J = Counter()
WIN_A_Y = Counter()
NULL = 0

random_mode = 1
features = [[] for ii in range(0,64)]
labels = [[] for ii in range(0,64)]
initial_year = 2008
slope_mode = 15
slope_mode_cases = [\
	[0,8],\
	[1,16],\
	[2,8],\
	[3,0],\
	[4,6],\
	[5,4],\
	[6,8],\
	[7,16],\
	[8,16],\
	[9,4],\
	[10,16],\
	[11,16], \
	[12,16],\
	[13,4], \
	[14,4],\
	[15,4]

This is Self Test

def slope(slope_0,slope_1,info_a,info_b,mode,answer):
	s00 = slope_0[0]
	s01 = slope_0[len(slope_0)/2]
	s02 = slope_0[len(slope_0)-1]
	s10 = slope_1[0]
	s11 = slope_1[len(slope_1)/2]
	s12 = slope_1[len(slope_1)-1]
	sa0 = (info_a[len(info_a)-1]/1000000) %100 -(info_a[len(info_a)-1]/10000) %100
	sma0 = (info_a[len(info_a)-1]/100) %100 -  (info_a[len(info_a)-1]/1) %100
	sa1 = (info_a[len(info_a)-5]/1000000) %100- (info_a[len(info_a)-5]/10000) %100
	sa2 = (info_a[len(info_a)-6]/1000000) %100- (info_a[len(info_a)-6]/10000) %100
	sma1 = (info_a[len(info_a)-5]/100) %100 -  (info_a[len(info_a)-5]/1) %100
	sb0 = (info_b[len(info_b)-1]/1000000) %100 -(info_b[len(info_b)-1]/10000) %100
	smb0 = (info_b[len(info_b)-1]/100) %100 -  (info_b[len(info_b)-1]/1) %100
	sb1 = (info_b[len(info_b)-5]/1000000) %100- (info_b[len(info_b)-5]/10000) %100
	sb2 = (info_b[len(info_b)-6]/1000000) %100- (info_b[len(info_b)-6]/10000) %100
	smb1 = (info_b[len(info_b)-5]/100) %100 -  (info_b[len(info_b)-5]/1) %100
	ret_value = -1
	t0 = 0
	t1 = 0
	t2 = 0
	t3 = 0
	t4 = 0
	t5 = 0
	t6 = 0
	if mode == 0:# non overlap 2x2 cases
		if s00 > s10 and s01 > s11 and s02 > s12:
			if s02-s00 > 0 and s12-s10 > 0:
				ret_value = 0
			elif s02-s00 > 0 and s12-s10 < 0:
				ret_value =  1
			elif s02-s00 < 0 and s12-s10 > 0:
				ret_value= 2
			else:
				ret_value= 3
		elif s00 < s10 and s01 < s11 and s02 < s12:
			if s02-s00 > 0 and s12-s10 > 0:
				ret_value= 4
			elif s02-s00 > 0 and s12-s10 < 0:
				ret_value= 5
			elif s02-s00 < 0 and s12-s10 > 0:
				ret_value= 6
			else:
				ret_value= 7
		else:
			ret_value -1
	elif mode == 1:# non overlap with same or different region 2x2 cases
		if s00*s10 > 0 and s01*s11 > 0 and s02*s12 > 0 and s00 > s10 and s01 > s11 and s02 > s12:
			if s02-s00 > 0 and s12-s10 > 0:
				ret_value =  0
			elif s02-s00 > 0 and s12-s10 < 0:
				ret_value =  1
			elif s02-s00 < 0 and s12-s10 > 0:
				ret_value =  2
			else:
				ret_value =  3
		elif s00*s10 > 0 and s01*s11 > 0 and s02*s12 > 0 and s00 < s10 and s01 < s11 and s02 < s12:
			if s02-s00 > 0 and s12-s10 > 0:
				ret_value =  4
			elif s02-s00 > 0 and s12-s10 < 0:
				ret_value =  5
			elif s02-s00 < 0 and s12-s10 > 0:
				ret_value =  6
			else:
				ret_value =  7
		elif s00*s10 < 0 and s01*s11 < 0 and s02*s12 < 0 and s00 > s10 and s01 > s11 and s02 > s12:
			if s02-s00 > 0 and s12-s10 > 0:
				ret_value =  8
			elif s02-s00 > 0 and s12-s10 < 0:
				ret_value =  9
			elif s02-s00 < 0 and s12-s10 > 0:
				ret_value =  10
			else:
				ret_value =  11
		elif s00*s10 < 0 and s01*s11 < 0 and s02*s12 < 0 and s00 < s10 and s01 < s11 and s02 < s12:
			if s02-s00 > 0 and s12-s10 > 0:
				ret_value =  12
			elif s02-s00 > 0 and s12-s10 < 0:
				ret_value =  13
			elif s02-s00 < 0 and s12-s10 > 0:
				ret_value =  14
			else:
				ret_value =  15
		else:
			ret_value = -1
	elif mode == 2:
		t0 = random.randint(-5,5)
		t1 = random.randint(-5,5)
		t2 = random.randint(-5,5)
		t3 = random.randint(-5,5)
		ret_value = random.randint(0,7)
	elif mode == 3:
		x0 = np.array([0.0 for ii in range(0,len(slope_0))])
		x1 = np.array([0.0 for ii in range(0,len(slope_1))])
		y0 = slope_0
		y1 = slope_1
		cnt_z0 = 0
		cnt_z1 = 0
		for poly in range(1,5):
			z0 = np.polyfit(x0,y0,poly)
			z1 = np.polyfit(x1,y1,poly)
			z0_next = np.polyval(z0,len(slope_0))
			z1_next = np.polyval(z1,len(slope_1))
			if z0_next < slope_0[len(slope_0)-1] and z1_next > slope_1[len(slope_1)-1]:
				cnt_z1 += 1
			elif z0_next > slope_0[len(slope_0)-1] and z1_next < slope_1[len(slope_1)-1]:
				cnt_z0 += 1
		if cnt_z0 < cnt_z1 :
			ret_value =  0
		elif cnt_z1 < cnt_z0 :
			ret_value =  1
		else:
			ret_value =  2
	elif mode == 4:# non overlap with same or different region 2x2 cases
		t0 = s00-s01
		t1 = s01-s02
		t2 = s10-s11
		t3 = s11-s12
		if s00 - s01 > 0 and s02 - slope_0[len(slope_0)-2] < 0:
			ret_value = 0
		elif s10 - s11 > 0 and s12 - slope_1[len(slope_1)-2] < 0:
			ret_value = 1
		elif (s01-s00) < 0 and (s02-s01)>0:
			ret_value = 2
		elif (s01-s00) > 0 and (s02-s01)<0:
			ret_value = 3
		elif (s11-s10) < 0 and (s12-s11)>0:
			ret_value = 4
		elif (s11-s10) > 0 and (s12-s11)<0:
			ret_value = 5
		pass
	elif mode == 5:
		t0 = s01-s00
		t1 = s11-s10
		slopes = 2 if s01-s00 > 0 else 0
		slopes += 1 if s11-s10 > 0 else 0
		ret_value = slopes
	elif mode == 6:
		slope_diff = np.array(slope_0)-np.array(slope_1)
		t0 = slope_diff[0]
		t1 = slope_diff[len(slope_diff)/2]
		t2 = slope_diff[len(slope_diff)-1]
		slopes = 4 if slope_diff[0] > 0 else 0
		slopes += 2 if slope_diff[len(slope_diff)/2] > 0 else 0
		slopes += 1 if slope_diff[len(slope_diff)-1] > 0 else 0
		ret_value = slopes
	elif mode == 7:
		t0 = slope_0[len(slope_0)-1]
		t1 = slope_1[len(slope_1)-1]
		t2 = slope_0[len(slope_0)-5] - slope_0[len(slope_0)-6]
		t3 = slope_1[len(slope_1)-5] - slope_1[len(slope_1)-6]
		#t4 = 1.0 if answer == "A" or answer == "T" else -1.0

		slopes = 8 if slope_0[len(slope_0)-1] > slope_1[len(slope_1)-1] else 0
		slopes += 4 if slope_0[len(slope_0)-5] > slope_1[len(slope_1)-5] else 0
		slopes += 2 if slope_0[len(slope_0)-5] - slope_0[len(slope_0)-6] > 0 else 0
		slopes += 1 if slope_1[len(slope_1)-5] - slope_1[len(slope_1)-6] > 0 else 0
		ret_value = slopes
	elif mode == 8:
		t0 = 1.0 if slope_0[len(slope_0)-5] - slope_0[len(slope_0)-6] > 0 else -1.0
		t1 = 1.0 if abs(slope_0[len(slope_0)-5] - slope_0[len(slope_0)-6]) > 2.0 else -1.0
		t2 = 1.0 if slope_1[len(slope_1)-5] - slope_1[len(slope_1)-6] > 0 else -1.0
		t3 = 1.0 if abs(slope_1[len(slope_1)-5] - slope_1[len(slope_1)-6]) > 2.0 else -1.0
		#t4 = 1.0 if answer == "a" or answer == "t" else -1.0

		slopes =  8 if t0 > 0 else 0
		slopes += 4 if t1 > 0 else 0
		slopes += 2 if t2 > 0 else 0
		slopes += 1 if t3 > 0 else 0
		ret_value = slopes
	elif mode == 9:
		t0 = slope_0[len(slope_0)-1] - slope_0[len(slope_0)-2]
		t1 = slope_0[len(slope_0)-5] - slope_0[len(slope_0)-6]
		t2 = slope_1[len(slope_1)-1] - slope_1[len(slope_1)-2]
		t3 = slope_1[len(slope_1)-5] - slope_1[len(slope_1)-6]

		#t4 = 1.0 if answer == "A" or answer == "T" else -1.0
		t0 = t0*t1
		t1 = t2*t3
		t2 = max(slope_0)*max(slope_0)
		t3 = min(slope_1)*min(slope_1)
		slopes = 2 if t0 > 0 else 0
		slopes += 1 if t1 > 0 else 0
		ret_value = slopes
	elif mode == 10:
		t0 = slope_0[len(slope_0)-1] - slope_0[len(slope_0)-2]
		t1 = slope_0[len(slope_0)-5] - slope_0[len(slope_0)-6]
		t2 = slope_1[len(slope_1)-1] - slope_1[len(slope_1)-2]
		t3 = slope_1[len(slope_1)-5] - slope_1[len(slope_1)-6]

		slopes =  8 if t0 > 0 else 0
		slopes += 4 if t1 > 0 else 0
		slopes += 2 if t2 > 0 else 0
		slopes += 1 if t3 > 0 else 0
		ret_value = slopes
	elif mode == 11:
		t2 = slope_0[len(slope_0)-1] - slope_0[len(slope_0)-6]
		t3 = slope_1[len(slope_1)-1] - slope_1[len(slope_1)-6]
		t0 = t2-t3
		t1 = slope_0[len(slope_0)-1] - slope_1[len(slope_1)-1]
		slopes =  8 if t0 > 0 else 0
		slopes += 4 if t1 > 0 else 0
		slopes += 2 if t2 > 0 else 0
		slopes += 1 if t3 > 0 else 0
		ret_value = slopes
	elif mode == 12:
		t0 = sa1
		t1 = sma0-sma1
		t2 = sb1
		t3 = smb0-smb1
		slopes =  8 if t0 >= 0 else 0
		slopes += 4 if t1 >= 0 else 0
		slopes += 2 if t2 >= 0 else 0
		slopes += 1 if t3 >= 0 else 0
		ret_value = slopes
	elif mode == 13:
		t0 = sa1
		t1 = sb1
		slopes = 2 if t0 >= 0 else 0
		slopes += 1 if t1 >= 0 else 0
		ret_value = slopes
	elif mode == 14:
		t0 = slope_0[len(slope_0)-5] - slope_0[len(slope_0)-6]
		t1 = slope_1[len(slope_1)-5] - slope_1[len(slope_1)-6]
		t2 = slope_0[len(slope_0)-1] - slope_0[len(slope_0)-2]
		t3 = slope_1[len(slope_1)-1] - slope_1[len(slope_1)-2]
		t0 = t0-t1
		t1 = t2-t3
		slopes = 2 if t0 > 0 else 0
		slopes += 1 if t1 > 0 else 0
		ret_value = slopes
	elif mode == 15:
		t0 = slope_0[len(slope_0)-1] - slope_0[len(slope_0)-6]
		t1 = slope_1[len(slope_1)-1] - slope_1[len(slope_1)-6]
		slopes = 2 if t0 > 0 else 0
		slopes += 1 if t1 > 0 else 0
		ret_value = slopes
	else:
		ret_value = -1
	if ret_value > -1:
		"""
		t0 = 1.0 if s02 > 0 else -1.0
		t1 = 1.0 if s02-s01 > 0 else -1.0
		t2 = 1.0 if s01-s00 > 0 else -1.0
		t3 = 1.0 if s12 > 0 else -1.0
		t4 = 1.0 if s12-s11 > 0 else -1.0
		t5 = 1.0 if s11-s10 > 0 else -1.0
		"""
		if slope_mode_cases[slope_mode][1] == 16:
			features[ret_value].append([t0,t1,t2,t3])
		elif slope_mode_cases[slope_mode][1] == 8:
			features[ret_value].append([t0,t1,t2])
		elif slope_mode_cases[slope_mode][1] == 4:
			features[ret_value].append([t0,t1])

		if answer == "A":
			labels[ret_value].append(0)
			#labels[ret_value].append((1.0,1.0))
		elif answer == "G":
			labels[ret_value].append(1)
			#labels[ret_value].append((1.0,-1.0))
		elif answer == "C":
			labels[ret_value].append(2)
			#labels[ret_value].append((-1.0,1.0))
		elif answer == "T":
			labels[ret_value].append(3)
			#labels[ret_value].append((-1.0,-1.0))
		else:
			labels[ret_value].append(-999)
			#labels[ret_value].append((0.0,0.0))
def data_gen():
	t = data_gen.t
	cnt = -1
	if len(line_black) < len(line_red):
		line_black.insert(0,line_black[0])
	if len(line_black) > len(line_red):
		line_red.insert(0,line_red[0])

	while cnt < max(len(line_black),len(line_red))-1:
		cnt += 1
		t += 1
		yield t , line_black[cnt],line_red[cnt]
def run(data):
	# update the data
	t,y1,y2 = data
	y3 = y1-y2
	xdata.append(t)
	ydata.append(y1)
	xdata2.append(t)
	ydata2.append(y2)
	xdata3.append(t)
	ydata3.append(y3)
	xmin, xmax = ax.get_xlim()
	ymin, ymax = ax.get_ylim()
	xx = [xdata,xdata2,xdata2]
	yy = [ydata,ydata2,ydata2]
	if y1 >= ymax or y2 >= ymax or y3 >= ymax:
		ymaxx = max(y1,y2,y3)
		ax.set_ylim(ymin, 1.2*ymaxx)
		ax.figure.canvas.draw()
	if y1 <= ymin or y2 <= ymin or y3 <= ymin:
		yminn = min(y1,y2,y3)
		ax.set_ylim(yminn*1.2,ymax)
		ax.figure.canvas.draw()
	if t >= xmax:
		ax.set_xlim(xmin, 1.3*xmax)
		ax.figure.canvas.draw()
	for lnum , line in enumerate(lines):
		line.set_data(xx[lnum], yy[lnum])
	return lines


class Kmer:
#	bp = ["H","T","A"]
#	bp = ["H","T","A","h","t","a"]
	bp = ["A","G","C","T"]
	def __init__(self):
#		self.bp = ["H","T","A"]
		pass
	def initial(self,year,kmer_num):
		self.year = year
		self.kmer_num = kmer_num
		self.Kmer = [[Counter() for ii in range(0,self.year)] for jj in range(0,self.kmer_num)]
		pass
	def insert_chromo(self,chromo_list):
		for kmer_index in range(0,self.kmer_num): # Kmer Indexes
			for year_list in range(0,len(chromo_list)): # Year List
				for c_list in range(0,len(chromo_list[year_list])): #MLB Teams 0~30
					num_kmers = len(chromo_list[year_list][c_list])-(kmer_index+2)+1
					for ii in range(num_kmers):
						self.Kmer[kmer_index][year_list]\
						[chromo_list[year_list][c_list][ii:ii + kmer_index+2]] += 1
		"""
		for kmer_index in range(0,self.kmer_num): # Kmer Indexes
			for year_list in range(0,self.year): # Year List
				pass
				print str(kmer_index+2)+"\t20"+str(year_list+initial_year-2000)
				print self.Kmer[kmer_index][year_list].most_common(20)
		"""
	def maximum_likelihood(self,chromo,kmer):
		#if kmer == 2 chromo size is 1 we estimate another character
		# find top 10 for all the year
		new_chromo=[]
		for ii in self.bp:
			new_chromo.append(chromo+ii)
#for odds score consider
#impact_factor=[0.6,0.55,0.45,0.4]

		impact_factor=[1.0 for ii in range(0,len(self.bp))]
		m_c = 0
		if kmer == 1:
			m_c = 4**(kmer+1)
		if kmer == 2:
			m_c = 15
		elif kmer == 3:
			m_c = 30
		elif kmer == 4:
			m_c = 60
		elif kmer == 5:
			m_c = 120
		elif kmer == 6:
			m_c = 240
		elif kmer == 7:
			m_c = 480
		m_c = int(4**(kmer+1)*3/4)
		result = [0.0 for ii in range(0,len(self.bp))]
		for ii in range(0,len(self.bp)): # case study for 4 characters
			for year_list in range(0,self.year):
				Temp = self.Kmer[kmer-1][year_list].most_common(m_c)
#				Temp = self.Kmer[kmer-1][year_list]
#				print Temp
				for jj in Temp:
					char,cnt = jj
					if new_chromo[ii] == char:
						#result[ii] += 1.0/impact_factor[ii]
						result[ii] += cnt*1.0/impact_factor[ii]
		#print result
		return result
	def estimate_result(self,chromo,answer):
		result = np.array([0.0 for ii in range(0,len(self.bp))])
		impact_factor = [0.7,1.5,2.0,4.0,8.0,10.0]
		return_list = []
		for ii in range(0,self.kmer_num):
			result_np = np.array(self.maximum_likelihood(chromo[len(chromo)-(ii+1):len(chromo)],ii+1))
			result += result_np*impact_factor[ii]
		if answer == "A" or answer == "T":
			if result[0] > result[3]:
				return_list.append("A")
#				return "A"
			else:
				return_list.append("T")
#				return "T"
			return_list.append(int(result[0]))
			return_list.append(int(result[3]))
		elif answer == "G" or answer == "C":
			if result[1] > result[2]:
				return_list.append("G")
#				return "G"
			else:
				return_list.append("C")
#				return "C"
			return_list.append(int(result[1]))
			return_list.append(int(result[2]))
		return return_list
		result_AG = result[0]+result[1]
		result_CT = result[2]+result[3]
		if result_CT+result_AG == 0.0:
			return "?"
		elif result_AG/(result_AG+result_CT) > 0.65:
			return "A"
		elif result_CT/(result_AG+result_CT) > 0.65:
			return "C"
		else:
			return "?"
		"""
		for jj in range(0,len(self.bp)):
			if result[jj] == max(result):
				return self.bp[jj]
		"""
fout = open("mlb_result.txt",'w')
history = Counter()
game_counter = 0
predict_predict = [0 for jj in range(0,12)]
while 1:
	game_counter += 1
	if game_counter % 10 == 9:
		print game_counter
		for kkk in range(0,4):
			print [predict_predict[kkk*2],predict_predict[kkk*2+1],predict_predict[kkk*2]/(predict_predict[kkk*2]+predict_predict[kkk*2+1]+0.00001),predict_predict[kkk+8]]
		predict_predict = [0 for jj in range(0,12)]
	if random_mode!= 3:
		data_gen.t = 0
		fig, ax = pl.subplots()
		line, = ax.plot([],[],lw=3)
		ax.set_ylim(-10, 10)
		ax.set_xlim(0, 20)
		ax.grid()
		lines = []
		plotlays, plotcols = [4],["black","red","green","yellow"]
		for index in range(3):
			lobj = ax.plot([], [], lw=3,color=plotcols[index])[0]
			lines.append(lobj)
		xdata, ydata = [], []
		xdata2,ydata2 = [], []
		xdata3,ydata3 = [], []
	if random_mode == 1:
		start = random.randint(0,2015-initial_year-1)
		end = start + 1
	else:
		if sys.argv[1] =="all":
			if random_mode == 2:
				start = 2015-initial_year
				end = 2015-initial_year+1
			else:
				start = 0
				end = 2015-initial_year+1
		else:
			start = int(sys.argv[1])-initial_year
			end = start+1

	for mlb_iter in range(start,end):
	####################################################################
		myKmer = Kmer()
		myKmer2 = Kmer()
	#year = int(sys.argv[1])-2007 # 8 is the default value
		year = mlb_iter
		myKmer.initial(2015-initial_year,4)
	#	myKmer.initial(8,4)
	####################################################################
		kmer_list_info = []
		kmer_list_list_info = []
		kmer_2015_info = []
		ch_start = 0
		ch_end = 2015-initial_year+1
		for ii in range(ch_start,ch_end):
			fin_info = open("chromo_info.txt",'r')
			while 1:
				fin_line_info = fin_info.readline()
				if not fin_line_info:
					break
				if fin_line_info.find(str(ii+initial_year-2000)) != -1 and \
								fin_line_info.find(">") != -1:
					chr_2015_info = []
					chk_2015_info = 0
					if fin_line_info.find(str(year+initial_year-2000)) != -1 and \
									fin_line_info.find(">") != -1:
						chk_2015_info = 1
						names = fin_line_info[4]
						if names == " ":
							chr_2015_info.append(fin_line_info[5:len(fin_line_info)-1])
						else:
							chr_2015_info.append(fin_line_info[4:len(fin_line_info)-1])
					fin_line_info = fin_info.readline()
					floats = map(int,fin_line_info.split())
					if chk_2015_info:
						chr_2015_info.append(floats)
						kmer_2015_info.append(chr_2015_info)
					else:
						kmer_list_info.append(floats)
					continue
			fin_info.close()
			if ii != year:
				kmer_list_list_info.append(kmer_list_info)
			kmer_list_info=[]
####################################################################
		kmer_list_opp = []
		kmer_list_list_opp = []
		kmer_2015_opp = []
		ch_start = 0
		ch_end = 2015-initial_year+1
		for ii in range(ch_start,ch_end):
			fin_opp = open("chromo_opp.txt",'r')
			while 1:
				fin_line_opp = fin_opp.readline()
				if not fin_line_opp:
					break
				if fin_line_opp.find(str(ii+initial_year-2000)) != -1 and \
					fin_line_opp.find(">") != -1:
					chr_2015_opp = []
					chk_2015_opp = 0
					if fin_line_opp.find(str(year+initial_year-2000)) != -1 and \
					fin_line_opp.find(">") != -1:
						chk_2015_opp = 1
						names = fin_line_opp[4]
						if names == " ":
							chr_2015_opp.append(fin_line_opp[5:len(fin_line_opp)-1])
						else:
							chr_2015_opp.append(fin_line_opp[4:len(fin_line_opp)-1])
					fin_line_opp = fin_opp.readline()
					floats = map(int,fin_line_opp.split())
					if chk_2015_opp:
						chr_2015_opp.append(floats)
						kmer_2015_opp.append(chr_2015_opp)
					else:
						kmer_list_opp.append(floats)
					continue
			fin_opp.close()
			if ii != year:
				kmer_list_list_opp.append(kmer_list_opp)
			kmer_list_opp=[]
	###################################################################
		kmer_list_odds = []
		kmer_list_list_odds = []
		kmer_2015_odds = []
		for ii in range(ch_start,ch_end):
			fin_odds = open("chromo_odds.txt",'r')
			while 1:
				fin_line_odds = fin_odds.readline()
				if not fin_line_odds:
					break
				if fin_line_odds.find(str(ii+initial_year-2000)) != -1 and \
					fin_line_odds.find(">") != -1:
					chr_2015_odds = []
					chk_2015_odds = 0
					if fin_line_odds.find(str(year+initial_year-2000)) != -1 and \
					fin_line_odds.find(">") != -1:
						chk_2015_odds = 1
						names = fin_line_odds[4]
						if names == " ":
							chr_2015_odds.append(fin_line_odds[5:len(fin_line_odds)-1])
						else:
							chr_2015_odds.append(fin_line_odds[4:len(fin_line_odds)-1])
					fin_line_odds = fin_odds.readline()
					floats = map(float,fin_line_odds.split())
					if chk_2015_odds:
						chr_2015_odds.append(floats)
						kmer_2015_odds.append(chr_2015_odds)
					else:
						kmer_list_odds.append(floats)
					continue
			fin_odds.close()
			if ii != year:
				kmer_list_list_odds.append(kmer_list_odds)
			kmer_list_odds=[]
	###################################################################
		kmer_list = []
		kmer_list_list = []
		kmer_2015 = []
		for ii in range(ch_start,ch_end):
			fin = open("chromo.txt",'r')
			while 1:
				fin_line = fin.readline()
				if not fin_line:
					break
				if fin_line.find(str(ii+initial_year-2000)) != -1 and\
				   fin_line.find(">") != -1:
					chr_2015 = []
					chk_2015 = 0
					if fin_line.find(str(year+initial_year-2000)) != -1 and \
					   fin_line.find(">") != -1:
						chk_2015 = 1
						names = fin_line[4]
						if names == " ":
							chr_2015.append(fin_line[5:len(fin_line)-1])
						else:
							chr_2015.append(fin_line[4:len(fin_line)-1])
					fin_line = fin.readline()
					if chk_2015:
						chr_2015.append(fin_line[0:len(fin_line)-1])
						kmer_2015.append(chr_2015)
					else:
						kmer_list.append(fin_line[0:len(fin_line)-1])
					continue
			fin.close()
			if ii != year:
				kmer_list_list.append(kmer_list)
			kmer_list=[]
	###################################################################
		myKmer.insert_chromo(kmer_list_list)
	###################################################################
		win_AT = 0.0
		lose_AT = 0.0
		win_GC = 0.0
		lose_GC = 0.0

		win_A=0.0
		win_T=0.0
		win_G=0.0
		win_C=0.0
		diff_AG=0.0
		diff_CT=0.0
		lose_A=0.0
		lose_G=0.0
		lose_C=0.0
		lose_T=0.0
		yes=0.0
		no=0.0
		offset = 10 #7 is the last element we should increase number
		offset = 7 #7 is the last element we should increase number
		chk = 0
	#"""
		h_win_A = Counter()
		h_win_G = Counter()
		h_win_C = Counter()
		h_win_T = Counter()
		h_diff_A = Counter()
		h_diff_G = Counter()
		h_diff_C = Counter()
		h_diff_T = Counter()
		h_lose_A = Counter()
		h_lose_G = Counter()
		h_lose_C = Counter()
		h_lose_T = Counter()
		h_opp = Counter()
	#############################################################
		if random_mode:
			for_rand = random.randint(0,len(kmer_2015)-1)
		else:
			pass
			for_rand = 0
			features = [[] for ii in range(0,64)]
			labels = [[] for ii in range(0,64)]
	#############################################################
		for ii in range(for_rand,len(kmer_2015)):
			name,chromo = kmer_2015[ii]
			name_f,chromo_f = kmer_2015_odds[ii]
			name_o,chromo_o = kmer_2015_opp[ii]
			name_i,chromo_i = kmer_2015_info[ii]
			if int(sys.argv[2])==1:
				start = len(chromo)-offset
			else:
				start = 0
			if random_mode:
				if random_mode == 1:
					start = random.randint(0,len(chromo)-offset-30)
					end = len(chromo)-offset+1
				elif random_mode == 2:
					start = len(chromo)-offset
					end = len(chromo)-offset+1
				elif random_mode == 3:
					start = random.randint(0,len(chromo)-offset-30)
					end = start+10
			else:
				start = 0
				end = len(chromo)-offset+1
			for jj in range(start,end):
				predict_a_list = myKmer.estimate_result(chromo[jj:jj+offset-1],chromo[jj+offset-1])
				opp_nid = chromo_o[jj+offset-1] % 100
				opp_game_name = chromo_o[jj+offset-1]/100
				name_opp,chromo_opp = kmer_2015[opp_nid]
				name_opp_odds,chromo_opp_odds = kmer_2015_odds[opp_nid]
				name_info_odds,chromo_opp_info = kmer_2015_info[opp_nid]
				predict_b_list = myKmer.estimate_result(chromo_opp[opp_game_name-offset+1:opp_game_name],chromo_opp[opp_game_name])
				predict_a = predict_a_list[0]
				predict_b = predict_b_list[0]
				if random_mode == 3:
#					if chromo_f[jj+offset-1] > 1.55 and chromo_f[jj+offset-1] < 2.6:
					if 1:
						if predict_a=="A" and predict_b=="C":
							if chromo[jj+offset-1] == "A":
								predict_predict[0]+=1
								predict_predict[8]+=chromo_f[jj+offset-1]-1
							else:
								predict_predict[1]+=1
								predict_predict[8]-=1
						elif predict_a=="C"and predict_b=="T":
							if chromo[jj+offset-1] == "G":
								predict_predict[2]+=1
								predict_predict[9]+=chromo_f[jj+offset-1]-1
							else:
								predict_predict[3]+=1
								predict_predict[9]-=1
						elif predict_a=="C" and predict_b=="A":
							if chromo_opp[opp_game_name] == "A":
								predict_predict[4]+=1
								predict_predict[10]+=chromo_opp_odds[opp_game_name]-1
							else:
								predict_predict[5]+=1
								predict_predict[10]-=1
						elif predict_a=="T"and predict_b=="C":
							if chromo_opp[opp_game_name] == "G":
								predict_predict[6]+=1
								predict_predict[11]+=chromo_opp_odds[opp_game_name]-1
							else:
								predict_predict[7]+=1
								predict_predict[11]-=1
				elif random_mode==1 or random_mode==2:
					print ("Year: %d Game Number: %d %s %s %s %s")%(mlb_iter+initial_year,jj+offset-1,name_f,name_opp_odds,chromo[jj+offset-1],chromo_opp[opp_game_name])
					if chromo[jj+offset-1] == "A" or chromo[jj+offset-1] == "T":
						ax.set_title("Predict: "+str(predict_a_list)+" "+str(predict_b_list)+"  Home win J or lose Y\nPrevious 5 games "+chromo[jj+offset-1-5] +" and "+ chromo_opp[opp_game_name-5])
					else:
						ax.set_title("Predict: "+str(predict_a_list)+" "+str(predict_b_list)+"  Home win Y or lose J\nPrevious 5 games "+chromo[jj+offset-1-5] +" and "+ chromo_opp[opp_game_name-5])
					line_black = chromo_f[jj:jj+offset-1]
					if opp_game_name > offset-2:
						line_red = chromo_opp_odds[opp_game_name-offset+1:opp_game_name]
					else:
						line_red = chromo_opp_odds[0:opp_game_name]
					ani = animation.FuncAnimation(fig, run, data_gen, blit=True, interval=10,repeat=False)
					plt.show()
					break
				else :
					point_a = chromo_f[jj:jj+offset-1]
					info_a = chromo_i[jj:jj+offset-1]
					if opp_game_name > offset-2:
						point_b = chromo_opp_odds[opp_game_name-offset+1:opp_game_name]
						info_b = chromo_opp_info[opp_game_name-offset+1:opp_game_name]
					else:
						point_b = chromo_opp_odds[0:opp_game_name]
						info_b = chromo_opp_info[0:opp_game_name]
						for add in range(0,len(point_a)-len(point_b)):
							point_b.insert(add,chromo_opp_odds[0])
							info_b.insert(add,chromo_opp_info[0])
		#######################################################################
		########################################################################
		########################################################################
					predict_jj = slope(point_a,point_b,info_a,info_b,slope_mode,chromo[jj+offset-1])
			if random_mode:
				break
		#			predict_jj = -1
		########################################################################
		if random_mode != 3:
			print mlb_iter+initial_year
			print "----------------------"
			yes_j_total = 0.0
			yes_y_total = 0.0
			no_j_total = 0.0
			no_y_total = 0.0
			hh = 0.0
			aa = 0.0
			learner_mode = 0
			for feature_ii in range(0,slope_mode_cases[slope_mode][1]):
				len_train = len(features[feature_ii])
				if len_train < 5:
					continue
				if learner_mode == 0:
					weak = milk.supervised.tree.stump_learner()
					learner = milk.supervised.adaboost.boost_learner(weak)
					learner = milk.supervised.multi.one_against_one(learner)
				else:
					learner = milk.defaultclassifier()
					learner = milk.supervised.defaultclassifier()
				cmat,names,predictions = milk.nfoldcrossvalidation(features[feature_ii][0:len_train/2],labels[feature_ii][0:len_train/2],classifier=learner,return_predictions=True)
				colors = "rgby"
				codes = "xo"
				T0 = []
				T1 = []
				L0 = []
				for kk in range(0,len(features[feature_ii])):
					kk0,kk1 = features[feature_ii][kk]
					L0.append(labels[feature_ii][kk])
					T0.append(kk0)
					T1.append(kk1)
				for y,x,r,p in zip(T0,T1,labels[feature_ii],predictions):
					if ( r + p < 2 or ( r == 1 and p == 1)) or \
					   ( r + p > 4 or ( r == 2 and p == 2)):
						code = codes[1]
					else:
						code = codes[0]
					code = codes[1]
					plt.plot([y],[x],colors[r/2]+code)
				ax.set_title(feature_ii)
				plt.show()
				model = learner.train(np.array(features[feature_ii][0:len_train/2]),np.array(labels[feature_ii][0:len_train/2]))
				yes_j = 0.0
				yes_y = 0.0
				no_j = 0.0
				no_y = 0.0
				select = 1
				lists = []
				for feature_jj in range(len_train/2,len_train):
					win_lose = model.apply(features[feature_ii][feature_jj])
					lists.append(win_lose)
					label_0 = labels[feature_ii][feature_jj]
					if select == 2:
						if (label_0 == 0 and (win_lose == 0 )) or \
						   (label_0 == 2 and (win_lose == 2 )):
							yes_j += 1.0
							yes_j_total += 1.0
							if label_0 == 0:
								hh += 1.0
							else:
								aa += 1.0
						elif(label_0 == 1 and (win_lose == 1)) or \
							(label_0 == 3 and (win_lose == 3)):
							yes_y += 1.0
							yes_y_total += 1.0
						elif(label_0 == 0 and (win_lose == 3)) or \
							(label_0 == 2 and (win_lose == 1)):
							no_j += 1.0
							no_j_total += 1.0
						elif(label_0 == 1 and (win_lose == 2)) or \
							(label_0 == 3 and (win_lose == 0)):
							no_y += 1.0
							no_y_total += 1.0
					if select == 1:
						if (label_0 == 0 and (win_lose == 0 or win_lose == 1)) or \
						   (label_0 == 2 and (win_lose == 2 or win_lose == 3)):
							yes_j += 1.0
							yes_j_total += 1.0
							if label_0 == 0:
								hh += 1.0
							else:
								aa += 1.0
						elif(label_0 == 1 and (win_lose == 0 or win_lose == 1)) or \
							(label_0 == 3 and (win_lose == 2 or win_lose == 3)):
							yes_y += 1.0
							yes_y_total += 1.0
						elif(label_0 == 0 and (win_lose == 2 or win_lose == 3)) or \
							(label_0 == 2 and (win_lose == 0 or win_lose == 1)):
							no_j += 1.0
							no_j_total += 1.0
						elif(label_0 == 1 and (win_lose == 2 or win_lose == 3)) or \
							(label_0 == 3 and (win_lose == 0 or win_lose == 1)):
							no_y += 1.0
							no_y_total += 1.0
					else:
						if (label_0 == 0 and (win_lose == 0 or win_lose == 2)) or \
						   (label_0 == 2 and (win_lose == 2 or win_lose == 0)):
							yes_j += 1.0
							yes_j_total += 1.0
							if label_0 == 0:
								hh += 1.0
							else:
								aa += 1.0
						elif(label_0 == 1 and (win_lose == 3 or win_lose == 1)) or \
							(label_0 == 3 and (win_lose == 1 or win_lose == 3)):
							yes_y += 1.0
							yes_y_total += 1.0
						elif(label_0 == 0 and (win_lose == 1 or win_lose == 3)) or \
							(label_0 == 2 and (win_lose == 1 or win_lose == 3)):
							no_j += 1.0
							no_j_total += 1.0
						elif(label_0 == 1 and (win_lose == 0 or win_lose == 2)) or \
							(label_0 == 3 and (win_lose == 0 or win_lose == 2)):
							no_y += 1.0
							no_y_total += 1.0
				#print ("%d win J %.3f %.3f %.3f")%(feature_ii,yes_j,no_y,yes_j/(yes_j+no_y+0.000001))
				#print ("%d win Y %.3f %.3f %.3f")%(feature_ii,yes_y,no_j,yes_y/(yes_y+no_j+0.000001))
				yj[feature_ii] += yes_j
				yy[feature_ii] += yes_y
				nj[feature_ii] += no_j
				ny[feature_ii] += no_y
				#print ("%d\t%.3f\t%.3f\t%.3f")%(feature_ii,yes_j,no_y,yes_j/(yes_j+no_y+0.000001))
				#print ("%d\t%.3f\t%.3f\t%.3f")%(feature_ii,yes_y,no_j,yes_y/(yes_y+no_j+0.000001))
	#		print kmer_2015_info
	#		print len(lists)
			chk0 = yes_j_total + no_y_total
			chk1 = yes_y_total + no_j_total
			if chk0 == 0:
				print ("Total Win_J ")
			else:
				print ("Total Win_J %.3f %.3f %.3f")%(yes_j_total,no_y_total,yes_j_total/(yes_j_total+no_y_total))
			if chk1 == 0:
				print ("Total Win_Y ")
			else:
				print ("Total Win_Y %.3f %.3f %.3f")%(yes_y_total,no_j_total,yes_y_total/(yes_y_total+no_j_total))
			if chk0 + chk1 == 0:
				print ("Home Away Total")
			else:
				print ("Home %.3f Away %.3f Total %.3f")%(hh,aa,(yes_y_total+yes_j_total)/(yes_y_total+yes_j_total+no_y_total+no_j_total))
			#			matrix,names = milk.nfoldcrossvalidation(np.array(features[feature_ii]),np.array(labels[feature_ii]))
			#			print 'Accuracy:', matrix.trace()/float(matrix.sum())
			print "----------------------"
for f_ii in range(0,slope_mode_cases[slope_mode][1]):
	print("%d\t%d\t%.3f\t%.3f\t%.3f")%( feature_ii,f_ii,yj[f_ii]/(yj[f_ii]+ny[f_ii]+0.00001),yy[f_ii]/(yy[f_ii]+nj[f_ii]+0.00001),(yj[f_ii]+yy[f_ii])/(yj[f_ii]+yy[f_ii]+ny[f_ii]+nj[f_ii]+0.0001))
		########################################################################
		########################################################################
	##########################################################
