from django.contrib.auth import get_user_model, backends

from web3auth.utils import recover_to_addr
from web3auth.settings import app_settings

class Web3Backend(backends.ModelBackend):
    def authenticate(self, request, address=None, token=None):
        # get user model
        User = get_user_model()
        # check if the address the user has provided matches the signature

        address_field = app_settings.WEB3AUTH_USER_ADDRESS_FIELD
        address = address[1]
        kwargs = {
            address_field+"__iexact": address     }
                # try to get user with provided data
        user = User.objects.filter(**kwargs).first()
        print("ano")

        return user
