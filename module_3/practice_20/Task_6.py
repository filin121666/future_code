class Permission:
    def get_permission(self, user):
        self.user = user


class Staff_permission(Permission):
    pass


class Simple_permission(Permission):
    pass


class Admin_permission(Permission):
    pass
