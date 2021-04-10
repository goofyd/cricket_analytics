from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Score, Match, Innings


def scorecard(request, id):
    match = get_object_or_404(Match, match_number=id)
    innings = get_list_or_404(Innings, match=id)
    summary = []
    for inning in innings:
        score = {}
        score['runs'] = get_list_or_404(Score.objects.order_by('ball_count'), innings=inning)
        score['scoreboard'] = get_induvidual_scores(score['runs'])
        score['innings'] = inning
        score['total'] = sum([x.runs for x in score['runs']])
        score['wkts'] = sum([1 for x in score['runs'] if x.action == 'WICKET'])
        score['overs'] = max([x.ball_count for x in score['runs']])
        summary.append(score)
    return render(request, 'scoreboard/score.html', { 'match' : match, 'innings': summary})

def get_induvidual_scores(obj):
    players = {}
    for o in obj:
        if o.batsman in players.keys():
            players[o.batsman] = int(players.get(o.batsman)) + int(o.runs)
        else:
            players[o.batsman] = 0
    print(players)
    return players