from flask_migrate import MigrateCommand
from flask_script import Manager, Shell

from app import app, db

manager = Manager(app)


def make_shell_context():
    return dict(app=app, db=db)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
