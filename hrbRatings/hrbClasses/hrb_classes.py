# Race Class
class Race:
	""" Race Class : defines race characteristics """
	def __init__(self, class_scores, score_multipliers, race_date, track, time, race_name, race_class, 
		race_restrictions, major, racetype, distance, prize, going, runners, category, 
		direction, topor):
		# class_score mapping
		self.class_scores = class_scores
		self.score_multipliers = score_multipliers
		self.race_date = race_date
		self.track = track
		self.time = time
		self.race_name = race_name
		self.race_class = race_class
		self.race_restrictions = race_restrictions
		self.major = major
		self.racetype = racetype
		self.distance = distance
		self.prize = prize
		self.going = going
		self.runners = runners
		self.category = category
		self.direction = direction
		self.topor = topor
		self.raceClass = self.set_raceClass()
		self.raceClass_score = self.set_raceClass_score()
		self.raceValue_score = self.set_raceValue_score()
		self.topor_score = self.set_topor_score()
		self.race_score = self.set_race_score()

	def print_race(self):
		msg = (
			f'race_date: {self.race_date}, track: {self.track}, time: {self.time}, '
			f'race_name: {self.race_name}, race_class: {self.race_class}, '
			f'race_restrictions: {self.race_restrictions}, major: {self.major}, '
			f'racetype: {self.racetype}, distance: {self.distance}, prize: {self.prize}, '
			f'going: {self.going}, runners: {self.runners}, category: {self.category}, '
			f'direction: {self.direction}, topor: {self.topor}, raceClass: {self.raceClass}, '
			f'raceClass_score: {self.raceClass_score}, raceValue_score {self.raceValue_score}, '
			f'topor_score: {self.topor_score}, race_score: {self.race_score} '
			)
		print(msg)

	def set_raceClass(self):
		if self.race_class == 'Irish':
			if self.major == 'Non-Major':
				if self.prize < 5000:
					self.raceClass = 'Class 6'
				elif self.prize < 7000:
					self.raceClass = 'Class 5'
				elif self.prize < 10000:
					self.raceClass = 'Class 4'
				elif self.prize < 14000:
					self.raceClass = 'Class 3'
				else:
			 		self.raceClass = 'Class 2'
			else:
				if self.major == 'Group 3':
			 		self.raceClass = 'Group 3'
				elif self.major == 'Group 2':
			 		self.raceClass = 'Group 2'
				elif self.major == 'Group 1':
			 		self.raceClass = 'Group 1'
				else:
			 		# Listed Race
			 		self.raceClass = 'class 1'
		else:
			self.raceClass = self.race_class

		return self.raceClass
		
	def set_raceClass_score(self):
		self.raceClass_score = self.class_scores.get(self.raceClass)

		return self.raceClass_score

	def set_raceValue_score(self):
		round_prize = (self.prize/1000).round(0).astype(int)
		# adjust rounded_prize to <= max_rounded_prize
		if round_prize <= 20:
			rounded_prize = round_prize
		else:
			rounded_prize = 20
		self.raceValue_score = rounded_prize *  self.score_multipliers.get('raceValue_multiplier')

		return self.raceValue_score

	def set_topor_score(self):
		self.topor_score = self.topor * self.score_multipliers.get('topor_multiplier')

		return self.topor_score

	def set_race_score(self):
		self.race_score = sum([self.raceClass_score, self.raceValue_score, self.topor_score])

		return self.race_score

