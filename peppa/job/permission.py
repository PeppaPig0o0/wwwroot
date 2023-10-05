from rest_framework.permissions import BasePermission
# class IsTeacher(BasePermission):
#     def has_permission(self, request, view):


class IsTeacher(BasePermission):
    def has_permission(self, request, view):
        print(request.user.user_type)
        if request.user.user_type == 'A':
            print('老师')
            return True
        else:
            return False


                    # 检查当前用户是否为教师
    # return request.user.is_authenticated and request.user.is_teacher


class IsStudent(BasePermission):
    def has_permission(self, request, view):
        if request.user.user_type == 'B':
            return True
        else:
            return False
                    # 检查当前用户是否为学生
    # return request.user.is_authenticated and request.user.is_student