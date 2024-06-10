from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.db.models import Q


from shop.models import Souvenir
from shop.forms import CartAddSouvenirForm
from .models import Team, Player, Gallery, GameSchedule, InterestingFactAboutPlayer


User = get_user_model()


def home_page(request):
    return render(request, 'main/home_page.html')


def tournament_schedule(request):
    return render(request, 'main/tournament-page.html')


def player(request, player_slug):
    player = Player.objects.get(slug=player_slug)
    player_facts = InterestingFactAboutPlayer.objects.filter(player=player)
    return render(request,
                  'main/player-page.html',
                  context={'player': player, 'facts': player_facts})


def team(request, team_slug):
    team = Team.objects.get(slug=team_slug)
    players = Player.objects.filter(team=team)
    gallery = Gallery.objects.all()
    games = GameSchedule.objects.filter(Q(player_one__in=players) | Q(player_two__in=players))
    return render(request, 'main/team-page.html',
                  context={'team': team, 'players': players, 'gallery': gallery, 'games': games})


def teams(request):
    teams = Team.objects.all()
    return render(request, 'main/teams-page.html', context={'teams': teams})


@login_required
def favorite_souvenirs(request):
    favorite_souvenirs = User.objects.get(id=request.user.id).favorite_souvenirs.all()
    cart_souvenir_form = CartAddSouvenirForm()
    return render(
        request,
        'main/favorite.html',
        context={'favorite_souvenirs': favorite_souvenirs, 'cart_souvenir_form': cart_souvenir_form})


@require_POST
@login_required
def add_favorite_souvenirs(request, souvenir_id):
    souvenir = get_object_or_404(Souvenir, id=souvenir_id)
    souvenir.users.add(request.user.id)
    return JsonResponse({'success': 'success', 'souvenir': souvenir.name,
                         'souvenir_id': souvenir.id})


@login_required
def del_favorite_souvenirs(request, souvenir_id):
    Souvenir.objects.get(id=souvenir_id).users.remove(request.user.id)
    return redirect('favorite_souvenirs')