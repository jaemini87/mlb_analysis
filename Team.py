#!/usr/bin/python
import random
import os
import numpy as np
import time
import sys
def Get_Nid(name):
	if name == "Baltimore Orioles":
		return 0
	elif name == "Boston Red Sox":
		return 1
	elif name == "Chicago White Sox":
		return 2
	elif name == "Cleveland Indians":
		return 3
	elif name == 	"Detroit Tigers":
		return 4
	elif name == "Houston Astros":
		return 5
	elif name == "Kansas City Royals":
		return 6
	elif name == "Los Angeles Angels":
		return 7
	elif name == "Minnesota Twins":
		return 8
	elif name == "New York Yankees":
		return 9
	elif name == "Oakland Athletics":
		return 10
	elif name == "Seattle Mariners":
		return 11
	elif name == "Tampa Bay Rays":
		return 12
	elif name == "Texas Rangers":
		return 13
	elif name == "Toronto Blue Jays":
		return 14
	elif name == "Arizona Diamondbacks":
		return 15
	elif name == "Atlanta Braves":
		return 16
	elif name == "Chicago Cubs":
		return 17
	elif name == "Cincinnati Reds":
		return 18
	elif name == "Colorado Rockies":
		return 19
	elif name == "Los Angeles Dodgers":
		return 20
	elif name == "Miami Marlins":
		return 21
	elif name == "Milwaukee Brewers":
		return 22
	elif name == "New York Mets":
		return 23
	elif name == "Philadelphia Phillies":
		return 24
	elif name == "Pittsburgh Pirates":
		return 25
	elif name == "San Diego Padres":
		return 26
	elif name == "San Francisco Giants":
		return 27
	elif name == "St.Louis Cardinals":
		return 28
	elif name == "Washington Nationals":
		return 29
	else:
		return -1

class Team3():
	Name=""
	odds_record_interval = 10
	record_const = 10
	score_mid = 3
	score_tight = 1
	odds_mid = 1.92
	odds_low = 1.60
	odds_high= 2.55
	s_n = 0
	s_nn = ""
	game_list = []
	nid = 0
	def __init__(self,name):
		self.Name = name
		self.score_w_w_h = []
		self.score_w_w_a = []
		self.score_w_t_h = []
		self.score_w_t_a = []
		self.score_w_m_h = []
		self.score_w_m_a = []
		self.score_l_w_h = []
		self.score_l_w_a = []
		self.score_l_t_h = []
		self.score_l_t_a = []
		self.score_l_m_h = []
		self.score_l_m_a = []
		self.win_j_h  = []
		self.win_y_h   = []
		self.lose_j_h = []
		self.lose_y_h  = []
		self.win_j_a  = []
		self.win_y_a   = []
		self.lose_j_a = []
		self.lose_y_a  = []
		self.odds_record = []
		self.score_home_hist = []
		self.score_away_hist = []
		self.odds_home_hist = []
		self.odds_away_hist = []
		self.game_list = []
		self.chromo = []
		self.chromo_odds = []
		self.chromo_opp = []
		self.chromo_info = []
		self.nid = 0
	def initial(self):
		self.score_w_w_h = []
		self.score_w_w_a = []
		self.score_w_t_h = []
		self.score_w_t_a = []
		self.score_w_m_h = []
		self.score_w_m_a = []
		self.score_l_w_h = []
		self.score_l_w_a = []
		self.score_l_t_h = []
		self.score_l_t_a = []
		self.score_l_m_h = []
		self.score_l_m_a = []
		self.win_j_h  = []
		self.win_y_h   = []
		self.lose_j_h = []
		self.lose_y_h  = []
		self.win_j_a  = []
		self.win_y_a   = []
		self.lose_j_a = []
		self.lose_y_a  = []
		self.odds_record = []
		self.score_home_hist = []
		self.score_away_hist = []
		self.odds_home_hist = []
		self.odds_away_hist = []
		self.s_n = 0
		self.s_nn = ""
	def set_chromo_info(self,game_info):
		self.chromo_info.append(game_info)
	def get_chromo_info(self):
		return self.chromo_info
	def set_chromo_opp(self,nid,game_num):
		self.chromo_opp.append(game_num*100+nid)
	def get_chromo_opp(self):
		return self.chromo_opp
	def get_game_num(self):
		return len(self.chromo)-1
	def set_chromo(self,game,over_under,homeaway,mode):
		ou,over,under,score_mid_h,score_mid_a = over_under
		score_h,score_a,odds_h,odds_a = game
		if mode == 0:
			odds_cali = 0.0
			if score_h > score_a :
				if score_h-score_a > (score_mid_h-score_mid_a):
					self.chromo.append('A')
					self.chromo_odds.append(1.0)
				else:
					self.chromo.append('G')
					self.chromo_odds.append(2.0)
			else:
				if score_a-score_h  > (score_mid_a-score_mid_h):
					self.chromo.append('C')
					self.chromo_odds.append(3.0)
				else:
					self.chromo.append('T')
					self.chromo_odds.append(4.0)
		elif mode == 1:
			odds_cali = 0.0
			if score_h-1 > score_a :
				if score_a-score_mid_a < 1:
					self.chromo.append('A')
					self.chromo_odds.append(1.0)
				else:
					self.chromo.append('G')
					self.chromo_odds.append(2.0)
			else:
				if score_a-score_h < 2:
					self.chromo.append('C')
					self.chromo_odds.append(3.0)
				else:
					self.chromo.append('T')
					self.chromo_odds.append(4.0)
		elif mode == 2:
			odds_cali = 0.0
			if score_h > score_a :
				if score_a - score_mid_a < 1:
					self.chromo.append('A')
					self.chromo_odds.append(1.0)
				else:
					self.chromo.append('G')
					self.chromo_odds.append(2.0)
			else:
				if score_h - score_mid_h < 2:
					self.chromo.append('C')
					self.chromo_odds.append(3.0)
				else:
					self.chromo.append('T')
					self.chromo_odds.append(4.0)
		elif mode == 3:
			self.chromo.append('A')
			if len(self.chromo_odds)>0:
				last_value = self.chromo_odds[len(self.chromo_odds)-1]
			else:
				last_value = 0
			if homeaway == 1:
				if score_h > score_a:
					self.chromo_odds.append((odds_a+odds_h)/odds_a/2.0+last_value)
				else:
					self.chromo_odds.append(-(odds_a+odds_h)/odds_h/2.0+last_value)
			else:
				if score_a > score_h:
					self.chromo_odds.append((odds_a+odds_h)/odds_h/2.0+last_value)
				else:
					self.chromo_odds.append(-(odds_a+odds_h)/odds_a/2.0+last_value)
		elif mode == 4:
			if len(self.chromo_odds) > 0:
				last_value = self.chromo_odds[len(self.chromo_odds)-1]
			else:
				last_value = 0
			if homeaway == 1:
				if score_h > score_a:
					self.chromo_odds.append((odds_a+odds_h)/odds_a+last_value)
					if odds_h < odds_a:
						self.chromo.append('A')
					else:
						self.chromo.append('G')
				else:
					self.chromo_odds.append(-(odds_a+odds_h)/odds_h+last_value)
					if odds_h > odds_a:
						self.chromo.append('C')
					else:
						self.chromo.append('T')
			else:
				if score_a > score_h:
					self.chromo_odds.append((odds_a+odds_h)/odds_h+last_value)
					if odds_a < odds_h:
						self.chromo.append('C')
					else:
						self.chromo.append('T')
				else:
					self.chromo_odds.append(-(odds_a+odds_h)/odds_a+last_value)
					if odds_a > odds_h:
						self.chromo.append('A')
					else:
						self.chromo.append('G')
		elif mode == 5:
			self.chromo.append('A')
			if len(self.chromo_odds)>0:
				last_value = self.chromo_odds[len(self.chromo_odds)-1]
			else:
				last_value = 0
			if homeaway == 1:
				self.chromo_odds.append((score_h-score_a)+last_value)
			else:
				self.chromo_odds.append((score_a-score_h)+last_value)
		elif mode == 6:
			if len(self.chromo_odds) > 0:
				last_value = self.chromo_odds[len(self.chromo_odds)-1]
			else:
				last_value = 0
			if score_h > score_a:
				if odds_h - 0.15 < odds_a:
					self.chromo.append('A')
				else:
					self.chromo.append('G')
			else:
				if odds_a < odds_h - 0.15:
					self.chromo.append('C')
				else:
					self.chromo.append('T')
			if homeaway == 1:
				if score_h > score_a:
					#self.chromo_odds.append((odds_a+odds_h)/odds_a+last_value)
					if odds_h < odds_a:
						self.chromo_odds.append(1.0+last_value)
					else:
						self.chromo_odds.append(2.0+last_value)
				else:
					if odds_h < odds_a:
						self.chromo_odds.append(-2.0+last_value)
					else:
						self.chromo_odds.append(-1.0+last_value)
					#self.chromo_odds.append(-(odds_a+odds_h)/odds_h+last_value)
			else:
				if score_a > score_h:
					if odds_h < odds_a:
						self.chromo_odds.append(2.0+last_value)
					else:
						self.chromo_odds.append(1.0+last_value)
					#self.chromo_odds.append((odds_a+odds_h)/odds_h+last_value)
				else:
					if odds_h < odds_a:
						self.chromo_odds.append(-1.0+last_value)
					else:
						self.chromo_odds.append(-2.0+last_value)
					#self.chromo_odds.append(-(odds_a+odds_h)/odds_a+last_value)
		elif mode == 7:
			if len(self.chromo_odds) > 0:
				last_value = self.chromo_odds[len(self.chromo_odds)-1]
			else:
				last_value = 0
			score_diff = abs(score_h-score_a)
			if score_diff > 3:
				score_diff = 2.0
			elif score_diff > 1:
				score_diff = 1.5
			else:
				score_diff = 1.0
			if homeaway == 1:
				info = score_h*1000000
				info += score_a*10000
				info += score_mid_h*100
				info += score_mid_a*1
				self.chromo_info.append(int(info))
				if score_h > score_a:
					self.chromo_odds.append(score_diff*(odds_a+odds_h)/odds_a+last_value)
					if odds_h < odds_a:
						self.chromo.append('A')
					else:
						self.chromo.append('G')
				else:
					self.chromo_odds.append(-score_diff*(odds_a+odds_h)/odds_h+last_value)
					if odds_h > odds_a:
						self.chromo.append('C')
					else:
						self.chromo.append('T')
			else:
				info = score_a*1000000
				info += score_h*10000
				info += score_mid_a*100
				info += score_mid_h*1
				self.chromo_info.append(int(info))
				if score_a > score_h:
					self.chromo_odds.append(score_diff*(odds_a+odds_h)/odds_h+last_value)
					if odds_a < odds_h:
						self.chromo.append('A')
					else:
						self.chromo.append('G')
				else:
					self.chromo_odds.append(-score_diff*(odds_a+odds_h)/odds_a+last_value)
					if odds_a > odds_h:
						self.chromo.append('C')
					else:
						self.chromo.append('T')
		elif mode == 8:
			if len(self.chromo_odds) > 0:
				last_value = self.chromo_odds[len(self.chromo_odds)-1]
			else:
				last_value = 0
			score_diff = abs(score_h-score_a)
			if score_diff > 3:
				score_diff = 3.0
			elif score_diff > 1:
				score_diff = 2.0
			else:
				score_diff = 1.0
			if homeaway == 1:
				info = score_h*1000000
				info += score_a*10000
				info += score_mid_h*100
				info += score_mid_a*1
				self.chromo_info.append(int(info))
				if odds_h + 0.35 < odds_a:
					amp = 1.0
				elif abs(odds_h - odds_a) < 0.35:
					amp = 2.0
				else:
					amp = 4.0
				if score_h > score_a:
