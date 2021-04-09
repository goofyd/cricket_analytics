from django.db import models


class Tournament(models.Model):
    tournament_name = models.CharField(max_length=100)
    start_date = models.DateTimeField('start date')
    end_date = models.DateTimeField('end date')

    def __str__(self):
        return self.tournament_name


class Team(models.Model):
    team_name = models.CharField(max_length=100)
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)

    def __str__(self):
        return self.team_name


class Player(models.Model):
    player_first_name = models.CharField(max_length=50, default='')
    player_middle_name = models.CharField(max_length=50, blank=True, null=True)
    player_last_name = models.CharField(max_length=50, default='')
    player_dob = models.DateField('birth date', blank=True, null=True)
    player_jersey_number = models.IntegerField(blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return '{} {}'.format(self.player_first_name, self.player_last_name)


class Venue(models.Model):
    venue_name = models.CharField(max_length=200)
    capacity = models.IntegerField()
    city = models.CharField(max_length=50, null=True, blank=True)
    state = models.CharField(max_length=50, null=True, blank=True)
    country = models.CharField(max_length=50)

    def __str__(self):
        return self.venue_name


class MatchType(models.Model):
    match_type = models.CharField(max_length=20)
    balls = models.IntegerField()
    ball_color = models.CharField(max_length=10)

    def __str__(self):
        return self.match_type


class Match(models.Model):
    tournament = models.ForeignKey(Tournament, on_delete=models.CASCADE)
    match_number = models.IntegerField()
    home_team = models.ForeignKey(Team, related_name='home', blank=False, null=False, on_delete=models.CASCADE)
    away_team = models.ForeignKey(Team, related_name='away', blank=False, null=False, on_delete=models.CASCADE)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE)
    match_date_time = models.DateTimeField('match start')
    match_type = models.ForeignKey(MatchType, on_delete=models.CASCADE)
    toss = models.ForeignKey(Team, related_name='toss', on_delete=models.CASCADE, null=True, blank=True)
    result = models.ForeignKey(Team, related_name='result', on_delete=models.CASCADE, null=True, blank=True)
    mom = models.ForeignKey(Player, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return 'Match {} - {} vs {}'.format(self.match_number, self.home_team, self.away_team)


class Innings(models.Model):
    innings_number = models.IntegerField()
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.match) + ' ' + '(Innings ' + str(self.innings_number) + ')'


class Score(models.Model):
    innings = models.ForeignKey(Innings, on_delete=models.CASCADE, null=True, blank=True, default=2)
    ball_count = models.IntegerField()
    batsman = models.ForeignKey(Player, related_name='batsman', on_delete=models.CASCADE)
    runs = models.IntegerField(default=0)
    action = models.CharField(max_length=10, default='', null=True, blank=True)
    comment = models.CharField(max_length=100, null=True, blank=True)
    bowler = models.ForeignKey(Player, related_name='bowler', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        if self.action is None:
            return str(self.runs) + " (" + str(self.ball_count) + ")" + " - " + str(self.bowler) + " to " + str(self.batsman)
        else:
            return str(self.action) + " (" + str(self.ball_count) + ")" + " - " + str(self.bowler) + " to " + str(self.batsman)