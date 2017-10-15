from django.shortcuts import render
from django.http import HttpResponse
import vk

def search(request):
    at = '72d9d403e83d27930eabaa1d4e50e16ec394ee69881bd2715fe04b5178b434bd43b2cc3db8d29cdd14b4f'
    session = vk.Session(access_token= at)
    api = vk.API(session)
    users = api.users.search(count=100,  age_from=14, age_to=18, school_year=2017,  fields = "photo_100,last_seen,photo_id,has_mobile,universities")
    groups = api.groups.getMembers(group_id='142498173')
    print (groups)
    del users[0]
    return render(request, 'search/done.html', {'users':users})


def forms(request):

    return render(request, 'search/forms.html')


def get_name(request):
    if 'your_name' in request.GET and request.GET['your_name']:
        your_name = request.GET['your_name']
        return render(request, 'search/test.html', {'your_name': your_name})
    else:
        return HttpResponse('Please submit a search term.')