#					self.chromo_odds.append(amp*(odds_a+odds_h)/odds_a+last_value)
					self.chromo_odds.append(amp+last_value)
					if odds_h < odds_a:
						self.chromo.append('A')
					else:
						self.chromo.append('G')
				else:
#					self.chromo_odds.append(-amp*(odds_a+odds_h)/odds_h+last_value)
					self.chromo_odds.append(-4.0/amp+last_value)
					if odds_h > odds_a:
						self.chromo.append('C')
					else:
						self.chromo.append('T')
			else:
				info = score_a*1000000
				info += score_h*10000
				info += score_mid_a*100
				info += score_mid_h*1
				self.chromo_info.append(int(info))
				if odds_a + 0.35 < odds_h:
					amp = 1.0
				elif abs(odds_a - odds_h) < 0.35:
					amp = 2.0
				else:
					amp = 4.0
				if score_a > score_h:
#					self.chromo_odds.append(amp*(odds_a+odds_h)/odds_h+last_value)
					self.chromo_odds.append(amp+last_value)
					if odds_a < odds_h:
						self.chromo.append('A')
					else:
						self.chromo.append('G')
				else:
					self.chromo_odds.append(-4.0/amp+last_value)
#					self.chromo_odds.append(-amp*(odds_a+odds_h)/odds_a+last_value)
					if odds_a > odds_h:
						self.chromo.append('C')
					else:
						self.chromo.append('T')
		elif mode == 9:
			if homeaway == 1:
				info = score_h*1000000
				info += score_a*10000
				info += score_mid_h*100
				info += score_mid_a*1
				self.chromo_info.append(int(info))
				if score_h > score_a:
					if odds_h < odds_a:
						self.chromo.append('A')
					else:
						self.chromo.append('G')
				else:
					if odds_h > odds_a:
						self.chromo.append('C')
					else:
						self.chromo.append('T')
				self.chromo_odds.append(odds_h)
			else:
				info = score_a*1000000
				info += score_h*10000
				info += score_mid_a*100
				info += score_mid_h*1
				self.chromo_info.append(int(info))
				if score_a > score_h:
					if odds_a < odds_h:
						self.chromo.append('A')
					else:
						self.chromo.append('G')
				else:
					if odds_a > odds_h:
						self.chromo.append('C')
					else:
						self.chromo.append('T')
				self.chromo_odds.append(odds_a)
		elif mode == 10:
			if homeaway == 1:
				info = score_h*1000000
				info += score_a*10000
				info += score_mid_h*100
				info += score_mid_a*1
				self.chromo_info.append(int(info))
				if score_h-1 > score_a:
					if odds_h < odds_a:
						self.chromo.append('A')
					else:
						self.chromo.append('G')
				else:
					if odds_h > odds_a:
						self.chromo.append('C')
					else:
						self.chromo.append('T')
				self.chromo_odds.append(odds_h*1.40)
			else:
				info = score_a*1000000
				info += score_h*10000
				info += score_mid_a*100
				info += score_mid_h*1
				self.chromo_info.append(int(info))
				if score_a-1 > score_h:
					if odds_a < odds_h:
						self.chromo.append('A')
					else:
						self.chromo.append('G')
				else:
					if odds_a > odds_h:
						self.chromo.append('C')
					else:
						self.chromo.append('T')
				self.chromo_odds.append(odds_a*1.40)
		else:
			return -1
	def get_chromo(self):
		return self.chromo
	def get_chromo_odds(self):
		return self.chromo_odds
	def set_Game(self,game):
		self.game_list.insert(0,game)
		return None
	def get_Game(self,kmer):
		if not self.game_list:
			return None
		else:
			if kmer == 2:
				return self.game_list.pop()
			elif kmer == 3:
				if len(self.game_list) < 2:
					return None
				else:
					ret = [self.game_list[0],self.game_list[1]]
					self.game_list.pop()
					return ret
			elif kmer == 4:
				if len(self.game_list) < 3:
					return None
				else:
					ret = [self.game_list[0],self.game_list[1],self.game_list[2]]
					self.game_list.pop()
					return ret
	def set_Series(self,team):
		if self.s_nn == team:
			self.s_n += 1
		else:
			self.s_nn = team
			self.s_n = 1
	def get_Series(self,team):
		if self.s_nn == team:
			return self.s_n
		else:
			return 0
	def update_diff_10_a(self,hometeam,score_w_w,score_w_m,score_w_t,score_l_w,score_l_m,score_l_t):
		self.score_away_hist.append(hometeam)
		self.score_w_w_a.append(score_w_w)
		self.score_w_t_a.append(score_w_t)
		self.score_l_w_a.append(score_l_w)
		self.score_l_t_a.append(score_l_t)
		self.score_w_m_a.append(score_w_m)
		self.score_l_m_a.append(score_l_m)
		if len(self.score_away_hist) > self.record_const:
			self.score_away_hist.remove(self.score_away_hist[0])
		if len(self.score_w_w_a) > self.record_const:
			self.score_w_w_a.remove(self.score_w_w_a[0])
		if len(self.score_w_t_a) > self.record_const:
			self.score_w_t_a.remove(self.score_w_t_a[0])
		if len(self.score_l_w_a) > self.record_const:
			self.score_l_w_a.remove(self.score_l_w_a[0])
		if len(self.score_l_t_a) > self.record_const:
			self.score_l_t_a.remove(self.score_l_t_a[0])
		if len(self.score_w_m_a) > self.record_const:
			self.score_w_m_a.remove(self.score_w_m_a[0])
		if len(self.score_l_m_a) > self.record_const:
			self.score_l_m_a.remove(self.score_l_m_a[0])
	def update_diff_10_h(self,awayteam,score_w_w,score_w_m,score_w_t,score_l_w,score_l_m,score_l_t):
		self.score_home_hist.append(awayteam)
		self.score_w_w_h.append(score_w_w)
		self.score_w_t_h.append(score_w_t)
		self.score_l_w_h.append(score_l_w)
		self.score_l_t_h.append(score_l_t)
		self.score_w_m_h.append(score_w_m)
		self.score_l_m_h.append(score_l_m)
		if len(self.score_home_hist) > self.record_const:
			self.score_home_hist.remove(self.score_home_hist[0])
		if len(self.score_w_w_h) > self.record_const:
			self.score_w_w_h.remove(self.score_w_w_h[0])
		if len(self.score_w_t_h) > self.record_const:
			self.score_w_t_h.remove(self.score_w_t_h[0])
		if len(self.score_l_w_h) > self.record_const:
			self.score_l_w_h.remove(self.score_l_w_h[0])
		if len(self.score_l_t_h) > self.record_const:
			self.score_l_t_h.remove(self.score_l_t_h[0])
		if len(self.score_w_m_h) > self.record_const:
			self.score_w_m_h.remove(self.score_w_m_h[0])
		if len(self.score_l_m_h) > self.record_const:
			self.score_l_m_h.remove(self.score_l_m_h[0])
	def update_score_10_a(self,hometeam,win_j_10,win_y_10,lose_j_10,lose_y_10):
		self.odds_away_hist.append(hometeam)
		self.win_j_a.append(win_j_10)
		self.win_y_a.append(win_y_10)
		self.lose_j_a.append(lose_j_10)
		self.lose_y_a.append(lose_y_10)
		if len(self.odds_away_hist)>self.record_const:
			self.odds_away_hist.remove(self.odds_away_hist[0])
		if len(self.win_j_a) > self.record_const:
			self.win_j_a.remove(self.win_j_a[0])
		if len(self.win_y_a) > self.record_const:
			self.win_y_a.remove(self.win_y_a[0])
		if len(self.lose_j_a) > self.record_const:
			self.lose_j_a.remove(self.lose_j_a[0])
		if len(self.lose_y_a) > self.record_const:
			self.lose_y_a.remove(self.lose_y_a[0])
	def update_score_10_h(self,awayteam,win_j_10,win_y_10,lose_j_10,lose_y_10):
		self.odds_home_hist.append(awayteam)
		self.win_j_h.append(win_j_10)
		self.win_y_h.append(win_y_10)
		self.lose_j_h.append(lose_j_10)
		self.lose_y_h.append(lose_y_10)
		if len(self.odds_home_hist)>self.record_const:
			self.odds_home_hist.remove(self.odds_home_hist[0])
		if len(self.win_j_h) > self.record_const:
			self.win_j_h.remove(self.win_j_h[0])
		if len(self.win_y_h) > self.record_const:
			self.win_y_h.remove(self.win_y_h[0])
		if len(self.lose_j_h) > self.record_const:
			self.lose_j_h.remove(self.lose_j_h[0])
		if len(self.lose_y_h) > self.record_const:
			self.lose_y_h.remove(self.lose_y_h[0])
	def update_score(self,hometeam,awayteam,score_diff,odds,home_away):
		if(home_away):
			if score_diff > 0:
				if odds <= self.odds_mid:
					self.update_score_10_h(awayteam,1.0*odds/self.record_const,0,0,0)
				elif odds > self.odds_mid:
					self.update_score_10_h(awayteam,0,2.0*odds/self.record_const,0,0)
				if score_diff > self.score_mid:
					self.update_diff_10_h(awayteam,3.0*odds/self.record_const,0,0,0,0,0)
				elif score_diff == self.score_tight:
					self.update_diff_10_h(awayteam,0,0,2.0*odds/self.record_const,0,0,0)
				else:
					self.update_diff_10_h(awayteam,0,1.0*odds/self.record_const,0,0,0,0)
			elif score_diff < 0:
				if odds >= self.odds_mid:
					self.update_score_10_h(awayteam,0,0,-1.0/odds/self.record_const,0)
				elif odds < self.odds_mid:
					self.update_score_10_h(awayteam,0,0,0,-2.0/odds/self.record_const)
				if -1*score_diff > self.score_mid:
					self.update_diff_10_h(awayteam,0,0,0,-3.0/odds/self.record_const,0,0)
				elif -1*score_diff == self.score_tight:
					self.update_diff_10_h(awayteam,0,0,0,0,0,-2.0/odds/self.record_const)
				else:
					self.update_diff_10_h(awayteam,0,0,0,0,-1.0/odds/self.record_const,0)
		else:
			if score_diff < 0:
				if odds <= self.odds_mid:
					self.update_score_10_a(hometeam,1.0*odds/self.record_const,0,0,0)
				elif odds > self.odds_mid:
					self.update_score_10_a(hometeam,0,2.0*odds/self.record_const,0,0)
				if -1*score_diff > self.score_mid:
					self.update_diff_10_a(hometeam,3.0*odds/self.record_const,0,0,0,0,0)
				elif -1*score_diff == self.score_tight:
					self.update_diff_10_a(hometeam,0,0,2.0*odds/self.record_const,0,0,0)
				else:
					self.update_diff_10_a(hometeam,0,1.0*odds/self.record_const,0,0,0,0)
			elif score_diff > 0:
				if odds >= self.odds_mid:
					self.update_score_10_a(hometeam,0,0,-1.0/odds/self.record_const,0)
				elif odds < self.odds_mid:
					self.update_score_10_a(hometeam,0,0,0,-2.0/odds/self.record_const)
				if score_diff > self.score_mid:
					self.update_diff_10_a(hometeam,0,0,0,-3.0/odds/self.record_const,0,0)
				elif score_diff == self.score_tight:
					self.update_diff_10_a(hometeam,0,0,0,0,0,-2.0/odds/self.record_const)
				else:
					self.update_diff_10_a(hometeam,0,0,0,0,-1.0/odds/self.record_const,0)
	def get_score_home_hist(self,awayteam):
		trg = 0
		cnt = 0
		cnt_a = 0
		res = [0.0,0.0,0.0,0.0,0.0,0.0]
		if len(self.score_home_hist) == 0:
				return [1.0,1.0,1.0,1.0,1.0,1.0]
		for ii in reversed(self.score_home_hist):
			cnt += 1
			if ii != awayteam:
				if trg == 0:
					leng = len(self.score_home_hist)
					res[0] = sum(self.score_w_w_h)/leng
					res[1] = sum(self.score_w_t_h)/leng
					res[2] = sum(self.score_w_m_h)/leng
					res[3] = sum(self.score_l_w_h)/leng
					res[4] = sum(self.score_l_t_h)/leng
					res[5] = sum(self.score_l_m_h)/leng
					return res
				else:
					dom = (len(self.score_home_hist)-cnt_a)*1.0/len(self.score_home_hist)
					res[0] += self.score_w_w_h[len(self.score_home_hist)-cnt]/dom
					res[1] += self.score_w_t_h[len(self.score_home_hist)-cnt]/dom
					res[2] += self.score_w_m_h[len(self.score_home_hist)-cnt]/dom
					res[3] += self.score_l_w_h[len(self.score_home_hist)-cnt]/dom
					res[4] += self.score_l_t_h[len(self.score_home_hist)-cnt]/dom
					res[5] += self.score_l_m_h[len(self.score_home_hist)-cnt]/dom
			else:
				cnt_a += 1
				trg = 1
				res[0] += self.score_w_w_h[len(self.score_home_hist)-cnt]	
				res[1] += self.score_w_t_h[len(self.score_home_hist)-cnt]	
				res[2] += self.score_w_m_h[len(self.score_home_hist)-cnt]	
				res[3] += self.score_l_w_h[len(self.score_home_hist)-cnt]	
				res[4] += self.score_l_t_h[len(self.score_home_hist)-cnt]	
				res[5] += self.score_l_m_h[len(self.score_home_hist)-cnt]	
		return res		
	def get_score_away_hist(self,hometeam):
		trg = 0
		cnt = 0
		cnt_a = 0
		res = [0.0,0.0,0.0,0.0,0.0,0.0]
		if len(self.score_away_hist) == 0:
				return [1.0,1.0,1.0,1.0,1.0,1.0]
		for ii in reversed(self.score_away_hist):
			cnt += 1
			if ii != hometeam:
				if trg == 0:
					leng = len(self.score_away_hist)
					res[0] = sum(self.score_w_w_a)/leng
					res[1] = sum(self.score_w_t_a)/leng
					res[2] = sum(self.score_w_m_a)/leng
					res[3] = sum(self.score_l_w_a)/leng
					res[4] = sum(self.score_l_t_a)/leng
					res[5] = sum(self.score_l_m_a)/leng
					return res
				else:
					dom = (len(self.score_away_hist)-cnt_a)*1.0/len(self.score_away_hist)
					res[0] += self.score_w_w_a[len(self.score_away_hist)-cnt]/dom
					res[1] += self.score_w_t_a[len(self.score_away_hist)-cnt]/dom
					res[2] += self.score_w_m_a[len(self.score_away_hist)-cnt]/dom
					res[3] += self.score_l_w_a[len(self.score_away_hist)-cnt]/dom
					res[4] += self.score_l_t_a[len(self.score_away_hist)-cnt]/dom
					res[5] += self.score_l_m_a[len(self.score_away_hist)-cnt]/dom
			else:
				cnt_a += 1
				trg = 1
				res[0] += self.score_w_w_a[len(self.score_away_hist)-cnt]	
				res[1] += self.score_w_t_a[len(self.score_away_hist)-cnt]	
				res[2] += self.score_w_m_a[len(self.score_away_hist)-cnt]	
				res[3] += self.score_l_w_a[len(self.score_away_hist)-cnt]	
				res[4] += self.score_l_t_a[len(self.score_away_hist)-cnt]	
				res[5] += self.score_l_m_a[len(self.score_away_hist)-cnt]	
		return res
	def get_odds_home_hist(self,awayteam):
		trg = 0
		cnt = 0
		cnt_a = 0
		res = [0.0,0.0,0.0,0.0]
		if len(self.odds_home_hist) == 0:
				return [1.0,1.0,1.0,1.0]
		for ii in reversed(self.odds_home_hist):
			cnt += 1
			if ii != awayteam:
				if trg == 0:
					leng = len(self.odds_home_hist)
					res[0] = sum(self.win_j_h)/leng
					res[1] = sum(self.win_y_h)/leng
					res[2] = sum(self.lose_j_h)/leng
					res[3] = sum(self.lose_y_h)/leng
					return res
				else:
					dom = (len(self.odds_home_hist)-cnt_a)*1.0/len(self.odds_home_hist)
					res[0] += self.win_j_h[len(self.odds_home_hist)-cnt]/dom
					res[1] += self.win_y_h[len(self.odds_home_hist)-cnt]/dom
					res[2] += self.lose_j_h[len(self.odds_home_hist)-cnt]/dom
					res[3] += self.lose_y_h[len(self.odds_home_hist)-cnt]/dom
			else:
				cnt_a += 1
				trg = 1
				res[0] += self.win_j_h[len(self.odds_home_hist)-cnt]	
				res[1] += self.win_y_h[len(self.odds_home_hist)-cnt]	
				res[2] += self.lose_j_h[len(self.odds_home_hist)-cnt]	
				res[3] += self.lose_y_h[len(self.odds_home_hist)-cnt]	
		return res
	def get_odds_away_hist(self,hometeam):
		trg = 0
		cnt = 0
		cnt_a = 0
		res = [0.0,0.0,0.0,0.0]
		if len(self.odds_away_hist) == 0:
				return [1.0,1.0,1.0,1.0]
		for ii in reversed(self.odds_away_hist):
			cnt += 1
			if ii != hometeam:
				if trg == 0:
					leng = len(self.odds_away_hist)
					res[0] = sum(self.win_j_a)/leng
					res[1] = sum(self.win_y_a)/leng
					res[2] = sum(self.lose_j_a)/leng
					res[3] = sum(self.lose_y_a)/leng
					return res
				else:
