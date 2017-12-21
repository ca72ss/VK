from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import vk
from django.contrib.sessions.backends.db import SessionStore
from requests.exceptions import ConnectionError
import vk.exceptions
from collections import Counter
import time
from .models import Post
from django.utils import timezone
from .forms import PostForm
from django.shortcuts import redirect
<<<<<<< HEAD
import json

def login(request):
    return render(request, 'search/login.html')

=======

def login(request):
    return render (request,'search/login.html')
>>>>>>> 161d3843e3aac5b19729ea055c06c9f531a755a7

def logout(request):
    del request.session['at']
    alert = 'Куки очищены'
<<<<<<< HEAD
    return render(request, 'search/test.html', {'alert': alert})


def get_at(request):
    if 'at' in request.GET and request.GET['at']:
        request.session['at'] = request.GET['at']
    return render(request, 'search/forms.html')


def create_message(request):
    return render(request, 'search/create_message.html')


def forms(request):
=======
    return render (request,'search/test.html',{'alert':alert})

def get_at(request):

    if 'at' in request.GET and request.GET['at']:
        request.session['at'] = request.GET['at']
    return render (request,'search/forms.html')

def create_message(request):

        return render(request, 'search/create_message.html')


def forms(request):

>>>>>>> 161d3843e3aac5b19729ea055c06c9f531a755a7
    return render(request, 'search/forms.html')


def get_name(request):
<<<<<<< HEAD
    at = request.session.get('at', '')
    session = vk.Session(access_token=at)
    api = vk.API(session)
=======

    at = request.session.get('at', '')
    session = vk.Session(access_token= at)
    api=vk.API(session)
>>>>>>> 161d3843e3aac5b19729ea055c06c9f531a755a7

    city = request.GET['city']
    school = request.GET['school']
    school_year = request.GET['school_year']
<<<<<<< HEAD
    request.session['groups_s'] = request.GET['groups']
=======
    request.session['groups_s'] =request.GET['groups']
>>>>>>> 161d3843e3aac5b19729ea055c06c9f531a755a7

    UA_CID = api.database.getCountries(code='UA')[0]['cid']
    CITY = api.database.getCities(country_id=UA_CID, q=city)
    nc = 0
    CITY_ID = CITY[nc]['cid']
<<<<<<< HEAD
    SCHOOL = api.database.getSchools(q=school, city_id=CITY_ID)
    SCHOOL_ID = SCHOOL[1]['id']
    ids_s = []

    users_s = api.users.search(count=1000, country=UA_CID, age_from=0, age_to=99, school_year=school_year,
                               school=SCHOOL_ID, fields="photo_100,last_seen,photo_id,has_mobile,universities")
    del users_s[0]
    for u in users_s:
        ids_s.append(str(u['uid']))
    print(ids_s)
=======
    SCHOOL =  api.database.getSchools(q=school,city_id=CITY_ID)
    SCHOOL_ID = SCHOOL[1]['id']
    ids_s = []

    users_s = api.users.search(count=1000,country=UA_CID, age_from=0, age_to=99, school_year=school_year, school = SCHOOL_ID, fields = "photo_100,last_seen,photo_id,has_mobile,universities")
    del users_s[0]
    for u in users_s:
        ids_s.append(str(u['uid']))
    print (ids_s)
>>>>>>> 161d3843e3aac5b19729ea055c06c9f531a755a7

    groups_s = request.session.get('groups_s', '')
    test = groups_s.split("\n")
    res = []
<<<<<<< HEAD
    # c = api.execute(code='return API.users.get({"user_ids": API.audio.search({"q":"Beatles",
    # "count":3}).items@.owner_id})@.last_name') print (c) of = 0 while of<300000:
    for x in test:
        groupsUsers = api.groups.getMembers(group_id=x, fields="photo_100")
        # of+=1000
        group_1 = groupsUsers['users']
        gu1 = [u['uid'] for u in group_1]
        res.extend(gu1)
        # time.sleep(0.33)

    resul = Counter(res)
    result = dict(resul)
    print(result)
    ids = []
    for key, value in result.items():
        if value > 1:
            ids.append(str(key))
    result_ids = list(set(ids) & set(ids_s))
    print(ids)
    print(result_ids)

    users = api.users.get(user_ids=result_ids,
                          fields="photo_100,last_seen,photo_id,has_mobile,universities,last_seen,photo_id,has_mobile,"
                                 "universities,can_write_private_message,can_send_friend_request")
    return render(request, 'search/done.html', {'users': users})
=======
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
>>>>>>> 161d3843e3aac5b19729ea055c06c9f531a755a7


def intersection(request):
    at = request.session.get('at', '')
<<<<<<< HEAD
    session = vk.Session(access_token=at)
    api = vk.API(session)
    groups_s = request.session.get('groups_s', '')
    test = groups_s.split(',')
    groups_users = api.groups.getMembers(group_id=test[0],
                                        fields="photo_100,last_seen,photo_id,has_mobile,universities,last_seen,"
                                               "photo_id,has_mobile,universities,can_write_private_message,"
                                               "can_send_friend_request")
    groups_users2 = api.groups.getMembers(group_id=test[1],
                                         fields="photo_100,last_seen,photo_id,has_mobile,universities,last_seen,"
                                                "photo_id,has_mobile,universities,can_write_private_message,"
                                                "can_send_friend_request")
    group_1 = groups_users['users']
    group_2 = groups_users2['users']
    gu1 = [u['uid'] for u in group_1]
    gu2 = [u['uid'] for u in group_2]
    result = list(set(gu1) & set(gu2))
    users = api.users.get(user_ids=result,
                          fields="photo_100,last_seen,photo_id,has_mobile,universities,last_seen,photo_id,has_mobile,"
                                 "universities,can_write_private_message,can_send_friend_request")
    print(test[0])
    return render(request, 'search/done.html', {'users': users})


def message(request):
    at = request.session.get('at', '')
    session = vk.Session(access_token=at)
    api = vk.API(session)
    us_id = request.GET.get('id')
    users = api.users.get(user_ids=us_id,
                          fields='last_seen,photo_id,has_mobile,universities,can_write_private_message,'
                                 'can_send_friend_request')[
        0]
    print(us_id)
    return render(request, 'search/test.html', {'users': users})

=======
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
>>>>>>> 161d3843e3aac5b19729ea055c06c9f531a755a7

def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    return render(request, 'search/post_list.html', {'posts': posts})

<<<<<<< HEAD

=======
>>>>>>> 161d3843e3aac5b19729ea055c06c9f531a755a7
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'search/post_detail.html', {'post': post})

<<<<<<< HEAD

=======
>>>>>>> 161d3843e3aac5b19729ea055c06c9f531a755a7
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'search/post_edit.html', {'form': form})

<<<<<<< HEAD

=======
>>>>>>> 161d3843e3aac5b19729ea055c06c9f531a755a7
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'search/post_edit.html', {'form': form})

<<<<<<< HEAD

def get_message(request):
    message_id = request.GET.get('Mid')
    print(message_id)
    return render(request, 'search/forms.html')


def visualisation(request):
        import vis0
        import vis1
        import vis2
        result = json.load(open('miserables.json', 'r'))
        print(result)
        return render(request, 'search/index.html', {'result': result})
=======
def get_message(request):
    message_id = request.GET.get('Mid')
    print (message_id)
    return render(request, 'search/forms.html')
>>>>>>> 161d3843e3aac5b19729ea055c06c9f531a755a7
