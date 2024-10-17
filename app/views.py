from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

# Create your views here.


def home_view(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "home.html", context)


def community_view(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "community.html", context)


def documentation_view(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "documentation.html", context)


def management_view(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "management.html", context)


def procurement_view(request: HttpRequest) -> HttpResponse:
    context = {}
    return render(request, "procurement.html", context)