#					dom = 1.0/len(self.odds_away_hist)
					dom = (len(self.odds_away_hist)-cnt_a)*1.0/len(self.odds_away_hist)
					res[0] += self.win_j_a[len(self.odds_away_hist)-cnt]/dom
					res[1] += self.win_y_a[len(self.odds_away_hist)-cnt]/dom
					res[2] += self.lose_j_a[len(self.odds_away_hist)-cnt]/dom
					res[3] += self.lose_y_a[len(self.odds_away_hist)-cnt]/dom
			else:
				cnt_a += 1
				trg = 1
				res[0] += self.win_j_a[len(self.odds_away_hist)-cnt]	
				res[1] += self.win_y_a[len(self.odds_away_hist)-cnt]	
				res[2] += self.lose_j_a[len(self.odds_away_hist)-cnt]	
				res[3] += self.lose_y_a[len(self.odds_away_hist)-cnt]	
		return res
	def get_Name(self):
		return self.Name
class Team2():
	Name=""
	odds_record_interval = 10
	record_const = 10
	score_mid = 3
	score_tight = 1
	odds_mid = 1.92
	odds_low = 1.60
	odds_high= 2.55
	def __init__(self,name):
		self.Name = name
		self.score_w_w_h = []
		self.score_w_w_a = []
		self.score_w_t_h = []
		self.score_w_t_a = []
		self.score_w_m_h = []
		self.score_w_m_a = []
		self.score_l_w_h = []
		self.score_l_w_a = []
		self.score_l_t_h = []
		self.score_l_t_a = []
		self.score_l_m_h = []
		self.score_l_m_a = []
		self.win_j_h  = []
		self.win_y_h   = []
		self.lose_j_h = []
		self.lose_y_h  = []
		self.win_j_a  = []
		self.win_y_a   = []
		self.lose_j_a = []
		self.lose_y_a  = []
		self.odds_record = []
		self.score_home_hist = []
		self.score_away_hist = []
		self.odds_home_hist = []
		self.odds_away_hist = []
	def initial(self):
		self.score_w_w_h = []
		self.score_w_w_a = []
		self.score_w_t_h = []
		self.score_w_t_a = []
		self.score_w_m_h = []
		self.score_w_m_a = []
		self.score_l_w_h = []
		self.score_l_w_a = []
		self.score_l_t_h = []
		self.score_l_t_a = []
		self.score_l_m_h = []
		self.score_l_m_a = []
		self.win_j_h  = []
		self.win_y_h   = []
		self.lose_j_h = []
		self.lose_y_h  = []
		self.win_j_a  = []
		self.win_y_a   = []
		self.lose_j_a = []
		self.lose_y_a  = []
		self.odds_record = []
		self.score_home_hist = []
		self.score_away_hist = []
		self.odds_home_hist = []
		self.odds_away_hist = []
	def update_diff_10_a(self,hometeam,score_w_w,score_w_m,score_w_t,score_l_w,score_l_m,score_l_t):
		self.score_away_hist.append(hometeam)
		self.score_w_w_a.append(score_w_w)
		self.score_w_t_a.append(score_w_t)
		self.score_l_w_a.append(score_l_w)
		self.score_l_t_a.append(score_l_t)
		self.score_w_m_a.append(score_w_m)
		self.score_l_m_a.append(score_l_m)
		if len(self.score_away_hist) > self.record_const:
			self.score_away_hist.remove(self.score_away_hist[0])
		if len(self.score_w_w_a) > self.record_const:
			self.score_w_w_a.remove(self.score_w_w_a[0])
		if len(self.score_w_t_a) > self.record_const:
			self.score_w_t_a.remove(self.score_w_t_a[0])
		if len(self.score_l_w_a) > self.record_const:
			self.score_l_w_a.remove(self.score_l_w_a[0])
		if len(self.score_l_t_a) > self.record_const:
			self.score_l_t_a.remove(self.score_l_t_a[0])
		if len(self.score_w_m_a) > self.record_const:
			self.score_w_m_a.remove(self.score_w_m_a[0])
		if len(self.score_l_m_a) > self.record_const:
			self.score_l_m_a.remove(self.score_l_m_a[0])
	def update_diff_10_h(self,awayteam,score_w_w,score_w_m,score_w_t,score_l_w,score_l_m,score_l_t):
		self.score_home_hist.append(awayteam)
		self.score_w_w_h.append(score_w_w)
		self.score_w_t_h.append(score_w_t)
		self.score_l_w_h.append(score_l_w)
		self.score_l_t_h.append(score_l_t)
		self.score_w_m_h.append(score_w_m)
		self.score_l_m_h.append(score_l_m)
		if len(self.score_home_hist) > self.record_const:
			self.score_home_hist.remove(self.score_home_hist[0])
		if len(self.score_w_w_h) > self.record_const:
			self.score_w_w_h.remove(self.score_w_w_h[0])
		if len(self.score_w_t_h) > self.record_const:
			self.score_w_t_h.remove(self.score_w_t_h[0])
		if len(self.score_l_w_h) > self.record_const:
			self.score_l_w_h.remove(self.score_l_w_h[0])
		if len(self.score_l_t_h) > self.record_const:
			self.score_l_t_h.remove(self.score_l_t_h[0])
		if len(self.score_w_m_h) > self.record_const:
			self.score_w_m_h.remove(self.score_w_m_h[0])
		if len(self.score_l_m_h) > self.record_const:
			self.score_l_m_h.remove(self.score_l_m_h[0])
	def update_score_10_a(self,hometeam,win_j_10,win_y_10,lose_j_10,lose_y_10):
		self.odds_away_hist.append(hometeam)
		self.win_j_a.append(win_j_10)
		self.win_y_a.append(win_y_10)
		self.lose_j_a.append(lose_j_10)
		self.lose_y_a.append(lose_y_10)
		if len(self.odds_away_hist)>self.record_const:
			self.odds_away_hist.remove(self.odds_away_hist[0])
		if len(self.win_j_a) > self.record_const:
			self.win_j_a.remove(self.win_j_a[0])
		if len(self.win_y_a) > self.record_const:
			self.win_y_a.remove(self.win_y_a[0])
		if len(self.lose_j_a) > self.record_const:
			self.lose_j_a.remove(self.lose_j_a[0])
		if len(self.lose_y_a) > self.record_const:
			self.lose_y_a.remove(self.lose_y_a[0])
	def update_score_10_h(self,awayteam,win_j_10,win_y_10,lose_j_10,lose_y_10):
		self.odds_home_hist.append(awayteam)
		self.win_j_h.append(win_j_10)
		self.win_y_h.append(win_y_10)
		self.lose_j_h.append(lose_j_10)
		self.lose_y_h.append(lose_y_10)
		if len(self.odds_home_hist)>self.record_const:
			self.odds_home_hist.remove(self.odds_home_hist[0])
		if len(self.win_j_h) > self.record_const:
			self.win_j_h.remove(self.win_j_h[0])
		if len(self.win_y_h) > self.record_const:
			self.win_y_h.remove(self.win_y_h[0])
		if len(self.lose_j_h) > self.record_const:
			self.lose_j_h.remove(self.lose_j_h[0])
		if len(self.lose_y_h) > self.record_const:
			self.lose_y_h.remove(self.lose_y_h[0])
	def update_score(self,hometeam,awayteam,score_diff,odds,home_away):
		if(home_away):
			if score_diff > 0:
				if odds <= self.odds_mid:
					self.update_score_10_h(awayteam,score_diff*odds/self.record_const,0,0,0)
				elif odds > self.odds_mid:
					self.update_score_10_h(awayteam,0,score_diff*odds/self.record_const,0,0)
				if score_diff > self.score_mid:
					self.update_diff_10_h(awayteam,score_diff*odds/self.record_const,0,0,0,0,0)
				elif score_diff == self.score_tight:
					self.update_diff_10_h(awayteam,0,0,score_diff*odds/self.record_const,0,0,0)
				else:
					self.update_diff_10_h(awayteam,0,score_diff*odds/self.record_const,0,0,0,0)
			elif score_diff < 0:
				if odds >= self.odds_mid:
					self.update_score_10_h(awayteam,0,0,score_diff/odds/self.record_const,0)
				elif odds < self.odds_mid:
					self.update_score_10_h(awayteam,0,0,0,score_diff/odds/self.record_const)
				if -1*score_diff > self.score_mid:
					self.update_diff_10_h(awayteam,0,0,0,score_diff/odds/self.record_const,0,0)
				elif -1*score_diff == self.score_tight:
					self.update_diff_10_h(awayteam,0,0,0,0,0,score_diff/odds/self.record_const)
				else:
					self.update_diff_10_h(awayteam,0,0,0,0,score_diff/odds/self.record_const,0)
		else:
			if score_diff < 0:
				if odds <= self.odds_mid:
					self.update_score_10_a(hometeam,-1*score_diff*odds/self.record_const,0,0,0)
				elif odds > self.odds_mid:
					self.update_score_10_a(hometeam,0,-1*score_diff*odds/self.record_const,0,0)
				if -1*score_diff > self.score_mid:
					self.update_diff_10_a(hometeam,-1*score_diff*odds/self.record_const,0,0,0,0,0)
				elif -1*score_diff == self.score_tight:
					self.update_diff_10_a(hometeam,0,0,-1*score_diff*odds/self.record_const,0,0,0)
				else:
					self.update_diff_10_a(hometeam,0,-1*score_diff*odds/self.record_const,0,0,0,0)
			elif score_diff > 0:
				if odds >= self.odds_mid:
					self.update_score_10_a(hometeam,0,0,-1*score_diff/odds/self.record_const,0)
				elif odds < self.odds_mid:
					self.update_score_10_a(hometeam,0,0,0,-1*score_diff/odds/self.record_const)
				if score_diff > self.score_mid:
					self.update_diff_10_a(hometeam,0,0,0,-1*score_diff/odds/self.record_const,0,0)
				elif score_diff == self.score_tight:
					self.update_diff_10_a(hometeam,0,0,0,0,0,-1*score_diff/odds/self.record_const)
				else:
					self.update_diff_10_a(hometeam,0,0,0,0,-1*score_diff/odds/self.record_const,0)
	def get_score_home_hist(self,awayteam):
		trg = 0
		cnt = 0
		cnt_a = 0
		res = [0.0,0.0,0.0,0.0,0.0,0.0]
		if len(self.score_home_hist) == 0:
				return [1.0,1.0,1.0,1.0,1.0,1.0]
		for ii in reversed(self.score_home_hist):
			cnt += 1
			if ii != awayteam:
				if trg == 0:
					leng = len(self.score_home_hist)
					res[0] = sum(self.score_w_w_h)/leng
					res[1] = sum(self.score_w_t_h)/leng
					res[2] = sum(self.score_w_m_h)/leng
					res[3] = sum(self.score_l_w_h)/leng
					res[4] = sum(self.score_l_t_h)/leng
					res[5] = sum(self.score_l_m_h)/leng
					return res
				else:
					dom = (len(self.score_home_hist)-cnt_a)*1.0/len(self.score_home_hist)
					res[0] += self.score_w_w_h[len(self.score_home_hist)-cnt]/dom
					res[1] += self.score_w_t_h[len(self.score_home_hist)-cnt]/dom
					res[2] += self.score_w_m_h[len(self.score_home_hist)-cnt]/dom
					res[3] += self.score_l_w_h[len(self.score_home_hist)-cnt]/dom
					res[4] += self.score_l_t_h[len(self.score_home_hist)-cnt]/dom
					res[5] += self.score_l_m_h[len(self.score_home_hist)-cnt]/dom
			else:
				cnt_a += 1
				trg = 1
				res[0] += self.score_w_w_h[len(self.score_home_hist)-cnt]	
				res[1] += self.score_w_t_h[len(self.score_home_hist)-cnt]	
				res[2] += self.score_w_m_h[len(self.score_home_hist)-cnt]	
				res[3] += self.score_l_w_h[len(self.score_home_hist)-cnt]	
				res[4] += self.score_l_t_h[len(self.score_home_hist)-cnt]	
				res[5] += self.score_l_m_h[len(self.score_home_hist)-cnt]	
		return res		
	def get_score_away_hist(self,hometeam):
		trg = 0
		cnt = 0
		cnt_a = 0
		res = [0.0,0.0,0.0,0.0,0.0,0.0]
		if len(self.score_away_hist) == 0:
				return [1.0,1.0,1.0,1.0,1.0,1.0]
		for ii in reversed(self.score_away_hist):
			cnt += 1
			if ii != hometeam:
				if trg == 0:
					leng = len(self.score_away_hist)
					res[0] = sum(self.score_w_w_a)/leng
					res[1] = sum(self.score_w_t_a)/leng
					res[2] = sum(self.score_w_m_a)/leng
					res[3] = sum(self.score_l_w_a)/leng
					res[4] = sum(self.score_l_t_a)/leng
					res[5] = sum(self.score_l_m_a)/leng
					return res
				else:
					dom = (len(self.score_away_hist)-cnt_a)*1.0/len(self.score_away_hist)
					res[0] += self.score_w_w_a[len(self.score_away_hist)-cnt]/dom
					res[1] += self.score_w_t_a[len(self.score_away_hist)-cnt]/dom
					res[2] += self.score_w_m_a[len(self.score_away_hist)-cnt]/dom
					res[3] += self.score_l_w_a[len(self.score_away_hist)-cnt]/dom
					res[4] += self.score_l_t_a[len(self.score_away_hist)-cnt]/dom
					res[5] += self.score_l_m_a[len(self.score_away_hist)-cnt]/dom
			else:
				cnt_a += 1
				trg = 1
				res[0] += self.score_w_w_a[len(self.score_away_hist)-cnt]	
				res[1] += self.score_w_t_a[len(self.score_away_hist)-cnt]	
				res[2] += self.score_w_m_a[len(self.score_away_hist)-cnt]	
				res[3] += self.score_l_w_a[len(self.score_away_hist)-cnt]	
				res[4] += self.score_l_t_a[len(self.score_away_hist)-cnt]	
				res[5] += self.score_l_m_a[len(self.score_away_hist)-cnt]	
		return res
	def get_odds_home_hist(self,awayteam):
		trg = 0
		cnt = 0
		cnt_a = 0
		res = [0.0,0.0,0.0,0.0]
		if len(self.odds_home_hist) == 0:
				return [1.0,1.0,1.0,1.0]
		for ii in reversed(self.odds_home_hist):
			cnt += 1
			if ii != awayteam:
				if trg == 0:
					leng = len(self.odds_home_hist)
					res[0] = sum(self.win_j_h)/leng
					res[1] = sum(self.win_y_h)/leng
					res[2] = sum(self.lose_j_h)/leng
					res[3] = sum(self.lose_y_h)/leng
					return res
				else:
					dom = (len(self.odds_home_hist)-cnt_a)*1.0/len(self.odds_home_hist)
					res[0] += self.win_j_h[len(self.odds_home_hist)-cnt]/dom
					res[1] += self.win_y_h[len(self.odds_home_hist)-cnt]/dom
					res[2] += self.lose_j_h[len(self.odds_home_hist)-cnt]/dom
					res[3] += self.lose_y_h[len(self.odds_home_hist)-cnt]/dom
			else:
				cnt_a += 1
				trg = 1
				res[0] += self.win_j_h[len(self.odds_home_hist)-cnt]	
				res[1] += self.win_y_h[len(self.odds_home_hist)-cnt]	
				res[2] += self.lose_j_h[len(self.odds_home_hist)-cnt]	
				res[3] += self.lose_y_h[len(self.odds_home_hist)-cnt]	
		return res
	def get_odds_away_hist(self,hometeam):
		trg = 0
		cnt = 0
		cnt_a = 0
		res = [0.0,0.0,0.0,0.0]
		if len(self.odds_away_hist) == 0:
				return [1.0,1.0,1.0,1.0]
		for ii in reversed(self.odds_away_hist):
			cnt += 1
			if ii != hometeam:
				if trg == 0:
					leng = len(self.odds_away_hist)
					res[0] = sum(self.win_j_a)/leng
					res[1] = sum(self.win_y_a)/leng
					res[2] = sum(self.lose_j_a)/leng
					res[3] = sum(self.lose_y_a)/leng
					return res
				else:
