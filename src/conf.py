# Flask settings
SERVER_NAME = 'localhost:8888'
FLASK_DEBUG = True

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
ERROR_404_HELP = False
PROPAGATE_EXCEPTIONS = False

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:password@localhost:15432/wishlist-db'
SQLALCHEMY_TRACK_MODIFICATIONS = False