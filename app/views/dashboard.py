from flask import Blueprint, render_template
try: 
  import key
except:
 from app import key
dash_bp = Blueprint("dash_bp", __name__)

# You'll need to install PyJWT via pip 'pip install PyJWT' or your project packages file

import jwt
import time
METABASE_SITE_URL = key.METABASE_SITE_URL
METABASE_SECRET_KEY = key.METABASE_SECRET_KEY


payload = {
  "resource": {"dashboard": 2},
  "params": {
    
  },
  "exp": round(time.time()) + (60 * 10) # 10 minute expiration
}
token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")

iframeUrl = METABASE_SITE_URL + "/embed/dashboard/" + token + "#bordered=true&titled=true"

@dash_bp.route('/dashboard')
def dashboard():
  return render_template('dashboard.html', iframeUrl = iframeUrl)