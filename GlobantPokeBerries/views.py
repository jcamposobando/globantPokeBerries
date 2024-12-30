from django.http import JsonResponse


def allBerryStats(request):
    return JsonResponse({'foo':'bar'})