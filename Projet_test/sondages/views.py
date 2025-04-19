from django.shortcuts import render
from django.http import JsonResponse
from sondages.models import Choice

def choice_json(request):
    results = {"sondages": []}
    for choice in Choice.objects.all():
        line = [str(choice), []]
        for question in choice.question_set.all():
            line[1].append(str(question))
        results["sondages"].append(line)
    return JsonResponse(results)