class DatabaseError(Exception):
    def __init__(self, error):
        self.error = error
        super.__init__("A DatabaseError occurred!")
        self.handle_error()

    def handle_error(self):
        if isinstance(self.error, ValueError):
            raise ValueError(f"A value error occurred {self.error}")
        raise self.error