#					dom = 1.0/len(self.odds_away_hist)
					dom = (len(self.odds_away_hist)-cnt_a)*1.0/len(self.odds_away_hist)
					res[0] += self.win_j_a[len(self.odds_away_hist)-cnt]/dom
					res[1] += self.win_y_a[len(self.odds_away_hist)-cnt]/dom
					res[2] += self.lose_j_a[len(self.odds_away_hist)-cnt]/dom
					res[3] += self.lose_y_a[len(self.odds_away_hist)-cnt]/dom
			else:
				cnt_a += 1
				trg = 1
				res[0] += self.win_j_a[len(self.odds_away_hist)-cnt]	
				res[1] += self.win_y_a[len(self.odds_away_hist)-cnt]	
				res[2] += self.lose_j_a[len(self.odds_away_hist)-cnt]	
				res[3] += self.lose_y_a[len(self.odds_away_hist)-cnt]	
		return res
	def get_Name(self):
		return self.Name
class Team():
	Name=""
	odds_record_interval = 10
	record_const = 10
	score_mid = 3
	score_tight = 1
	odds_mid = 1.92
	odds_low = 1.60
	odds_high= 2.55
	def __init__(self,name):
		self.Name = name
		self.score_w_w_h = []
		self.score_w_w_a = []
		self.score_w_t_h = []
		self.score_w_t_a = []
		self.score_w_m_h = []
		self.score_w_m_a = []
		self.score_l_w_h = []
		self.score_l_w_a = []
		self.score_l_t_h = []
		self.score_l_t_a = []
		self.score_l_m_h = []
		self.score_l_m_a = []
		self.win_j_h  = []
		self.win_y_h   = []
		self.lose_j_h = []
		self.lose_y_h  = []
		self.win_j_a  = []
		self.win_y_a   = []
		self.lose_j_a = []
		self.lose_y_a  = []
		self.odds_record = []
		
	def initial(self):
		self.score_w_w_h = []
		self.score_w_w_a = []
		self.score_w_t_h = []
		self.score_w_t_a = []
		self.score_w_m_h = []
		self.score_w_m_a = []
		self.score_l_w_h = []
		self.score_l_w_a = []
		self.score_l_t_h = []
		self.score_l_t_a = []
		self.score_l_m_h = []
		self.score_l_m_a = []
		self.win_j_h  = []
		self.win_y_h   = []
		self.lose_j_h = []
		self.lose_y_h  = []
		self.win_j_a  = []
		self.win_y_a   = []
		self.lose_j_a = []
		self.lose_y_a  = []
		self.odds_record = []
	def update_diff_10_a(self,score_w_w,score_w_m,score_w_t,score_l_w,score_l_m,score_l_t):
		self.score_w_w_a.append(score_w_w)
		self.score_w_t_a.append(score_w_t)
		self.score_l_w_a.append(score_l_w)
		self.score_l_t_a.append(score_l_t)
		self.score_w_m_a.append(score_w_m)
		self.score_l_m_a.append(score_l_m)
		if len(self.score_w_w_a) > self.record_const:
			self.score_w_w_a.remove(self.score_w_w_a[0])
		if len(self.score_w_t_a) > self.record_const:
			self.score_w_t_a.remove(self.score_w_t_a[0])
		if len(self.score_l_w_a) > self.record_const:
			self.score_l_w_a.remove(self.score_l_w_a[0])
		if len(self.score_l_t_a) > self.record_const:
			self.score_l_t_a.remove(self.score_l_t_a[0])
		if len(self.score_w_m_a) > self.record_const:
			self.score_w_m_a.remove(self.score_w_m_a[0])
		if len(self.score_l_m_a) > self.record_const:
			self.score_l_m_a.remove(self.score_l_m_a[0])
	def update_diff_10_h(self,score_w_w,score_w_m,score_w_t,score_l_w,score_l_m,score_l_t):
		self.score_w_w_h.append(score_w_w)
		self.score_w_t_h.append(score_w_t)
		self.score_l_w_h.append(score_l_w)
		self.score_l_t_h.append(score_l_t)
		self.score_w_m_h.append(score_w_m)
		self.score_l_m_h.append(score_l_m)
		if len(self.score_w_w_h) > self.record_const:
			self.score_w_w_h.remove(self.score_w_w_h[0])
		if len(self.score_w_t_h) > self.record_const:
			self.score_w_t_h.remove(self.score_w_t_h[0])
		if len(self.score_l_w_h) > self.record_const:
			self.score_l_w_h.remove(self.score_l_w_h[0])
		if len(self.score_l_t_h) > self.record_const:
			self.score_l_t_h.remove(self.score_l_t_h[0])
		if len(self.score_w_m_h) > self.record_const:
			self.score_w_m_h.remove(self.score_w_m_h[0])
		if len(self.score_l_m_h) > self.record_const:
			self.score_l_m_h.remove(self.score_l_m_h[0])
	def update_score_10_a(self,win_j_10,win_y_10,lose_j_10,lose_y_10):
		self.win_j_a.append(win_j_10)
		self.win_y_a.append(win_y_10)
		self.lose_j_a.append(lose_j_10)
		self.lose_y_a.append(lose_y_10)
		if len(self.win_j_a) > self.record_const:
			self.win_j_a.remove(self.win_j_a[0])
		if len(self.win_y_a) > self.record_const:
			self.win_y_a.remove(self.win_y_a[0])
		if len(self.lose_j_a) > self.record_const:
			self.lose_j_a.remove(self.lose_j_a[0])
		if len(self.lose_y_a) > self.record_const:
			self.lose_y_a.remove(self.lose_y_a[0])
	def update_score_10_h(self,win_j_10,win_y_10,lose_j_10,lose_y_10):
		self.win_j_h.append(win_j_10)
		self.win_y_h.append(win_y_10)
		self.lose_j_h.append(lose_j_10)
		self.lose_y_h.append(lose_y_10)
		if len(self.win_j_h) > self.record_const:
			self.win_j_h.remove(self.win_j_h[0])
		if len(self.win_y_h) > self.record_const:
			self.win_y_h.remove(self.win_y_h[0])
		if len(self.lose_j_h) > self.record_const:
			self.lose_j_h.remove(self.lose_j_h[0])
		if len(self.lose_y_h) > self.record_const:
			self.lose_y_h.remove(self.lose_y_h[0])
	def update_score(self,score_diff,odds,home_away):
		if(home_away):
			if score_diff > 0:
				if odds <= self.odds_mid:
					self.update_score_10_h(1.0/self.record_const,0,0,0)
				elif odds > self.odds_mid:
					self.update_score_10_h(0,1.0/self.record_const,0,0)
				if score_diff > self.score_mid:
					self.update_diff_10_h(1.0/self.record_const,0,0,0,0,0)
				elif score_diff == self.score_tight:
					self.update_diff_10_h(0,0,1.0/self.record_const,0,0,0)
				else:
					self.update_diff_10_h(0,1.0/self.record_const,0,0,0,0)
			elif score_diff < 0:
				if odds >= self.odds_mid:
					self.update_score_10_h(0,0,1.0/self.record_const,0)
				elif odds < self.odds_mid:
					self.update_score_10_h(0,0,0,1.0/self.record_const)
				if -1*score_diff > self.score_mid:
					self.update_diff_10_h(0,0,0,1.0/self.record_const,0,0)
				elif -1*score_diff == self.score_tight:
					self.update_diff_10_h(0,0,0,0,0,1.0/self.record_const)
				else:
					self.update_diff_10_h(0,0,0,0,1.0/self.record_const,0)
				
		else:
			if score_diff < 0:
				if odds <= self.odds_mid:
					self.update_score_10_a(-1*1.0/self.record_const,0,0,0)
				elif odds > self.odds_mid:
					self.update_score_10_a(0,-1*1.0/self.record_const,0,0)
				if -1*score_diff > self.score_mid:
					self.update_diff_10_a(-1*1.0/self.record_const,0,0,0,0,0)
				elif -1*score_diff == self.score_tight:
					self.update_diff_10_a(0,0,-1*1.0/self.record_const,0,0,0)
				else:
					self.update_diff_10_a(0,-1*1.0/self.record_const,0,0,0,0)
			elif score_diff > 0:
				if odds >= self.odds_mid:
					self.update_score_10_a(0,0,-1*1.0/self.record_const,0)
				elif odds < self.odds_mid:
					self.update_score_10_a(0,0,0,-1*1.0/self.record_const)
				if score_diff > self.score_mid:
					self.update_diff_10_a(0,0,0,-1*1.0/self.record_const,0,0)
				elif score_diff == self.score_tight:
					self.update_diff_10_a(0,0,0,0,0,-1.0/self.record_const)
				else:
					self.update_diff_10_a(0,0,0,0,-1.0/self.record_const,0)
	def get_score_w_w(self,home_away):
		if home_away:
			return sum(self.score_w_w_h)
		else:
			return sum(self.score_w_w_a)
	def get_score_w_t(self,home_away):
		if home_away:
			return sum(self.score_w_t_h)
		else:
			return sum(self.score_w_t_a)
	def get_score_l_w(self,home_away):
		if home_away:
			return sum(self.score_l_w_h)
		else:
			return sum(self.score_l_w_a)
	def get_score_l_t(self,home_away):
		if home_away:
			return sum(self.score_l_t_h)
		else:
			return sum(self.score_l_t_a)
	def get_score_w_m(self,home_away):
		if home_away:
			return sum(self.score_w_m_h)
		else:
			return sum(self.score_w_m_a)
	def get_score_l_m(self,home_away):
		if home_away:
			return sum(self.score_l_m_h)
		else:
			return sum(self.score_l_m_a)
	def get_win_j(self,home_away):
		if home_away:
			return sum(self.win_j_h)
		else:
			return sum(self.win_j_a)
	def get_win_y(self,home_away):
		if home_away:
			return sum(self.win_y_h)
		else:
			return sum(self.win_j_a)
	def get_lose_j(self,home_away):
		if home_away:
			return sum(self.lose_j_h)
		else:
			return sum(self.lose_j_a)
	def get_lose_y(self,home_away):
		if home_away:
			return sum(self.lose_y_h)
		else:
			return sum(self.lose_y_a)
	def get_Name(self):
		return self.Name
