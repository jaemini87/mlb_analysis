# /usr/bin/python
import random
import datetime

import numpy as np
import pykov
from game_bank import Games
from Team import Team2
from Team import Team3
from Team import Get_Nid
import sys
class Bank():
	Name = "Jaemin"
	Budjet = 1000.0
	Winmoney = 10.0

	def __init__(self, name, money):
		self.Name = name
		self.Budjet = money

	def set_Winmoney(self, money):
		self.Winmoney = money

	def get_Winmoney(self):
		return self.Winmoney

	def get_Budjet(self):
		return self.Budjet

	def print_name(self):
		print(self.Name)

	def print_Budjet(self):
		print(self.Budjet)

	def payout(self, bet_money):
		self.Budjet -= bet_money

	def buyin(self, money_in):
		self.Budjet += money_in

fout = open("chromo.txt",'w')
fout_odds = open("chromo_odds.txt",'w')
fout_opp = open("chromo_opp.txt",'w')
fout_info = open("chromo_info.txt",'w')
class Analyzer():
#	def __init__(self, chromo, MLB_File_List, exec_data, output_data, mode,cali):
	def __init__(self, chromo, mlb_year, exec_data, output_data, mode,cali,kmer,start_year):
		self.mode = mode
		self.cali = cali
		self.kmer = kmer
		self.win_h = 0.0
		self.win_a = 0.0
		self.lose_h = 0.0
		self.lose_a = 0.0
		self.start_year = start_year
		self.exec_data = exec_data
		self.output_data = output_data
		self.chromo = chromo
		self.T_entropy = 0.0
		self.T_steady = 0.0
		self.win_ratio = 0.0
		self.win_cnt = 0.0
		self.T_succ_b = [ [0 for ii in range(0,4)] for jj in range(0,5)]
		self.walk_list = []
		str_ii = "0"+str(mlb_year) if mlb_year < 10 else str(mlb_year)
		mlb_update_file = today.strftime("mlb20" +str_ii+ ".txt.mid.rev")
		self.mlb_year = mlb_year
		self.MLB_File_List = mlb_update_file
		self.MLB_Team_List = []
		self.MLB_Team_List.append(Team3("Baltimore Orioles"))
		self.MLB_Team_List.append(Team3("Boston Red Sox"))
		self.MLB_Team_List.append(Team3("Chicago White Sox"))
		self.MLB_Team_List.append(Team3("Cleveland Indians"))
		self.MLB_Team_List.append(Team3("Detroit Tigers"))
		self.MLB_Team_List.append(Team3("Houston Astros"))
		self.MLB_Team_List.append(Team3("Kansas City Royals"))
		self.MLB_Team_List.append(Team3("Los Angeles Angels"))
		self.MLB_Team_List.append(Team3("Minnesota Twins"))
		self.MLB_Team_List.append(Team3("New York Yankees"))
		self.MLB_Team_List.append(Team3("Oakland Athletics"))
		self.MLB_Team_List.append(Team3("Seattle Mariners"))
		self.MLB_Team_List.append(Team3("Tampa Bay Rays"))
		self.MLB_Team_List.append(Team3("Texas Rangers"))
		self.MLB_Team_List.append(Team3("Toronto Blue Jays"))
		self.MLB_Team_List.append(Team3("Arizona Diamondbacks"))
		self.MLB_Team_List.append(Team3("Atlanta Braves"))
		self.MLB_Team_List.append(Team3("Chicago Cubs"))
		self.MLB_Team_List.append(Team3("Cincinnati Reds"))
		self.MLB_Team_List.append(Team3("Colorado Rockies"))
		self.MLB_Team_List.append(Team3("Los Angeles Dodgers"))
		self.MLB_Team_List.append(Team3("Miami Marlins"))
		self.MLB_Team_List.append(Team3("Milwaukee Brewers"))
		self.MLB_Team_List.append(Team3("New York Mets"))
		self.MLB_Team_List.append(Team3("Philadelphia Phillies"))
		self.MLB_Team_List.append(Team3("Pittsburgh Pirates"))
		self.MLB_Team_List.append(Team3("San Diego Padres"))
		self.MLB_Team_List.append(Team3("San Francisco Giants"))
		self.MLB_Team_List.append(Team3("St.Louis Cardinals"))
		self.MLB_Team_List.append(Team3("Washington Nationals"))
		self.MinBudjet_Avg = 0.0
		self.MaxBudjet_Avg = 0.0
		self.EndBudjet_Avg = 0.0
		self.Odds_ratio = 0.0

	def Fitness(self):
		Budjet = 200.0
		Winmoney = Budjet / 20
		Jaemin = Bank("Jaemin", Budjet)
		Jaemin.set_Winmoney(Winmoney)
