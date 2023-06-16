# from Blog.models import Post
# from django import template
# from django.db.models import Count
# from django.utils.safestring import mark_safe
# import markdown
# from activity_log import models as activity_log_model
#
# register = template.Library()
#
#
# @register.simple_tag()
# def user_unread_post(request):
#     user_activities = activity_log_model.ActivityLog.objects.filter(user_id=request.user.id).filter(request_method='GET')
#     user_unread_post_list = []
#     for post in Post.objects.all():
#         for user_activity in user_activities:
#             if post.get_absolute_url != user_activity.request_url:
#                 user_unread_post_list.append(post)
#
#     return user_unread_post_list
