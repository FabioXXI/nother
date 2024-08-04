from controller.errors.http.http_exceptions import bad_request
from typing import NamedTuple

class Variable(NamedTuple):
    type: str
    value: str

class VariableEnvironment:
    def __init__(self, variable: Variable):
        self.variable = variable

    def verify_type_compatible(self, type: str) -> bool:
        return self.get_type() == type

    def get_type(self) -> str:
        return self.variable.type

    def get_value(self) -> str:
        return self.variable.value

    def put_value(self, value: str) -> None:
        self.variable.value = value

    def put_type(self, type: str) -> None:
        self.variable.type = type

    def get_copy_of_variable(self) -> Variable:
        return Variable(type=self.get_type(), value=self.get_value())

    def put_variable(self, variable: dict) -> None:
        self.variable = Variable(type=variable['type'], value=variable['value'])

    def get_variable(self) -> Variable:
        return self.variable

    def create_variable_from_dict(self, variable: dict) -> Variable:
        return Variable(type=variable['type'], value=variable['value'])

    def __add__(self, other):
        if not(self.verify_type_compatible(other.get_type())):
            raise bad_request(f"{self.get_variable()!r} is not compatible with {other.get_variable()!r}")
        if self.get_type() == "float" and other.get_type() == "float":
            return VariableEnvironment(self.create_variable_from_dict({
                "type": "float",
                "value": str(float(self.get_value()) + float(other.get_value()))
            }))
        return VariableEnvironment(self.create_variable_from_dict({
            "type": "str",
            "value": self.get_value() + other.get_value()
        }))

    def __sub__(self, other):
        if not(self.verify_type_compatible(other.get_type())):
            raise bad_request(f"{self.get_variable()!r} is not compatible with {other.get_variable()!r}")
        if self.get_type() == "float" and other.get_type() == "float":
            return VariableEnvironment(self.create_variable_from_dict({
                "type": "float",
                "value": str(float(self.get_value()) - float(other.get_value()))
            }))
        raise bad_request(f"{self.get_variable()!r} cannot complete operation with {other.get_variable()!r}")

    def __mul__(self, other):
        if self.get_type() == "float" and other.get_type() == "float":
            return VariableEnvironment(self.create_variable_from_dict({
                "type": "float",
                "value": str(float(self.get_value()) * float(self.get_value()))
            }))
        if self.get_type() == "str" and other.get_type() == "float":
            return VariableEnvironment(self.create_variable_from_dict({
                "type": "str",
                "value": self.get_value() * int(self.get_value())
            }))
        raise bad_request(f"{self.get_variable()!r} cannot complete operation with {other.get_variable()!r}")

    def __truediv__(self, other):
        if not(self.verify_type_compatible(other.get_type())):
            raise bad_request(f"{self.get_variable()} is not compatible with {other.get_variable()!r}")
        if self.get_type() == "float" and other.get_type() == "float":
            return VariableEnvironment(self.create_variable_from_dict({
                "type": "float",
                "value": str(float(self.get_value()) / float(other.get_value()))
            }))
        raise bad_request(f"{self.get_variable()!r} cannot complete operation with {other.get_variable()!r}")

    def __floordiv__(self, other):
        if not(self.verify_type_compatible(other.get_type())):
            raise bad_request(f"{self.get_variable()!r} is not compatible with {other.get_variable()!r}")
        if self.get_type() == "float" and other.get_type() == "float":
            return VariableEnvironment(self.create_variable_from_dict({
                "type": "float",
                "value": str(float(self.get_value()) // float(other.get_value()))
            }))
        raise bad_request(f"{self.get_variable()!r} cannot complete operation with {other.get_variable()!r}")

    def __mod__(self, other):
        if not(self.verify_type_compatible(other.get_type)):
            raise bad_request(f"{self.get_variable()!r} is not compatible with {other.get_variable()!r}")
        if self.get_type() == "float" and other.get_type() == "float":
            return VariableEnvironment(self.create_variable_from_dict({
                "type": "float",
                "value": str(float(self.get_value()) % float(other.get_value()))
            }))
        raise bad_request(f"{self.get_variable()!r} cannot complete operation with {other.get_variable()!r}")

    def __pow__(self, other):
        if not(self.verify_type_compatible(other.get_type())):
            raise bad_request(f"{self.get_variable()!r} is not compatible with {other.get_variable()!r}")
        if self.get_type() == "float" and other.get_type() == "float":
            return VariableEnvironment(self.create_variable_from_dict({
                "type": "float",
                "value": str(float(self.get_value()) ** int(other.get_value()))
            }))
        raise bad_request(f"{self.get_variable()!r} cannot complete operation with {other.get_variable()!r}")

    def create_variable(self, value: str):
        variable = VariableEnvironment(self.create_variable_from_dict(
            {
                "type": self.get_value_type(value),
                "value": value,
            })
        )
        return variable

    def __eq__(self, other) -> bool:
        if not(self.verify_type_compatible(other.get_type())):
            raise bad_request(f"{self.get_variable()!r} is not compatible with {other.get_variable()!r}")
        if self.get_type() == "float" and other.get_type() == "float":
            return float(self.get_value()) == float(other.get_value())
        return self.get_value() == other.get_value()

    def __gt__(self, other):
        if not(self.verify_type_compatible(other.get_type())):
            raise bad_request(f"{self.get_variable()!r} is not compatible with {other.get_variable()!r}")
        if self.get_type() == "float" and other.get_type() == "float":
            return float(self.get_value()) > float(other.get_value())
        raise bad_request(f"{self.get_variable()!r} cannot complete operation with {other.get_variable()!r}")

    def __ge__(self, other):
        if not(self.verify_type_compatible(other.get_type())):
            raise bad_request(f"{self.get_variable()!r} is not compatible with {other.get_variable()!r}")
        if self.get_type() == "float" and other.get_type() == "float":
            return float(self.get_value()) >= float(other.get_value())
        raise bad_request(f"{self.get_variable()!r} cannot complete operation with {other.get_variable()!r}")

    def __lt__(self, other):
        if not(self.verify_type_compatible(other.get_type())):
            raise bad_request(f"{self.get_variable()!r} is not compatible with {other.get_variable()!r}")
        if self.get_type() == "float" and other.get_type() == "float":
            return float(self.get_value()) < float(other.get_value())
        raise bad_request(f"{self.get_variable()!r} cannot complete operation with {other.get_variable()!r}")

    def __le__(self, other):
        if not(self.verify_type_compatible(other.get_type())):
            raise bad_request(f"{self.get_variable()!r} is not compatible with {other.get_variable()!r}")
        if self.get_type() == "float" and other.get_type() == "float":
            return float(self.get_value()) <= float(other.get_value())
        raise bad_request(f"{self.get_variable()!r} cannot complete operation with {other.get_variable()!r}")

    def __ne__(self, other):
        if not(self.verify_type_compatible(other.get_type())):
            raise bad_request(f"{self.get_variable()!r} is not compatible with {other.get_variable()!r}")
        if self.get_type() == "float" and other.get_type() == "float":
            return float(self.get_value()) != float(other.get_value())
        return self.get_value() != other.get_value()

    def __float__(self):
        try:
            float(self.get_value())
            return VariableEnvironment(self.create_variable_from_dict({
                "type": "float",
                "value": self.get_value(),
            }))
        except:
            raise bad_request(f"{self.get_variable()!r} cannot be converted to float")

    def __str__(self):
        return VariableEnvironment(self.create_variable_from_dict({
            "type": "str",
            "value": self.get_value(),
        }))

    def get_value_type(self, value: str) -> str:
        try:
            float(value)
            return "float"
        except:
            return "str"

    def __radd__(self, other: str):
        other = self.create_variable(other)
        return other + self

    def __rsub__(self, other: str):
        other = self.create_variable(other)
        return other - self

    def __rmul__(self, other: str):
        other = self.create_variable(other)
        return other * self

    def __rtruediv__(self, other: str):
        other = self.create_variable(other)
        return other / self

    def __rfloordiv__(self, other: str):
        other = self.create_variable(other)
        return other // self

    def __rmod__(self, other: str):
        other = self.create_variable(other)
        return other % self

    def __rpow__(self, other: str):
        other = self.create_variable(other)
        return other ** self

    def __len__(self):
        if self.get_type() == "float":
            raise bad_request(f"float object doens't has size")
        return VariableEnvironment(self.create_variable_from_dict(
            {
                "type": "float",
                "value": len(self.get_value())
            }
        ))

    def __repr__(self):
        return f"VariableEnvironment({self.get_variable()!r})"