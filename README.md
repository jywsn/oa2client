Start FAB (Authorization Server) on http://127.0.0.1:8000/

Create an `Application` instance, making a note of the client ID and secret.
```
Redirect URI = http://0.0.0.0:5000/complete/forallbackpack/
Client type = Confidential
Authorization grant type Authorization code
Skip authorization = CHECKED
```

Create `oa2client` database and run migrations.

Copy the client ID and secret to the project's setttings file:
```
FAB_SERVER_URL = 'http://127.0.0.1:8000'
FAB_CLIENT_ID  = '...'
FAB_CLIENT_SECRET = '...'
```

Start oa2client on http://0.0.0.0:5000.




