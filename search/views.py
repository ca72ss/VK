from django.shortcuts import render
import vk


def search(request):
    at = '72d9d403e83d27930eabaa1d4e50e16ec394ee69881bd2715fe04b5178b434bd43b2cc3db8d29cdd14b4f'
    session = vk.Session(access_token= at)
    api = vk.API(session)
    users = api.users.search(count=10,  age_from=14, age_to=18, school_year=2017,  fields = "photo_100,last_seen,photo_id,has_mobile,universities")
    del users[0]

    return render(request, 'search/done.html', {'users':users})
