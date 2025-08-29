from todo_app.entity.user_entity import UserEntity


class UserDao:

    def create_user(
            self,
            firstname,
            lastname,
            username,
            password,
            email
    ):
        return UserEntity.objects.create(
            firstname=firstname,
            lastname=lastname,
            username=username,
            password=password,
            email=email,
        )

    def get_user_by_username(self, username):
        return UserEntity.objects.get(username=username)