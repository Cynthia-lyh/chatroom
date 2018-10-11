from django import template
from chatroom import userlist

register = template.Library()

	#@register.inclusion_tag('templatetags/logged_in_user_list.html')
@register.inclusion_tag('logged_in_user_list.html')
def render_logged_in_user_list():
	return { 'users': userlist.get_all_logged_in_users()}