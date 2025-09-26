from django.shortcuts import render
import time
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)
logging.basicConfig(level=logging.INFO)

def home(request):
    return render(request, "djar/home.html", {"a": 1})


def view1(request):
    return render(request, "djar/template1.html", {"a": 1})


def view2(request, seconds=0):
    log.info(f"view2 {seconds=}")
    if seconds:
        time.sleep(seconds)
    else:
        seconds = 3
        time.sleep(seconds)

    return render(request, "djar/template2.html", {"seconds": seconds})