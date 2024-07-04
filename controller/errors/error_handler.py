from controller.errors.database_error import DatabaseError

def error_handler(error):
    if isinstance(error, DatabaseError):
        DatabaseError(error)
    raise error