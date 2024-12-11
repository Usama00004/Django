from django.http import HttpResponse,JsonResponse

def home_page(request):
    print("Home page requested")
    list_friends = ["Usama","Bilal","Faizan","Shammas"]
    return JsonResponse(list_friends,safe=False)