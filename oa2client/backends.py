from social_core.backends.oauth import BaseOAuth2

class ForAllBackpackOAuth2(BaseOAuth2):
    """
    ForAllBackpack OAuth2 authentication backend
    
    Define in settings:
    
    SOCIAL_AUTH_FORALLBACKPACK_KEY = '...'
    SOCIAL_AUTH_FORALLBACKPACK_SECRET = '...'
    """
    # scheme://login/forallbackpack/
    name = 'forallbackpack'
    
    AUTHORIZATION_URL = 'http://127.0.0.1:8000/o/authorize/'
    ACCESS_TOKEN_URL = 'http://127.0.0.1:8000/o/token/'
    ACCESS_TOKEN_METHOD = 'POST'

    REVOKE_TOKEN_URL = 'http://127.0.0.1:8000/o/revoke_token/'
    REVOKE_TOKEN_METHOD = 'POST'
    
    ID_KEY = 'id'

    SCOPE_SEPARATOR = ','
#   EXTRA_DATA = [
#       ('client_id', 'client_id'),
#       ('expires', 'expires')
#   ]

    def get_user_details(self, response):
        """Return user details from `response`"""
        return {
            'username': response.get('username', ''),
            'email': response.get('email', ''),
            'fullname': response.get('fullname', ''),
            'first_name': response.get('first_name', ''),
            'last_name': response.get('last_name', '')
        }

    def user_data(self, access_token, *args, **kwargs):
        """Load user data from authorization server"""
        response = kwargs.get('response')
        return self.get_json('http://127.0.0.1:8000/api/user/test/', headers={
            'Authorization': '{0} {1}'.format(response.get('token_type'),
                                              access_token)
        })
        
    def revoke_token_params(self, token, uid):
        """Compose params POST-ed to `REVOKE_TOKEN_URL`"""
        client_id, client_secret = self.get_key_and_secret()
        
        return {
            'client_id': client_id,
            'client_secret': client_secret,
            'token': token
        }

