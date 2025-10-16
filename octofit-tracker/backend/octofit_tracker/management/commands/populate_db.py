from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Workout, Leaderboard
from datetime import date

class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Apaga dados antigos
        Activity.objects.all().delete()
        Workout.objects.all().delete()
        Leaderboard.objects.all().delete()
        User.objects.all().delete()
        Team.objects.all().delete()

        # Cria times
        marvel = Team.objects.create(name='Marvel', description='Time Marvel')
        dc = Team.objects.create(name='DC', description='Time DC')

        # Cria usuários super-heróis
        spiderman = User.objects.create(name='Spider-Man', email='spiderman@marvel.com', team=marvel, is_superhero=True)
        ironman = User.objects.create(name='Iron Man', email='ironman@marvel.com', team=marvel, is_superhero=True)
        batman = User.objects.create(name='Batman', email='batman@dc.com', team=dc, is_superhero=True)
        superman = User.objects.create(name='Superman', email='superman@dc.com', team=dc, is_superhero=True)

        # Cria atividades
        Activity.objects.create(user=spiderman, type='Corrida', duration=30, date=date.today())
        Activity.objects.create(user=ironman, type='Ciclismo', duration=45, date=date.today())
        Activity.objects.create(user=batman, type='Natação', duration=25, date=date.today())
        Activity.objects.create(user=superman, type='Musculação', duration=60, date=date.today())

        # Cria treinos
        w1 = Workout.objects.create(name='Treino Força', description='Treino para força geral')
        w2 = Workout.objects.create(name='Treino Cardio', description='Treino para resistência cardiovascular')
        w1.suggested_for.add(spiderman, batman)
        w2.suggested_for.add(ironman, superman)

        # Cria leaderboard
        Leaderboard.objects.create(team=marvel, points=150)
        Leaderboard.objects.create(team=dc, points=120)

        self.stdout.write(self.style.SUCCESS('octofit_db populado com dados de teste!'))
