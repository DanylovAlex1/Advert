from django.core.exceptions import PermissionDenied

class UserIsOwnerOrAdminMixin():
    """
    выполняем проверку. будет возвращено True в случае, если USER_ID объекта
    совпадает с пользователем, залогинившимся в систему. Это означает, что это владелец.
    Либо это Администратор user.is_staff
    """
    def has_permission(self):
        return self.get_object().user == self.request.user \
               or self.request.user.is_staff

    def dispatch(self, request, *args, **kwargs):
        if not self.has_permission():
            raise PermissionDenied # выбрасываем 403 ошибку.
        return super().dispatch(request, *args, **kwargs)

