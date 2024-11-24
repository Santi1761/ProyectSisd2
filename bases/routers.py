class DatabaseRouter:
    """
    Enrutador para manejar la asignación de operaciones de base de datos a PostgreSQL o MongoDB.
    """

    def db_for_read(self, model, **hints):
        """
        Rutea las lecturas de modelos a la base de datos correspondiente.
        """
        if model._meta.app_label == 'app_que_usa_postgresql':
            return 'default'  # PostgreSQL
        elif model._meta.app_label == 'app_que_usa_mongodb':
            return 'mongodb'  # MongoDB
        return None

    def db_for_write(self, model, **hints):
        """
        Rutea las escrituras de modelos a la base de datos correspondiente.
        """
        if model._meta.app_label == 'app_que_usa_postgresql':
            return 'default'  # PostgreSQL
        elif model._meta.app_label == 'app_que_usa_mongodb':
            return 'mongodb'  # MongoDB
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Determina si una migración debe ser permitida en una base de datos específica.
        """
        if db == 'mongodb':
            return False  # MongoDB no usa migraciones de Django
        return True  # Permite migraciones en PostgreSQL
