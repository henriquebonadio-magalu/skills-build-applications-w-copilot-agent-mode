from django.test import TestCase
from .models import User, Team, Activity, Workout, Leaderboard

class BasicModelTest(TestCase):
    def setUp(self):
        self.team = Team.objects.create(name='Marvel', description='Marvel Team')
        self.user = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=self.team, is_superhero=True)
        self.workout = Workout.objects.create(name='Pushups', description='Upper body workout')
        self.activity = Activity.objects.create(user=self.user, type='Running', duration=30, date='2025-10-15')
        self.leaderboard = Leaderboard.objects.create(team=self.team, points=100)

    def test_user_creation(self):
        self.assertEqual(self.user.name, 'Spider-Man')
        self.assertEqual(self.user.team.name, 'Marvel')

    def test_activity(self):
        self.assertEqual(self.activity.type, 'Running')
        self.assertEqual(self.activity.duration, 30)

    def test_leaderboard(self):
        self.assertEqual(self.leaderboard.points, 100)
