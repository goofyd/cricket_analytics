from django.shortcuts import render, get_object_or_404, get_list_or_404
from .models import Score, Match, Innings


def scorecard(request, id):
    match = get_object_or_404(Match, match_number=id)
    innings = get_list_or_404(Innings, match=id)
    summary = []
    for inning in innings:
        score = {}
        score['runs'] = get_list_or_404(Score.objects.order_by('ball_count'), innings=inning)
        score['innings'] = inning
        score['total'] = sum([x.runs for x in score['runs']])
        summary.append(score)
    return render(request, 'scoreboard/score.html', { 'match' : match, 'innings': summary})