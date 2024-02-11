from django.shortcuts import render
import logging
from django.http import HttpResponse

logger = logging.getLogger(__name__)

def index(request):
    logger.info('Index page was requested.')
    return render(request, "index.html")

def about(request):
    logger.info('About page was requested.')
    return render(request, "about.html")
