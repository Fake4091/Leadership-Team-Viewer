from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse
from dataclasses import dataclass

# Create your views here.


@dataclass
class Team:
    teamName: str
    desc: str
    members: list


comTeam = Team(
    "Community",
    "Our job is to plan events that bring people together, build lasting relationships, and promote engagement.",
    ["Arianna", "Peyton"],
)
docTeam = Team(
    "Documentation",
    "Documentation team is responsible for taking photos of guest speaker, community events, and unit projects after taking the pictures depending on the event happening in the photos determines which social media we post on we are also responsible for getting all the photos for the year book.",
    ["Jason", "Patrick"],
)
manTeam = Team(
    "Management",
    "As the Management team we are required to manage all of the chores for each day and who does them. This includes cleaning the kitchen, taking out the trash, sweeping the main lobby & backhallway/classrooms, and wiping all the tables, including the kitchen tables.",
    ["Aidan", "Chris", "Kilan", "Tanner"],
)
procTeam = Team(
    "Procurement",
    "We buy food to cook so that we can feed you guys at lunch time and we buy supplies like soap, trash, bags etc.",
    ["Aaron", "Arthur", "Jacob", "Markel"],
)

teams = {
    "Community": comTeam,
    "Documentation": docTeam,
    "Management": manTeam,
    "Procurement": procTeam,
}


def home_view(request: HttpRequest) -> HttpResponse:
    return render(request, "home.html")


def team_view(request: HttpRequest, teamName) -> HttpResponse:
    print(teamName)
    team = teams[teamName.title()]
    context = {
        "team": team,
    }
    return render(request, "team.html", context)
