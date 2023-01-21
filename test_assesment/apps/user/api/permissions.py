from rest_framework.permissions import BasePermission


class AdminOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_admin


class StaffOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_staff_user

class GeneralUserOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_general


class SuperAdminOnly(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_superuser


