# Race Class
class Race:
	""" Race Class : defines race characteristics """
	def __init__(self, race_date, track, time, race_name, race_class, race_restrictions, 
		major, racetype, distance, prize, going, runners, category, direction):
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

	def print_race(self):
		msg = (
			f'race_date: {self.race_date}, track: {self.track}, time: {self.time}, '
			f'race_name: {self.race_name}, race_class: {self.race_class}, '
			f'race_restrictions: {self.race_restrictions}, major: {self.major}, '
			f'racetype: {self.racetype}, distance: {self.distance}, prize: {self.prize}, '
			f'going: {self.going}, runners: {self.runners}, category: {self.category}, '
			f'direction: {self.direction}'
			)
		print(msg)
		

