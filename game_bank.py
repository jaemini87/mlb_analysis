__author__ = 'JAEMIN'
class Games():
	#game contains scorediff and odds_H odds_A and counter
	#Example
	# list should be FIFO manner not using append!!
	# use Insert(0,element) and Pop
	# [game1,game2]
	# [game1, cnt1, game2, cnt2]
	# game  = [ score_diff, score_offset, odds_h, odds_a ]
	def __init__ (self,):
		self.games_2 = []
		self.games_3 = []
		self.games_4 = []
	def calibrate(self,game,mode):
		if mode == 0:
			score_a,score_b,odds_a,odds_b = game
			if abs(score_a) > 4:
				score_a = 3 if score_a > 0 else -3
			elif abs(score_a) > 2:
				score_a = 2 if score_a > 0 else -2
			else:
				score_a = 1 if score_a > 0 else -1
			if score_b > 6:
				score_b = 3
			elif score_b > 3:
				score_b = 2
			elif score_b > 1:
				score_b = 1
			else:
				score_b = 0
			if odds_a > 2.39:
				odds_a = 4
			elif odds_a > 2.01:
				odds_a = 3
			elif odds_a > 1.80:
				odds_a = 2
			elif odds_a > 1.68:
				odds_a = 1
			else:
				odds_a = 0
			if odds_b > 2.39:
				odds_b = 4
			elif odds_b > 2.01:
				odds_b = 3
			elif odds_b > 1.8:
				odds_b = 2
			elif odds_b > 1.68:
				odds_b = 1
			else:
				odds_b = 0
		elif mode == 1:
			score_a,score_b,odds_a,odds_b = game
			if abs(score_a) > 2:
				score_a = 2 if score_a>0 else -2
			else:
				score_a = 1 if score_a>0 else -1
			if score_b > 3:
				score_b = 1
			else:
				score_b = 0
			if odds_a > 2.20:
				odds_a = 2
			elif odds_a > 1.80:
				odds_a = 1
			else:
				odds_a = 0
			if odds_b > 2.2:
				odds_b = 2
			elif odds_b > 1.8:
				odds_b = 1
			else:
				odds_b = 0
		elif mode == 2:
			score_a,score_b,odds_a,odds_b = game
			if abs(score_a) > 1:
				score_a = 2 if score_a>0 else -2
			else:
				score_a = 1 if score_a>0 else -1
			if score_b > 2:
				score_b = 1
			else:
				score_b = 0
			if odds_a > odds_b:
				odds_a = 1
			else:
				odds_a = 0
			if odds_b > odds_a:
				odds_b = 1
			else:
				odds_b = 0
		elif mode == 3:
			score_a,score_b,odds_a,odds_b = game
			if abs(score_a) > 5:
				score_a = 4 if score_a > 0 else -4
			elif abs(score_a) > 3:
				score_a = 3 if score_a > 0 else -3
			elif abs(score_a) > 1:
				score_a = 2 if score_a > 0 else -2
			else:
				score_a = 1 if score_a > 0 else -1
			if score_b > 5:
				score_b = 2
			elif score_b > 2:
				score_b = 1
			else:
				score_b = 0
			if odds_a > 1.92:
				odds_a = 0
			else:
				odds_a = 0
			if odds_b > 1.92:
				odds_b = 0
			else:
				odds_b = 0
		elif mode == 4:
			score_a,score_b,odds_a,odds_b = game
			if abs(score_a) > 5:
				score_a = 4 if score_a > 0 else -4
			elif abs(score_a) > 3:
				score_a = 3 if score_a > 0 else -3
			elif abs(score_a) > 1:
				score_a = 2 if score_a > 0 else -2
			else:
				score_a = 1 if score_a > 0 else -1
			if score_b > 5:
				score_b = 2
			elif score_b > 2:
				score_b = 1
			else:
				score_b = 0
			if odds_a > odds_b:
				odds_a = 1
			else:
				odds_a = 0
			if odds_b > odds_a:
				odds_b = 1
			else:
				odds_b = 0
		elif mode == 5:
			score_a,score_b,odds_a,odds_b = game
			if (odds_a < odds_b and score_a > 0) or (odds_a<odds_b and score_a<0):
				odds_a = 1
			else:
				odds_a = 0
			score_a = 1 if score_a > 0 else 0
			score_b = 0
			odds_b = 0
		elif mode == 6:
			score_a,score_b,odds_a,odds_b = game
			if (odds_a < odds_b and score_a > 0) or (odds_a<odds_b and score_a<0):
				odds_b = 1 if min(odds_a,odds_b)<1.75 else 0
				odds_a = 1
			else:
				odds_b = 1 if min(odds_a,odds_b)<1.75 else 0
				odds_a = 0
			score_a = 1 if score_a > 0 else 0
			score_b = 1 if score_b > 5 else 0
		return [score_a,score_b,odds_a,odds_b]
	def Insert_2(self,game,mode):
		m_game1,m_game2 = game
		m_game1 = self.calibrate(m_game1,mode)
		m_game2 = self.calibrate(m_game2,mode)# game 2 is the new one
		check = 0
		for game_i in self.games_2:
			if game_i[0] == m_game1:
				check = 1
				game_i.append(m_game2)
		if check == 0:
			m_game = [m_game1,m_game2]
			self.games_2.append(m_game)
	def Insert_3(self,game,mode):
		m_game1,m_game2,m_game3 = game
		m_game1 = self.calibrate(m_game1,mode)
		m_game2 = self.calibrate(m_game2,mode)
		m_game3 = self.calibrate(m_game3,mode)
		check = 0
		for game_i in self.games_3:
			if game_i[0] == m_game1 and game_i[1] == m_game2:
				check = 1
				game_i.append(m_game3)
		if check == 0:
			m_game = [m_game1,m_game2,m_game3]
			self.games_3.append(m_game)
	def Insert_4(self,game,mode):
		m_game1,m_game2,m_game3,m_game4 = game
		m_game1 = self.calibrate(m_game1,mode)
		m_game2 = self.calibrate(m_game2,mode)
		m_game3 = self.calibrate(m_game3,mode)
		m_game4 = self.calibrate(m_game4,mode)
		check = 0
		for game in self.games_4:
			if game[0] == m_game1 and game[1] == m_game2 and game[2] == m_game3:
				check = 1
				game.append(m_game4)
		if check == 0:
			m_game = [m_game1,m_game2,m_game3,m_game4]
			self.games_4.append(m_game)
	def Get_2(self,game,mode):
		m_game1,m_game2 = game # game 2 is the new one
		m_game1 = self.calibrate(m_game1,mode)
		m_game2 = self.calibrate(m_game2,mode)
		score_h,score_a,m_odds_a,m_odds_b = m_game2
		pick_h = 0
		pick_a = 0
		pick_offset = 0.55
		for game_i in self.games_2:
			if game_i[0] == m_game1:
				for ii in range(len(game_i)):
					if ii > 0:
						score_1,score_2,odds_a,odds_b = game_i[ii]
						if odds_a == m_odds_a and odds_b == m_odds_b:
							if score_1>0:
								pick_h+=1
							else:
								pick_a+=1
		pick_ratio = pick_h*1.0/(pick_h+pick_a) if pick_h+pick_a > 0 else 0
		if pick_ratio == 0 or pick_h + pick_a < 5:
			return 0
		elif pick_ratio > pick_offset:
			return 1
		elif pick_ratio < 1 - pick_offset:
			return -1
		elif pick_ratio < pick_offset and pick_ratio > 1-pick_offset:
			return 0
		else:
			return 0
	def Get_3(self,game,mode):
		m_game1,m_game2,m_game3 = game
		m_game1 = self.calibrate(m_game1,mode)
		m_game2 = self.calibrate(m_game2,mode)
		m_game3 = self.calibrate(m_game3,mode)
		score_h,score_a,m_odds_a,m_odds_b = m_game3
		pick_h = 0
		pick_a = 0
		pick_offset = 0.55
		for game_i in self.games_3:
			if game_i[0] == m_game1 and game_i[1] == m_game2:
				for ii in range(len(game_i)):
					if ii > 1:
						score_1, score_2, odds_a, odds_b = game_i[ii]
						if odds_a == m_odds_a and odds_b == m_odds_b:
							if score_1 > 0:
								pick_h += 1
							else:
								pick_a += 1
		pick_ratio = pick_h*1.0 / (pick_h + pick_a) if pick_h + pick_a > 0 else 0
		if pick_ratio == 0 or pick_h + pick_a < 4:
			return 0
		elif pick_ratio > pick_offset:
			return pick_ratio
		elif pick_ratio < 1.0 - pick_offset:
			return -1
		elif pick_ratio < pick_offset and pick_ratio > 1.0 - pick_offset:
			return 0
		else:
			return 0
	def Get_4(self,game,mode):
		m_game1,m_game2,m_game3,m_game4 = game
		m_game1 = self.calibrate(m_game1,mode)
		m_game2 = self.calibrate(m_game2,mode)
		m_game3 = self.calibrate(m_game3,mode)
		m_game4 = self.calibrate(m_game4,mode)
		score_h,score_a,m_odds_a,m_odds_b = m_game4
		pick_h = 0
		pick_a = 0
		pick_offset = 0.55
		for game_i in self.games_4:
			if game_i[0] == m_game1 and game_i[1] == m_game2 and game_i[2] == m_game3:
				for ii in range(len(game_i)):
					if ii > 2:
						score_1, score_2, odds_a, odds_b = game_i[ii]
						if odds_a == m_odds_a and odds_b == m_odds_b:
							if score_1 > 0:
								pick_h += 1
							else:
								pick_a += 1
		pick_ratio = pick_h*1.0 / (pick_h + pick_a) if pick_h + pick_a > 0 else 0
		if pick_ratio == 0 or pick_h + pick_a < 5:
			return 0
		elif pick_ratio > pick_offset:
			return pick_ratio
		elif pick_ratio < 1.0 - pick_offset:
			return -1
		elif pick_ratio < pick_offset and pick_ratio > 1.0 - pick_offset:
			return 0
		else:
			return 0
	def Print(self):
		print "---------"
		for ii in self.games:
			print ii
		print "---------"
	def Print_Info(self,kmer):
		for ii in self.games:
			index=0
			win = 0.0
			lose = 0.0
			for jj in ii:
				if index > kmer-2:
					if jj[0] > 0:
						win+=1.0
					else:
						lose+=1.0
				index+=1
			if win+lose > 10:
				print str(ii[0])+"\t"+str(win/(win+lose))+"\t"+str(win+lose)






