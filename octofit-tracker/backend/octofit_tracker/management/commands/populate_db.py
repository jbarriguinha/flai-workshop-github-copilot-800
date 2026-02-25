from django.core.management.base import BaseCommand
from octofit_tracker.models import User, Team, Activity, Leaderboard, Workout
from datetime import date


class Command(BaseCommand):
    help = 'Populate the octofit_db database with test data'

    def handle(self, *args, **kwargs):
        # Delete existing data
        Leaderboard.objects.all().delete()
        Activity.objects.all().delete()
        Team.objects.all().delete()
        User.objects.all().delete()
        Workout.objects.all().delete()

        self.stdout.write('Existing data cleared.')

        # Create users (Superheroes)
        users_data = [
            {'email': 'ironman@avengers.com', 'name': 'Tony Stark', 'age': 45, 'username': 'ironman', 'password': 'pepper123'},
            {'email': 'thor@avengers.com', 'name': 'Thor Odinson', 'age': 1500, 'username': 'thor', 'password': 'mjolnir123'},
            {'email': 'blackwidow@avengers.com', 'name': 'Natasha Romanoff', 'age': 35, 'username': 'blackwidow', 'password': 'shield123'},
            {'email': 'spiderman@avengers.com', 'name': 'Peter Parker', 'age': 22, 'username': 'spiderman', 'password': 'spidey123'},
            {'email': 'captainamerica@avengers.com', 'name': 'Steve Rogers', 'age': 105, 'username': 'captainamerica', 'password': 'shield456'},
            {'email': 'batman@justiceleague.com', 'name': 'Bruce Wayne', 'age': 40, 'username': 'batman', 'password': 'gotham123'},
            {'email': 'superman@justiceleague.com', 'name': 'Clark Kent', 'age': 35, 'username': 'superman', 'password': 'krypton123'},
            {'email': 'wonderwoman@justiceleague.com', 'name': 'Diana Prince', 'age': 800, 'username': 'wonderwoman', 'password': 'themyscira123'},
            {'email': 'flash@justiceleague.com', 'name': 'Barry Allen', 'age': 28, 'username': 'flash', 'password': 'speedforce123'},
            {'email': 'aquaman@justiceleague.com', 'name': 'Arthur Curry', 'age': 38, 'username': 'aquaman', 'password': 'atlantis123'},
        ]

        users = {}
        for ud in users_data:
            user = User.objects.create(**ud)
            users[ud['username']] = user
            self.stdout.write(f"Created user: {ud['name']}")

        # Create teams
        team_marvel = Team.objects.create(name='Team Marvel')
        team_marvel.members.add(
            users['ironman'], users['thor'], users['blackwidow'],
            users['spiderman'], users['captainamerica']
        )

        team_dc = Team.objects.create(name='Team DC')
        team_dc.members.add(
            users['batman'], users['superman'], users['wonderwoman'],
            users['flash'], users['aquaman']
        )

        self.stdout.write('Created teams: Team Marvel, Team DC')

        # Create activities
        activities_data = [
            {'user': users['ironman'], 'activity_type': 'Running', 'duration': 45, 'date': date(2026, 2, 1)},
            {'user': users['thor'], 'activity_type': 'Weightlifting', 'duration': 60, 'date': date(2026, 2, 2)},
            {'user': users['blackwidow'], 'activity_type': 'Yoga', 'duration': 30, 'date': date(2026, 2, 3)},
            {'user': users['spiderman'], 'activity_type': 'Cycling', 'duration': 50, 'date': date(2026, 2, 4)},
            {'user': users['captainamerica'], 'activity_type': 'Swimming', 'duration': 40, 'date': date(2026, 2, 5)},
            {'user': users['batman'], 'activity_type': 'Martial Arts', 'duration': 90, 'date': date(2026, 2, 1)},
            {'user': users['superman'], 'activity_type': 'Flying', 'duration': 120, 'date': date(2026, 2, 2)},
            {'user': users['wonderwoman'], 'activity_type': 'Sword Training', 'duration': 75, 'date': date(2026, 2, 3)},
            {'user': users['flash'], 'activity_type': 'Sprinting', 'duration': 15, 'date': date(2026, 2, 4)},
            {'user': users['aquaman'], 'activity_type': 'Swimming', 'duration': 60, 'date': date(2026, 2, 5)},
        ]

        for ad in activities_data:
            Activity.objects.create(**ad)
        self.stdout.write('Created activities.')

        # Create leaderboard entries
        leaderboard_data = [
            {'user': users['ironman'], 'score': 950},
            {'user': users['thor'], 'score': 980},
            {'user': users['blackwidow'], 'score': 870},
            {'user': users['spiderman'], 'score': 910},
            {'user': users['captainamerica'], 'score': 960},
            {'user': users['batman'], 'score': 990},
            {'user': users['superman'], 'score': 1000},
            {'user': users['wonderwoman'], 'score': 975},
            {'user': users['flash'], 'score': 920},
            {'user': users['aquaman'], 'score': 880},
        ]

        for ld in leaderboard_data:
            Leaderboard.objects.create(**ld)
        self.stdout.write('Created leaderboard entries.')

        # Create workouts
        workouts_data = [
            {
                'name': 'Avengers Strength Circuit',
                'description': 'A high-intensity strength training circuit for Marvel heroes',
                'exercises': ['Push-ups x50', 'Pull-ups x30', 'Squats x50', 'Deadlift 200kg x5']
            },
            {
                'name': 'Justice League Cardio Blast',
                'description': 'Cardio workout inspired by DC hero training regimens',
                'exercises': ['5km Run', 'Jump Rope 10min', 'Swimming 1km', 'Cycling 20km']
            },
            {
                'name': 'Iron Man Tech Training',
                'description': 'Precision training for enhanced suit operation',
                'exercises': ['Core Stability x20min', 'Balance Training x15min', 'Reaction Drills x20min']
            },
            {
                'name': 'Batman Combat Prep',
                'description': 'Combat and agility training for Gotham\'s Dark Knight',
                'exercises': ['Martial Arts 1hr', 'Obstacle Course 30min', 'Grappling 30min']
            },
            {
                'name': 'Speed Force Workout',
                'description': 'Flash-inspired speed and endurance workout',
                'exercises': ['100m Sprint x20', 'Agility Ladder 20min', 'Plyometrics 30min']
            },
        ]

        for wd in workouts_data:
            Workout.objects.create(**wd)
        self.stdout.write('Created workouts.')

        self.stdout.write(self.style.SUCCESS('Database populated successfully with superhero test data!'))
