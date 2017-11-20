from django.shortcuts import render
from django.http import HttpResponse
import vk
from django.contrib.sessions.backends.db import SessionStore

def login(request):
    return render (request,'search/login.html')

def get_at(request):

    if 'at' in request.GET and request.GET['at']:
        request.session['at'] =request.GET['at']
    return render (request,'search/forms.html')

def search(request):

    at = request.session.get('at', '')
    session = vk.Session(access_token= at)
    api = vk.API(session)
    users = api.users.search(count=100,  age_from=14, age_to=18, school_year=2017,  fields = "photo_100,last_seen,photo_id,has_mobile,universities,last_seen,photo_id,has_mobile,universities,can_write_private_message,can_send_friend_request")
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

    if 'your_name' in request.GET and request.GET['your_name']:
        your_name = request.GET['your_name']
        request.session['groups_s'] =request.GET['groups']

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
        print (test)
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
    print (test)
    return render(request, 'search/done.html', {'users':users})

def message(request,arg):
    
    at = request.session.get('at', '')
    session = vk.Session(access_token= at)
    api = vk.API(session)
    id = request.args.get('id')
    ud = api.users.get(user_ids=id,fields='last_seen,photo_id,has_mobile,universities,can_write_private_message,can_send_friend_request')[0]
    print (id)
    print(ud)
    return render(request, 'search/test.html')
