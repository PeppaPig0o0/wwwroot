from rest_framework.permissions import BasePermission
from rest_framework.exceptions import PermissionDenied
# class IsTeacher(BasePermission):
#     def has_permission(self, request, view):


class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        print(request.user.level)
        if request.user.level == 'A':
            print('老师')
            return True
        else:
            print('不是老师')
            raise PermissionDenied('您没有执行该操作的权限。')


                    # 检查当前用户是否为教师
    # return request.user.is_authenticated and request.user.is_teacher


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        print('学生')
        if request.user.level == 'B':
            print('学生')
            return True
        else:
            print('学生不')
            raise PermissionDenied('您没有执行该操作的权限。')

            # 检查当前用户是否为学生
