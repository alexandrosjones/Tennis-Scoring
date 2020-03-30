import unittest


POINTS = ('0', '15', '30', '40')


def increment_point(player_points, scorer):
	if player_points == ['40', '40']:
		scorer_points = 'ADV'
	else:
		try:
			scorer_points = POINTS[POINTS.index(player_points[scorer]) + 1]
		except IndexError:
			scorer_points = 'WIN'
	return scorer_points


def point_scored(score, scorer):
	scorer -= 1
	loser = abs(1 - scorer)
	player_points = score.split()
	if player_points[loser] == 'ADV':
		player_points[loser] = '40'
	elif player_points[scorer] == 'ADV':
		player_points[scorer] = 'WIN'
	else:
		player_points[scorer] = increment_point(player_points, scorer)
	return ' '.join(player_points)


class TennisTest(unittest.TestCase):
	
	def test_server_scores_an_incrementing_point(self):
		self.assertEqual('15 0', point_scored('0 0', 1))
	
	def test_receiver_scores_an_incrementing_point(self):
		self.assertEqual('15 15', point_scored('15 0', 2))
	
	def test_player_takes_advantage_at_deuce(self):
		self.assertEqual('ADV 40', point_scored('40 40', 1))
		self.assertEqual('40 ADV', point_scored('40 40', 2))
		
	def test_either_player_saves_game_point(self):
		self.assertEqual('40 40', point_scored('40 ADV', 1))
		self.assertEqual('40 40', point_scored('ADV 40', 2))
	
	def test_either_player_wins_game_from_advantage(self):
		self.assertEqual('WIN 40', point_scored('ADV 40', 1))
		self.assertEqual('40 WIN', point_scored('40 ADV', 2))
		
	def test_wins_game_by_two_clear_points(self):
		self.assertEqual('30 WIN', point_scored('30 40', 2))
		self.assertEqual('WIN 0', point_scored('40 0', 1))

	
if __name__ == '__main__':
	unittest.main()