################################
class Bank():
	Name = "Jaemin"
	Budjet = 1000.0
	Winmoney = 10.0
	def __init__(self,name,money):
		self.Name = name
		self.Budjet = money
	def set_Winmoney(self,money):
		self.Winmoney = money
	def get_Winmoney(self):
		return self.Winmoney
	def get_Budjet(self):
		return self.Budjet
	def print_name(self):
		print(self.Name)
	def print_Budjet(self):
		print(self.Budjet)
	def payout(self,bet_money):
		self.Budjet -= bet_money
	def buyin(self,money_in):
		self.Budjet += money_in
###############################
def Gene_File_Parser2(MLB_File_List):
	MLB_Team_List = []
	MLB_Team_List.append(Team2("Baltimore Orioles"))
	MLB_Team_List.append(Team2("Boston Red Sox"))
	MLB_Team_List.append(Team2("Chicago White Sox"))
	MLB_Team_List.append(Team2("Cleveland Indians"))
	MLB_Team_List.append(Team2("Detroit Tigers"))
	MLB_Team_List.append(Team2("Houston Astros"))
	MLB_Team_List.append(Team2("Kansas City Royals"))
	MLB_Team_List.append(Team2("Los Angeles Angels"))
	MLB_Team_List.append(Team2("Minnesota Twins"))
	MLB_Team_List.append(Team2("New York Yankees"))
	MLB_Team_List.append(Team2("Oakland Athletics"))
	MLB_Team_List.append(Team2("Seattle Mariners"))
	MLB_Team_List.append(Team2("Tampa Bay Rays"))
	MLB_Team_List.append(Team2("Texas Rangers"))
	MLB_Team_List.append(Team2("Toronto Blue Jays"))
	MLB_Team_List.append(Team2("Arizona Diamondbacks"))
	MLB_Team_List.append(Team2("Atlanta Braves"))
	MLB_Team_List.append(Team2("Chicago Cubs"))
	MLB_Team_List.append(Team2("Cincinnati Reds"))
	MLB_Team_List.append(Team2("Colorado Rockies"))
	MLB_Team_List.append(Team2("Los Angeles Dodgers"))
	MLB_Team_List.append(Team2("Miami Marlins"))
	MLB_Team_List.append(Team2("Milwaukee Brewers"))
	MLB_Team_List.append(Team2("New York Mets"))
	MLB_Team_List.append(Team2("Philadelphia Phillies"))
	MLB_Team_List.append(Team2("Pittsburgh Pirates"))
	MLB_Team_List.append(Team2("San Diego Padres"))
	MLB_Team_List.append(Team2("San Francisco Giants"))
	MLB_Team_List.append(Team2("St.Louis Cardinals"))
	MLB_Team_List.append(Team2("Washington Nationals"))
	fin = open(MLB_File_List,'r')
	MLB_List_Out = []
	while 1:
		fin_line = fin.readline()
		if not fin_line:
			break
		if fin_line.find('\014') != -1:
			continue
		if fin_line.find("canc")!=-1:
			continue
		if fin_line.find("post")!=-1:
			continue
		dash      = fin_line.find("-") 
		endname   = max(fin_line.rfind("s"),fin_line.rfind("x"),fin_line.rfind("p"))
		endcolon  = fin_line.rfind(":")
		score_h   = fin_line[endcolon-2:endcolon]
		score_a   = fin_line[endcolon+1:endcolon+3]
		scorediff = int(score_h)-int(score_a)
		enddot    = fin_line.rfind(".")
		endplus   = fin_line.rfind("+")
		endminus  = fin_line.rfind("-")
		endslash  = fin_line.rfind("/")
		slash     = fin_line.find("/")
		bet_luck  = 1
		endpl     = max(endplus,endminus)
	 
		if fin_line.count(".") > 1:
			 odds_h = float(fin_line[enddot-7:enddot-2])
			 odds_a = float(fin_line[enddot-2:enddot+3])
		elif fin_line.count("+")+fin_line.count("-") > 1:
			 if fin_line[endpl-5] == '+':
				 odds_h = 1.0+int(fin_line[endpl-4:endpl-1])/100.0
			 elif fin_line[endpl-5] == '-':  
				 odds_h = 1.0+100.0/int(fin_line[endpl-4:endpl-1])
			 if fin_line[endpl] == '+':
				 odds_a = 1.0+int(fin_line[endpl+1:endpl+4])/100.0
			 elif fin_line[endpl] == '-':
				 odds_a = 1.0+100.0/int(fin_line[endpl+1:endpl+4])
		else:
			odds_h_denom = 0
			odds_h_nom = 0
			for ii in range(3):
				odds_h_t = fin_line[slash-1-ii:slash]
				odds_h_tt = fin_line[slash+1:slash+2+ii]
				odds_a_t = fin_line[endslash-1-ii:endslash]
				odds_a_tt = fin_line[endslash+1:endslash+2+ii]
				if odds_h_t.isdigit() == 1:
					odds_h_denom = odds_h_t
				if odds_h_tt.isdigit() == 1:
					odds_h_nom = odds_h_tt
				if odds_a_t.isdigit() == 1:
					odds_a_denom = odds_a_t
				if odds_a_tt.isdigit() == 1:
					odds_a_nom = odds_a_tt
			odds_h = 1.0 + int(odds_h_denom)*1.0/int(odds_h_nom)
			odds_a = 1.0 + int(odds_a_denom)*1.0/int(odds_a_nom)
		hometeam  = fin_line[6:dash-1]
		awayteam  = fin_line[dash+2:endname+1]
		c_h_cnt = 0
		c_h_trg = 0
		c_a_cnt = 0
		c_a_trg = 0
		MLB_Team_Exist = 2
		for ii in MLB_Team_List:
			if MLB_Team_Exist == 0:
				break
			elif ii.get_Name() == hometeam:
				c_h_trg = 1
				MLB_Team_Exist -= 1
			elif ii.get_Name() == awayteam:
				c_a_trg = 1
				MLB_Team_Exist -= 1
			c_h_cnt = c_h_cnt if c_h_trg else c_h_cnt + 1
			c_a_cnt = c_a_cnt if c_a_trg else c_a_cnt + 1
		if MLB_Team_Exist != 0:
			continue
		List = [c_h_cnt,c_a_cnt,odds_h,odds_a,int(score_h),int(score_a)]
		MLB_List_Out.append(List)
	return MLB_List_Out

