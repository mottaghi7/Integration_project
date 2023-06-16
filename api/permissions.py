from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsSuperUserOrReadOnly(BasePermission):
    """
        پرمیژنی برای دسترسی دادن به کاربران سوپریوزر یا تنها دیده شدن اینستنس ها
    """
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return bool(request.user and request.user.is_authenticated)
        return bool(request.user and request.user.is_superuser)


class IsUserPlanOrSuperUser(BasePermission):
    """
        پرمیژنی برای دسترسی دادن به دیدن پلن غذایی کاربران که فقط خود کاربر یا سوپریوزر به ان دسترسی داشته باشد
    """
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user.is_authenticated and request.user.is_superuser or
            request.user.is_authenticated and obj.custom_user == request.user
        )


class IsUserManageOrSuperUser(BasePermission):
    """
        پرمیژنی برای دسترسی دادن به دیدن اطلاعات کاربران که فقط خود کاربر یا سوپریوزر به ان دسترسی داشته باشد
    """
    def has_object_permission(self, request, view, obj):
        return bool(
            request.user.is_authenticated and request.user.is_superuser or
            request.user.is_authenticated and obj.email == request.user.email
        )