# file to contain score and settings classes
class ScoreClass:
	def __init__(self):
		# class_score mapping
		self.class_scores = {
			'Class 7' : 80,
			'Class 6' : 85,
			'Class 5' : 90,
			'Class 4' : 95,
			'Class 3' : 100,
			'Class 2' : 105,
			'Class 1' : 110,
			'Group 3' : 115,
			'Group 2' : 120,
			'Group 1' : 125	
		}

	def get_class_score(self, race_class):
		return self.class_scores.get(race_class)

class RaceScoreMultiplier:
	def __init__(self):
		# score multiplier mapping
		self.race_score_multipliers = {
			'raceValue' : 1,
			'topor' : 1
		}
	
	def get_race_score_multiplier(self, setting):
		return self.race_score_multipliers.get(setting)

class HorseScoreMultiplier:
	def __init__(self):
		# horse score multiplier mapping
		self.horse_score_multipliers = {
			'prior_win' : 2,
			'prior_place' : 1
		}
	
	def get_horse_score_multiplier(self, setting):
		return self.horse_score_multipliers.get(setting)


