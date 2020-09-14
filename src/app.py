import logging.config

import os
import conf
from flask import Flask, Blueprint
from api.restplus import api
from database import db
from api.controllers.customers import ns as customers_namespace

app = Flask(__name__)
app.config.from_object(conf)
logging_conf_path = os.path.normpath(os.path.join(os.path.dirname(__file__), '../logging.conf'))
logging.config.fileConfig(logging_conf_path)
log = logging.getLogger(__name__)

def initialize_app(flask_app):
    blueprint = Blueprint('api', __name__, url_prefix='/api')
    api.init_app(blueprint)
    api.add_namespace(customers_namespace)
    flask_app.register_blueprint(blueprint)

    db.init_app(flask_app)

def main():
    initialize_app(app)
    log.info('>>>>> Starting development server at http://{}/api/ <<<<<'.format(app.config['SERVER_NAME']))
    app.run(debug=conf.FLASK_DEBUG)

if __name__ == "__main__":
    main()
