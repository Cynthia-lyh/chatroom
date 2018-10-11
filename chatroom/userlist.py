from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.utils import timezone
 

def get_all_logged_in_users():
    # 获取没有过期的session
	print("iscalled")
	sessions = Session.objects.filter(expire_date__gte=timezone.now())
	uid_list = []
    # 获取session中的userid
	for session in sessions:
		data = session.get_decoded()
		uid_list.append(data.get('_auth_user_id', None))

    # 根据userid查询user
	users_info = User.objects.filter(id__in=uid_list)
	#print(users_info)
	users = []
	for _user in users_info:
		print(_user)
		users.append(str(_user))
	return users
	#request.session.set_expiry(0);



