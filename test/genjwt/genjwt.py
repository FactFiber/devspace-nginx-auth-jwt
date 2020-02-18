'''
Create key
'''
import os
import sys
import datetime
import jwt

def create_key(expires_hours = None, **kw):
    payload = kw.copy()
    payload['iat'] = datetime.datetime.utcnow()
    expires = get_expires(expires_hours)
    payload['exp'] = expires
    key = os.environ["JWT_KEY"]
    return jwt.encode(payload, key, algorithm='ES512').decode('utf-8')

def get_expires(hours = None):
    if hours is None:
        hours = float(os.environ.get("JWT_EXP_HOURS"))
    now = datetime.datetime.utcnow()
    return now + datetime.timedelta(hours = hours)

if __name__ == '__main__':
    user_id = sys.argv[1]
    permissions = [
        s.split("=") for s in sys.argv[2:]]
    options = {}
    for key, val in permissions:
      options.setdefault(key, []).append(val)

    expires_hours = None
    if 'expires' in permissions:
        expires_hours = float(permissions.pop('expires'))
    jwt = create_key(
        expires_hours = expires_hours, **options)
    print(jwt)
