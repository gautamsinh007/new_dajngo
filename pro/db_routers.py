# pro/db_routers.py

class App1Router:
    """
    A router to control all database operations on models in the
    'app1' application.
    """

    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'app1':
            return 'app1_db'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'app1':
            return 'app1_db'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        if (
            obj1._meta.app_label == 'app1' and
            obj2._meta.app_label == 'app1'
        ):
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'app1':
            return db == 'app1_db'
        return None
    
    