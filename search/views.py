from django.shortcuts import render
from django.http import HttpResponse
import vk
from django.contrib.sessions.backends.db import SessionStore

s = SessionStore()
s['at'] = 'c3c55cb015f5c383ec3495eee0fe25b8c8e1a583a07543b3856247c28c41a1103b9c24b388447e6158e56'

def search(request):

    session = vk.Session(access_token= s['at'])
    api = vk.API(session)
    users = api.users.search(count=100,  age_from=14, age_to=18, school_year=2017,  fields = "photo_100,last_seen,photo_id,has_mobile,universities,last_seen,photo_id,has_mobile,universities,can_write_private_message,can_send_friend_request")
    groups = api.groups.getMembers(group_id='142498173')
    print (s['at'])
    del users[0]
    return render(request, 'search/done.html', {'users':users})


def forms(request):

    return render(request, 'search/forms.html')


def get_name(request):
    session = vk.Session(access_token= s['at'])
    api = vk.API(session)

    city_name = 'Шостка'
    school_num = 'школа 5'
    UA_CID = api.database.getCountries(code='UA')[0]['cid']
    CITY = api.database.getCities(country_id=UA_CID, q=city_name)
    nc = 0
    CITY_ID = CITY[nc]['cid']
    SCHOOL =  api.database.getSchools(q=school_num,city_id=CITY_ID)
    SCHOOL_ID = SCHOOL[1]['id']


    if 'your_name' in request.GET and request.GET['your_name']:
        your_name = request.GET['your_name']


        users = api.users.search(count=10,city=CITY_ID, country=UA_CID, age_from=14, age_to=24, school_year=2012, school = SCHOOL_ID, fields = "photo_100,last_seen,photo_id,has_mobile,universities,last_seen,photo_id,has_mobile,universities,can_write_private_message,can_send_friend_request")
        groups = api.groups.getMembers(group_id='142498173')
        print (groups)
        del users[0]
        return render(request, 'search/done.html', {'your_name': your_name, 'users':users})
    else:
        return HttpResponse('Please submit a search term.')

def getGroupUsers(request):
    session = vk.Session(access_token= s ['at'])
    api = vk.API(session)
    groupsUsers = api.groups.getMembers(group_id = '127378018',fields = "photo_100,last_seen,photo_id,has_mobile,universities,last_seen,photo_id,has_mobile,universities,can_write_private_message,can_send_friend_request")
    groupsUsers2 = api.groups.getMembers(group_id = '43325743',fields = "photo_100,last_seen,photo_id,has_mobile,universities,last_seen,photo_id,has_mobile,universities,can_write_private_message,can_send_friend_request")
    group_1 = groupsUsers['users']
    group_2 = groupsUsers2['users']
    request.session['groups1'] = group_1
    request.session['groups2'] = group_2
    return render(request, 'search/done.html', {'users':group_1})

def intersection(request):
    session = vk.Session(access_token = s['at'])
    api=vk.API(session)
    groupsUsers = api.groups.getMembers(group_id = '127378018',fields = "photo_100,last_seen,photo_id,has_mobile,universities,last_seen,photo_id,has_mobile,universities,can_write_private_message,can_send_friend_request")
    groupsUsers2 = api.groups.getMembers(group_id = '43325743',fields = "photo_100,last_seen,photo_id,has_mobile,universities,last_seen,photo_id,has_mobile,universities,can_write_private_message,can_send_friend_request")
    group_1 = groupsUsers['users']
    group_2 = groupsUsers2['users']
    gu1=[u['uid'] for u in group1]
    gu2=[u['uid'] for u in group2]
    result=list(set(gu1) & set(gu2))
    users = api.users.get(user_ids = result,fields = "photo_100,last_seen,photo_id,has_mobile,universities,last_seen,photo_id,has_mobile,universities,can_write_private_message,can_send_friend_request")
    print (users)
    return render(request, 'search/done.html', {'users':users})

def message(request,arg):
    session = vk.Session(access_token= s ['at'])
    api = vk.API(session)
    id = request.args.get('id')
    ud = api.users.get(user_ids=id,fields='last_seen,photo_id,has_mobile,universities,can_write_private_message,can_send_friend_request')[0]
    print (id)
    print(ud)
    return render(request, 'search/test.html')
