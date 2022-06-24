from flask import Flask

def create_app():
  app = Flask(__name__)
  try:
    from views.index import index_bp
    from views.result import result_bp
    from views.dashboard import dash_bp
  except:
    from app.views.index import index_bp
    from app.views.result import result_bp
    from app.views.dashboard import dash_bp
    
  app.register_blueprint(index_bp)
  app.register_blueprint(result_bp)
  app.register_blueprint(dash_bp)
  return app

app = create_app()
app.run(debug=True)