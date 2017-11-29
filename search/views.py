from django.shortcuts import render
from django.http import HttpResponse
import vk
from django.contrib.sessions.backends.db import SessionStore
from requests.exceptions import ConnectionError
import vk.exceptions
from collections import Counter
import time

def login(request):
    return render (request,'search/login.html')

def logout(request):
    del request.session['at']
    alert = 'Куки очищены'
    return render (request,'search/test.html',{'alert':alert})

def get_at(request):

    if 'at' in request.GET and request.GET['at']:
        request.session['at'] =request.GET['at']
    return render (request,'search/forms.html')

def search(request):

    at = request.session.get('at', '')
    session = vk.Session(access_token= at)
    api = vk.API(session)
    try:
        users = api.users.search(count=100,  age_from=14, age_to=18, school_year=2017,  fields = "photo_100,last_seen,photo_id,has_mobile,universities,last_seen,photo_id,has_mobile,universities,can_write_private_message,can_send_friend_request")
    except vk.exceptions.VkAPIError as e:
        alert = 'Введите ваш токен'
        return render (request,'search/login.html', {'alert':alert})
    else:
        print ('Все гуд')
        groups = api.groups.getMembers(group_id='142498173')
        print (at)
        del users[0]
        return render(request, 'search/done.html', {'users':users})


def forms(request):

    return render(request, 'search/forms.html')


def get_name(request):

    at = request.session.get('at', '')
    session = vk.Session(access_token= at)
    api=vk.API(session)

    city = request.GET['city']
    school = request.GET['school']
    school_year = request.GET['school_year']
    request.session['groups_s'] =request.GET['groups']

    UA_CID = api.database.getCountries(code='UA')[0]['cid']
    CITY = api.database.getCities(country_id=UA_CID, q=city)
    nc = 0
    CITY_ID = CITY[nc]['cid']
    SCHOOL =  api.database.getSchools(q=school,city_id=CITY_ID)
    SCHOOL_ID = SCHOOL[1]['id']
    ids_s = []

    users_s = api.users.search(count=1000,country=UA_CID, age_from=0, age_to=99, school_year=school_year, school = SCHOOL_ID, fields = "photo_100,last_seen,photo_id,has_mobile,universities")
    del users_s[0]
    for u in users_s:
        ids_s.append(str(u['uid']))
    print (ids_s)

    groups_s = request.session.get('groups_s', '')
    test = groups_s.split("\n")
    res = []
    #c = api.execute(code='return API.users.get({"user_ids": API.audio.search({"q":"Beatles", "count":3}).items@.owner_id})@.last_name')
    #print (c)
    #of = 0
    #while of<300000:
    for x in test:
        groupsUsers = api.groups.getMembers(group_id = x, fields = "photo_100")
        #of+=1000
        group_1 = groupsUsers['users']
        gu1=[u['uid'] for u in group_1]
        res.extend(gu1)
        #time.sleep(0.33)

    resul = Counter(res)
    result = dict(resul)
    print (result)
    ids=[]
    for key, value in result.items():
        if value>1:
            ids.append(str(key))
    result_ids=list(set(ids) & set(ids_s))
    print (ids)
    print(result_ids)

    users = api.users.get(user_ids = result_ids,fields = "photo_100,last_seen,photo_id,has_mobile,universities,last_seen,photo_id,has_mobile,universities,can_write_private_message,can_send_friend_request")
    return render(request, 'search/done.html', {'users':users})


def intersection(request):
    at = request.session.get('at', '')
    session = vk.Session(access_token= at)
    api=vk.API(session)
    groups_s = request.session.get('groups_s', '')
    test = groups_s.split(',')
    groupsUsers = api.groups.getMembers(group_id = test[0],fields = "photo_100,last_seen,photo_id,has_mobile,universities,last_seen,photo_id,has_mobile,universities,can_write_private_message,can_send_friend_request")
    groupsUsers2 = api.groups.getMembers(group_id = test[1],fields = "photo_100,last_seen,photo_id,has_mobile,universities,last_seen,photo_id,has_mobile,universities,can_write_private_message,can_send_friend_request")
    group_1 = groupsUsers['users']
    group_2 = groupsUsers2['users']
    gu1=[u['uid'] for u in group_1]
    gu2=[u['uid'] for u in group_2]
    result=list(set(gu1) & set(gu2))
    users = api.users.get(user_ids = result,fields = "photo_100,last_seen,photo_id,has_mobile,universities,last_seen,photo_id,has_mobile,universities,can_write_private_message,can_send_friend_request")
    print (test[0])
    return render(request, 'search/done.html', {'users':users})
    

def message(request):

    at = request.session.get('at', '')
    session = vk.Session(access_token= at)
    api = vk.API(session)
    us_id = request.GET.get('id')
    users = api.users.get(user_ids=us_id,fields='last_seen,photo_id,has_mobile,universities,can_write_private_message,can_send_friend_request')[0]
    print (us_id)
    return render(request, 'search/test.html', {'users':users})
