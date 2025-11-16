from importlib.resources import contents

from Demos.win32cred_demo import username
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import  reverse

# Create your views here.


posts=[{"id":1,"title":"lets study javascript","content":"dfhadsfdasfjkdsalfkjdaslkfjasdlfkjdf"},
       {"id":2,"title":"lets study python","content":"fhakdjfhadskjfhkajdshfkajsdhfjadskhf"},
       {"id":3,"title":"lets study json","content":"fhakdjfhadskjfhkajdshfkajsdhfjadskhf"}]
def home(request):
    # reverse('home',args=['simar'])
    html=""
    for post in posts:
        html+=f'''
        <div> 
            <a href="/post/{post['id']}/">
            <h1>{post['id']}-{post['title']}</h1>
        <p style="color:red"> {post['content']}</p>
        </div>'''

    return render(request,'posts/home.html',{'posts':posts} )
def post(request,id):
    valid_id=False
    html = ""
    for post in posts:

        if post['id']==id:
            post_dict=post
            valid_id=True
            break
    if valid_id:

        html=f'''
        <div>
        <h1>{post_dict['title']}</h1>
        <p>{post_dict['content']}</p>
        </div>
        '''

    # print(type(id))
        return render(request,"post/post.html")
    else:
        return HttpResponseNotFound("not available we are working on it")
def google(request,id):
    url=reverse('post',args=[id])

    return HttpResponseRedirect(url)

