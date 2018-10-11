from django.shortcuts import render,redirect,reverse
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect,HttpResponse,JsonResponse
from django.contrib import auth
from django.template import RequestContext, loader
from django.contrib.auth.decorators import login_required

# Create your views here.
def login(request):
	return render(request,'chatroom_login.html')

def register(request):
    return render(request,'chatroom_register.html')

@login_required
def user(request):
    return render(request,
                  'chatroom.html',
                  {'username': request.POST.get('username', '')})

def registersuc(request):
    return render(request,'chatroom_registersuc.html')

def websocket(request):
    return render(request,'websocket.html')


def chatroom(request):
    return render(request,'chatroom.html')

def online_people(request):
    return render(request,'online_people.html')

def userRegister(request):
	#if request.user.is_authenticated():
        #return HttpResponseRedirect("/user")
    try:
    	if request.method=='POST':
            username=request.POST.get('name','')
            password1=request.POST.get('password1','')
            password2=request.POST.get('password2','')
            errors=[]
            #print (username)
            '''registerForm=RegisterForm({'username':username,'password1':password1,'password2':password2})#b********
            if not registerForm.is_valid():
                errors.extend(registerForm.errors.values())
                print (password1)
                print (errors)
                return render(request,"chatroom_register.html",{'username':username,'errors':errors})
                '''
            if password1!=password2:
                #print (password2)
                errors.append("两次输入的密码不一致!")
                return JsonResponse({'username':username,'errors':errors, 'rtn':1})
            #print (password1)
            filterResult=User.objects.filter(username=username)#c************
            if len(filterResult)>0:
                errors.append("用户名已存在")
                return JsonResponse({'username':username,'errors':errors,'rtn':1})
    		
            '''user=User()
            user.username=username
            user.set_password(password1)
            user.save()'''
            
            user = User.objects.create_user(username=username,password=password1)
            newUser=auth.authenticate(username=username,password=password1)#f***************
            print (password1)
            if newUser is not None:
                print (password1)
                print (newUser)
                errors.append( "test" ) 
                #return redirect("login")
                '''t1 = loader.get_template('chatroom_registersuc.html')
                context = RequestContext(request, {'username':username,'errors':errors},encode('utf8'))
                return HttpResponse(t1.render(context))'''
                return JsonResponse({'username':username,'errors':errors,'rtn':0})

                #return HttpResponse(request,"chatroom_registersuc.html",{'username':username,'errors':errors},encode('utf8'))
                #auth.login(request, newUser)#g*******************
                #return HttpResponseRedirect("/user")

    except Exception as e:
        errors.append("注册失败：%s"%str(e))
        print(errors)
        return JsonResponse({'username':username,'errors':errors})

def do_login(request):
    if request.method == 'GET':
        return render(request, 'chatroom_login.html')
 
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    print(request.POST)
    print(request.GET)
    print(request)
    #return user(request)
 
    _user = auth.authenticate(request, username=username, password=password)
    if _user is not None:
        #login(request, user)
        #print (password)
        auth.login(request, _user)
        return user(request)
    else:
        return render(request, 'chatroom_login.html', {
            'username': username,
            'password': password,
        })
    
'''def userlist(request):

    _user = userlist.get_all_logged_in_users()
    if _user is not None:
        #login(request, user)
        print (_user)
        return JsonResponse({'username':_user})'''
    