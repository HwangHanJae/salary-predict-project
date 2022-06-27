from dotenv import load_dotenv
import os
import jwt
import time
from flask import Blueprint, render_template
dash_bp = Blueprint("dash_bp", __name__)

# # You'll need to install PyJWT via pip 'pip install PyJWT' or your project packages file

# load_dotenv()
# METABASE_SITE_URL = "http://predsalaryappmetabase.herokuapp.com"
# METABASE_SECRET_KEY = os.getenv('METABASE_SECRET_KEY')

# payload = {
#   "resource": {"dashboard": 2},
#   "params": {
    
#   },
#   "exp": round(time.time()) + (60 * 10) # 10 minute expiration
# }
# token = jwt.encode(payload, METABASE_SECRET_KEY, algorithm="HS256")

# iframeUrl = METABASE_SITE_URL + "/embed/dashboard/" + token + "#bordered=true&titled=true"
iframeUrl = "http://predsalaryappmetabase.herokuapp.com/public/dashboard/5b352f35-5ea9-47f8-a9f4-6bc146e718ff"
@dash_bp.route('/dashboard')
def dashboard():
  return render_template('dashboard.html', iframeUrl = iframeUrl)