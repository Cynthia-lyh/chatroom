from django.contrib.auth.models import User 

user = User.objects.create_user(username='admin',password='123456')

