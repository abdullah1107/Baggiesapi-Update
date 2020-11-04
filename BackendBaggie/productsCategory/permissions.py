# from rest_framework import permissions
#
# class IsOwner(permissions.BasePermission):
#
#     def has_object_permission(self, request, view, obj):
#         print("hello")
#         if request.method == 'GET':
#             return True
#         return obj.owner == request.user

# class IsAuthorOrReadOnly(permissions.BasePermission):
#     # Read-only permissions are allowed for any request
#     def has_object_permission(self, request, view, obj):
#         if request.method == "POST":
#             return False
#         else:
#             return True
# class IsProductCateOrIsAuthenticated(permissions.BasePermission):
#
#     def has_permission(self, request, view):
#         # allow all POST requests
#         if request.method == 'GET':
#             return True
#
#         # Otherwise, only allow authenticated requests
#         # Post Django 1.10, 'is_authenticated' is a read-only attribute
#         return request.user and request.user.is_authenticated
