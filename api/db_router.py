# api/db_router.py

class DbRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'api':
            return 'supabase'
        return None

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'api':
            return 'supabase'
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'api':
            return db == 'supabase'
        return None