def Gene_File_Parser(MLB_File_List):
	MLB_Team_List = []
	MLB_Team_List.append(Team("Baltimore Orioles"))
	MLB_Team_List.append(Team("Boston Red Sox"))
	MLB_Team_List.append(Team("Chicago White Sox"))
	MLB_Team_List.append(Team("Cleveland Indians"))
	MLB_Team_List.append(Team("Detroit Tigers"))
	MLB_Team_List.append(Team("Houston Astros"))
	MLB_Team_List.append(Team("Kansas City Royals"))
	MLB_Team_List.append(Team("Los Angeles Angels"))
	MLB_Team_List.append(Team("Minnesota Twins"))
	MLB_Team_List.append(Team("New York Yankees"))
	MLB_Team_List.append(Team("Oakland Athletics"))
	MLB_Team_List.append(Team("Seattle Mariners"))
	MLB_Team_List.append(Team("Tampa Bay Rays"))
	MLB_Team_List.append(Team("Texas Rangers"))
	MLB_Team_List.append(Team("Toronto Blue Jays"))
	MLB_Team_List.append(Team("Arizona Diamondbacks"))
	MLB_Team_List.append(Team("Atlanta Braves"))
	MLB_Team_List.append(Team("Chicago Cubs"))
	MLB_Team_List.append(Team("Cincinnati Reds"))
	MLB_Team_List.append(Team("Colorado Rockies"))
	MLB_Team_List.append(Team("Los Angeles Dodgers"))
	MLB_Team_List.append(Team("Miami Marlins"))
	MLB_Team_List.append(Team("Milwaukee Brewers"))
	MLB_Team_List.append(Team("New York Mets"))
	MLB_Team_List.append(Team("Philadelphia Phillies"))
	MLB_Team_List.append(Team("Pittsburgh Pirates"))
	MLB_Team_List.append(Team("San Diego Padres"))
	MLB_Team_List.append(Team("San Francisco Giants"))
	MLB_Team_List.append(Team("St.Louis Cardinals"))
	MLB_Team_List.append(Team("Washington Nationals"))
	fin = open(MLB_File_List,'r')
	MLB_List_Out = []
	while 1:
		fin_line = fin.readline()
		if not fin_line:
			break
		if fin_line.find('\014') != -1:
			continue
		if fin_line.find("canc")!=-1:
			continue
		if fin_line.find("post")!=-1:
			continue
		dash      = fin_line.find("-") 
		endname   = max(fin_line.rfind("s"),fin_line.rfind("x"),fin_line.rfind("p"))
		endcolon  = fin_line.rfind(":")
		score_h   = fin_line[endcolon-2:endcolon]
		score_a   = fin_line[endcolon+1:endcolon+3]
		scorediff = int(score_h)-int(score_a)
		enddot    = fin_line.rfind(".")
		endplus   = fin_line.rfind("+")
		endminus  = fin_line.rfind("-")
		endslash  = fin_line.rfind("/")
		slash     = fin_line.find("/")
		bet_luck  = 1
		endpl     = max(endplus,endminus)
	 
		if fin_line.count(".") > 1:
			 odds_h = float(fin_line[enddot-7:enddot-2])
			 odds_a = float(fin_line[enddot-2:enddot+3])
		elif fin_line.count("+")+fin_line.count("-") > 1:
			 if fin_line[endpl-5] == '+':
				 odds_h = 1.0+int(fin_line[endpl-4:endpl-1])/100.0
			 elif fin_line[endpl-5] == '-':  
				 odds_h = 1.0+100.0/int(fin_line[endpl-4:endpl-1])
			 if fin_line[endpl] == '+':
				 odds_a = 1.0+int(fin_line[endpl+1:endpl+4])/100.0
			 elif fin_line[endpl] == '-':
				 odds_a = 1.0+100.0/int(fin_line[endpl+1:endpl+4])
		else:
			odds_h_denom = 0
			odds_h_nom = 0
			for ii in range(3):
				odds_h_t = fin_line[slash-1-ii:slash]
				odds_h_tt = fin_line[slash+1:slash+2+ii]
				odds_a_t = fin_line[endslash-1-ii:endslash]
				odds_a_tt = fin_line[endslash+1:endslash+2+ii]
				if odds_h_t.isdigit() == 1:
					odds_h_denom = odds_h_t
				if odds_h_tt.isdigit() == 1:
					odds_h_nom = odds_h_tt
				if odds_a_t.isdigit() == 1:
					odds_a_denom = odds_a_t
				if odds_a_tt.isdigit() == 1:
					odds_a_nom = odds_a_tt
			odds_h = 1.0 + int(odds_h_denom)*1.0/int(odds_h_nom)
			odds_a = 1.0 + int(odds_a_denom)*1.0/int(odds_a_nom)
		hometeam  = fin_line[6:dash-1]
		awayteam  = fin_line[dash+2:endname+1]
		c_h_cnt = 0
		c_h_trg = 0
		c_a_cnt = 0
		c_a_trg = 0
		MLB_Team_Exist = 2
		for ii in MLB_Team_List:
			if MLB_Team_Exist == 0:
				break
			elif ii.get_Name() == hometeam:
				c_h_trg = 1
				MLB_Team_Exist -= 1
			elif ii.get_Name() == awayteam:
				c_a_trg = 1
				MLB_Team_Exist -= 1
			c_h_cnt = c_h_cnt if c_h_trg else c_h_cnt + 1
			c_a_cnt = c_a_cnt if c_a_trg else c_a_cnt + 1
		if MLB_Team_Exist != 0:
			continue
		List = [c_h_cnt,c_a_cnt,odds_h,odds_a,int(score_h),int(score_a)]
		MLB_List_Out.append(List)
	return MLB_List_Out