#		fin = open("mlb2015.txt", 'r')
		fin = open(self.MLB_File_List, 'r')
		TrainCount = 0
		#TrainStart = random.randint(0,1000)
		ExecStart = 1
		ExecDurat = 20004
		UpdateNum = 1
		TrainStart = 1
		TrainEnd = 20000 if self.cali == 0 else 20000
		#random.randint(1,1300)
		DayCount = 0
		yes = 0
		no = 0
		odds_pre = []
		score_pre = []
		odds_cur = []
		score_cur = []
		mode = 0
		cur_time = 0
		cali = 0
		collect_money_hist=[]
		kmercnt = 1
		while 1:
			pre_time = cur_time
			fin_line = fin.readline()
			TrainCount += 1
			if not fin_line:
				break
			if TrainCount < TrainStart:
				continue
			if UpdateNum>3:
				break
			if TrainCount > TrainEnd:
				break
			if DayCount > ExecDurat*UpdateNum+ExecStart:
				new_walk_list = self.walk_list[ExecDurat:len(self.walk_list)]
				self.walk_list = []
				self.walk_list = new_walk_list
				UpdateNum += 1
				continue
			if fin_line.find('\014') != -1:
				TrainCount -= 1
				continue
			if fin_line.find("canc") != -1:
				TrainCount -= 1
				continue
			if fin_line.find("- -") != -1:
				TrainCount -= 1
				continue
			if fin_line.find("post") != -1:
				TrainCount -= 1
				continue
			if fin_line.find("2007") != -1 or fin_line.find("2008") != -1 or\
				fin_line.find("2009") != -1 or fin_line.find("2010") != -1 or \
				fin_line.find("2011") != -1 or fin_line.find("2012") != -1 or \
				fin_line.find("2013") != -1 or fin_line.find("2014") != -1 or\
				fin_line.find("2015") != -1:
				TrainCount -= 1
				continue
######################################################################################################
			cur_time = int(fin_line[0:2])
			dash = fin_line.find("-")
			endname = max(fin_line.rfind("s"), fin_line.rfind("x"), fin_line.rfind("p"))
			colon = fin_line.find(":")
			endcolon = fin_line.rfind(":")
			score_h = fin_line[endcolon - 2:endcolon]
			score_a = fin_line[endcolon + 1:endcolon + 3]
			scorediff = int(score_h) - int(score_a)
			sharp = fin_line.find("#")
			enddot = fin_line[0:sharp].rfind(".")
			endplus = fin_line.rfind("+")
			endminus = fin_line.rfind("-")
			endslash = fin_line.rfind("/")
			slash = fin_line.find("/")
			bet_luck = 1
			endpl = max(endplus, endminus)
			hometeam  = fin_line[6:dash-1]
			awayteam  = fin_line[dash+2:endname+1]
			if sharp == -1:
				over_under = [7.5,1.9,1.9,0,0]
			else:
				over_under = map(float,fin_line[sharp+1:len(fin_line)].split())
			if fin_line.count(".") > 4 and sharp != -1 or (fin_line.count(".") > 1 and sharp == -1):
				odds_h = float(fin_line[enddot - 7:enddot - 2])
				odds_a = float(fin_line[enddot - 2:enddot + 3])
			elif fin_line.count("+") + fin_line.count("-") > 1:
				if fin_line[endpl - 5] == '+':
					odds_h = 1.0 + int(fin_line[endpl - 4:endpl - 1]) / 100.0
				elif fin_line[endpl - 5] == '-':
					odds_h = 1.0 + 100.0 / int(fin_line[endpl - 4:endpl - 1])
				if fin_line[endpl] == '+':
					odds_a = 1.0 + int(fin_line[endpl + 1:endpl + 4]) / 100.0
				elif fin_line[endpl] == '-':
					odds_a = 1.0 + 100.0 / int(fin_line[endpl + 1:endpl + 4])
			else:
				odds_h_denom = 0
				odds_h_nom = 0
				for ii in range(3):
					odds_h_t = fin_line[slash - 1 - ii:slash]
					odds_h_tt = fin_line[slash + 1:slash + 2 + ii]
					odds_a_t = fin_line[endslash - 1 - ii:endslash]
					odds_a_tt = fin_line[endslash + 1:endslash + 2 + ii]
					if odds_h_t.isdigit() == 1:
						odds_h_denom = odds_h_t
					if odds_h_tt.isdigit() == 1:
						odds_h_nom = odds_h_tt
					if odds_a_t.isdigit() == 1:
						odds_a_denom = odds_a_t
					if odds_a_tt.isdigit() == 1:
						odds_a_nom = odds_a_tt
				odds_h = 1.0 + int(odds_h_denom) * 1.0 / int(odds_h_nom)
				odds_a = 1.0 + int(odds_a_denom) * 1.0 / int(odds_a_nom)

			score_diff = int(score_h)-int(score_a)
			score_offset = min(int(score_h),int(score_a))
			game_now = [int(score_h),int(score_a),odds_h,odds_a]
			game_now_h = [score_diff,score_offset,odds_h,odds_a]
			game_now_a = [score_diff,score_offset,odds_a,odds_h]
			kmercnt += 1
