from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from database.models import *
from database import db
from app import app

db.init_app(app)
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()