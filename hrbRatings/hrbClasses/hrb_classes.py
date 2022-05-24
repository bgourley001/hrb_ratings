import pandas as pd
import numpy as np
from hrbClasses import score_settings

# Race Class
class Race:
	""" Race Class : defines race characteristics """
	def __init__(self, race_date, track, time, race_name, race_class, 
		race_restrictions, major, racetype, distance, prize, going, runners, category, 
		direction, topor):
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
		self.runners = runners.astype(int)
		self.category = category
		self.direction = direction
		self.topor = topor
		self.places = self.get_no_of_places()
		self.raceClass = self.set_raceClass()
		self.raceClass_score = self.set_raceClass_score()
		self.raceValue_score = self.set_raceValue_score()
		self.topor_score = self.set_topor_score()
		self.race_score = self.set_race_score()

	def get_no_of_places(self):
		if self.runners < 5:
			self.places = 1
		elif self.runners < 8:
			self.places = 2
		elif self.runners < 16:
			self.places = 3
		else:
			self.places = 4

		return self.places

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
		classScores = score_settings.ScoreClass()
		self.raceClass_score = classScores.get_class_score(self.raceClass)

		return self.raceClass_score

	def set_raceValue_score(self):
		setting = score_settings.RaceScoreMultiplier()
		round_prize = (self.prize/1000).round(0).astype(int)
		# adjust rounded_prize to <= max_rounded_prize
		if round_prize <= 20:
			rounded_prize = round_prize
		else:
			rounded_prize = 20
		self.raceValue_score = rounded_prize *  setting.get_race_score_multiplier('raceValue')

		return self.raceValue_score

	def set_topor_score(self):
		setting = score_settings.RaceScoreMultiplier()
		self.topor_score = self.topor * setting.get_race_score_multiplier('topor')

		return self.topor_score

	def set_race_score(self):
		self.race_score = sum([self.raceClass_score, self.raceValue_score, self.topor_score])

		return self.race_score

	def set_horse_entries(self, horse_entries):
		self.horse_entries = horse_entries

		return self.horse_entries

	def get_horse_entries(self):
		return self.horse_entries

	def get_runners(self):
		return self.runners

	def get_race_date(self):
		return self.race_date

	def get_track(self):
		return self.track

	def get_time(self):
		return self.time

	def process_horse_entries(self):
		self.prior_form_total = 0
		for entry in self.get_horse_entries():
			horse_msg = (
				f'horse: {entry.get_horseName()}, form: {entry.get_form()}, '
				f'prior_form: {entry.get_prior_form()}, '
				f'prior_form_score: {entry.set_prior_form_score(self.places)} '
				)
			print(horse_msg)
			self.prior_form_total += entry.get_prior_form_score()
		self.race_score += self.prior_form_total
		print()

	def print_race(self):
			race_msg = (
				f'race_date: {self.race_date}, track: {self.track}, time: {self.time}, '
				f'race_name: {self.race_name}, race_class: {self.race_class}, '
				f'race_restrictions: {self.race_restrictions}, major: {self.major}, '
				f'racetype: {self.racetype}, distance: {self.distance}, prize: {self.prize}, '
				f'going: {self.going}, runners: {self.runners}, category: {self.category}, '
				f'direction: {self.direction}, topor: {self.topor}, places: {self.places}, '
				f'raceClass: {self.raceClass}, raceClass_score: {self.raceClass_score}, '
				f'raceValue_score {self.raceValue_score}, topor_score: {self.topor_score}, '
				f'prior_form_total: {self.prior_form_total}, race_score: {self.race_score} '
				)
			print(race_msg)

class Horse:
	""" Horse Class : defines Horse characteristics """
	def __init__(self, horse, horse_form):
		self.horseName = horse
		# self.OfficialRating = OfficialRating
		# self.LastRun = LastRun
		self.form = horse_form

	def get_horseName(self):
		return self.horseName

	def get_form(self):
		return self.form

	def get_prior_form(self):
		# prior form
		position = -1
		self.prior_form = pd.to_numeric(self.form[position], errors='coerce')

		return self.prior_form

	def set_prior_form_score(self, places):
		setting = score_settings.HorseScoreMultiplier()
		self.prior_form_score = 0
		if self.prior_form <= places:
			if self.prior_form > 1:
				self.prior_form_score = setting.get_horse_score_multiplier('prior_place')
			elif self.prior_form == 1:
				self.prior_form_score = setting.get_horse_score_multiplier('prior_win')

		return self.prior_form_score

	def get_prior_form_score(self):
		return self.prior_form_score

	def print_horse(self):
		msg = (
			f'horseName: {get_horseName()}, form: {get_form()}, prior_form: {get_prior_form()}, '
			f'prior_form_score: {get_prior_form_score()} '
			)
		print(msg)