######################update chromo and chromo_odds information#######
			team_check = 2
			mode = 8
			for mlb_team_itr in self.MLB_Team_List:
				if mlb_team_itr.get_Name() == hometeam:
					#mlb_team_itr.set_chromo(game_now,over_under,1,int(sys.argv[1]))
					mlb_team_itr.set_chromo(game_now,over_under,1,mode)
					team_check -= 1
				elif mlb_team_itr.get_Name() == awayteam:
					#mlb_team_itr.set_chromo(game_now,over_under,0,int(sys.argv[1]))
					mlb_team_itr.set_chromo(game_now,over_under,0,mode)
					team_check -= 1
			if team_check != 0:
				continue
###############End of update chromo and chromo_odds information#######
			
######################update chromo_opp information###################
			team_check = 2
			for mlb_team_itr in self.MLB_Team_List:
				if mlb_team_itr.get_Name() == hometeam:
					away_nid = Get_Nid(awayteam)
					away_game_num = self.MLB_Team_List[away_nid].get_game_num()
					mlb_team_itr.set_chromo_opp(away_nid,away_game_num)
					team_check -= 1
				elif mlb_team_itr.get_Name() == awayteam:
					home_nid = Get_Nid(hometeam)
					home_game_num = self.MLB_Team_List[home_nid].get_game_num()
					mlb_team_itr.set_chromo_opp(home_nid,home_game_num)
					team_check -= 1
			if team_check != 0:
				continue
##################End of chromo_opp information#######################

		#print("yes:%d\tno:%d=%.3f"%(yes,no,yes*1.0/(yes+no+0.00001)))
		#return Jaemin.get_Budjet()
#"""
		for mlb_team_itr in self.MLB_Team_List:
			fout.write("> "+str(self.mlb_year)+" "+mlb_team_itr.get_Name()+"\n")
			myChromo = mlb_team_itr.get_chromo()
			for ii in myChromo:
				fout.write(ii)
			fout.write("\n")
#"""
		for mlb_team_itr in self.MLB_Team_List:
			fout_odds.write("> "+str(self.mlb_year)+" "+mlb_team_itr.get_Name()+"\n")
			myChromo_odds = mlb_team_itr.get_chromo_odds()
			for ii in myChromo_odds:
				ii = int(ii*1000)*1.0/1000.0
				fout_odds.write(str(ii)+" ")
			fout_odds.write("\n")
		
		for mlb_team_itr in self.MLB_Team_List:
			fout_opp.write("> "+str(self.mlb_year)+" "+mlb_team_itr.get_Name()+"\n")
			myChromo_opp = mlb_team_itr.get_chromo_opp()
			for ii in myChromo_opp:
				fout_opp.write(str(ii)+" ")
			fout_opp.write("\n")

		for mlb_team_itr in self.MLB_Team_List:
			fout_info.write("> "+str(self.mlb_year)+" "+mlb_team_itr.get_Name()+"\n")
			myChromo_info = mlb_team_itr.get_chromo_info()
			for ii in myChromo_info:
				fout_info.write(str(ii)+" ")
			fout_info.write("\n")

		return [self.win_ratio,self.win_cnt,Jaemin.get_Budjet()]

ii = 11
c15 = [0]
today = datetime.date.today()
mlb_pick_file = ""
mlb_upcoming_file = ""

np.set_printoptions(precision=3)
average = []
cali = 0
iters = 1
Budjet = 0.0
LastBudjet = 200.0
win_ratio = 0.0
win_cnt = 0.0
Result = []
"""
start_year = 7
end_year = start_year + 8
"""
start_year = 8
end_year = start_year + 7
kmer = 3
#year_list = []
for jj in range(0,iters):
	for ii in range(start_year,end_year+1):
	#for ii in year_list:
		#cali = 1 if ii == end_year else 0
		str_ii = "0" + str(ii) if ii < 10 else str(ii)
		mlb_update_file = today.strftime("mlb20" +str_ii+ ".txt")
		mlb_year = ii
		myAnalyzer = Analyzer(c15, mlb_year,jj, mlb_pick_file, 1,cali,kmer,start_year)
		Result = myAnalyzer.Fitness()
		"""
		if max(Budjet,LastBudjet)-min(Budjet,LastBudjet)<100:
			cali = abs(3-cali)
		"""
		#print Budjet
		#LastBudjet = Budjet
		#average.append(Budjet -200)
win_ratio, win_cnt,myBudjet = Result
output = win_ratio / win_cnt if win_cnt > 0 else 0
print "Finished"
#TODO List:
#for gathering information, make sure all the year average ratio is above 0.5 or below 0.5
#Then, we only get those information and put it into storage
#print sum(average)/len(average)
#myGame.Print_Info(3)
print("------------------")
#print np.std(average)
#print T_succ_b_w
#print T_succ_b_l
fout_odds.close()
fout_opp.close()
fout_info.close()
fout.close()
