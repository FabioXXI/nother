from controller.errors.http.http_exceptions import bad_request

class VariableValidator:
    def __init__(self, variable: dict):
        self.variable = variable
        self.check_type_and_value()
        self.check_name()

    def check_type_and_value(self):
        if self.variable['type'] != "float" and self.variable['type'] != "str":
            raise bad_request(f"Invalid type: Must be float or str")
        if self.variable['type'] == "float":
            try:
                float(self.variable['value'])
            except Exception as error:
                raise bad_request(f"Invalid type: {error!r}")

    def check_name(self):
        if " " in self.variable['name']:
            raise bad_request(f"Invalid name")