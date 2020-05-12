from django.contrib.auth.models import User

class EmailAuth:
    """Authenticate a user by an exact match on the email an password"""

    def authenticate(self, username=None, password=None):
        """"Get an instance of user based off the email ad verify the psw"""

        try:
            user = User.objects.get(email=username)

            if user.check_password(password):
                return user
            return None 
        except User.DoesNotExist:
            return None

    def get_user(self, user_id):
        """Used by the Django authentication system to retreive a user instance"""

        try:
            user = User.objects.get(pk=user_id)

            if user.is_active:
                return user
            return None
        except User.DoesNotExist:
            return None
