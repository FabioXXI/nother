class VariableObj:
    def __init__(self, variable: dict) -> None:
        self.variable = variable
        if not(self.check_type_and_value(self.variable['type'], self.variable['value'])):
            raise f"{self.get_type()} is not compatible with {self.get_value()}"

    def __repr__(self) -> str:
        return f"{self.get_copy_of_variable()!r}"

    def get_type(self) -> str:
        return self.variable['type']
    
    def get_value(self) -> str:
        return self.variable['value']

    def check_type_and_value(self, type: str, value: str) -> bool:
        match type:
            case "string":
                return True
            case "float":
                try:
                    float(value)
                    return True
                except:
                    return False
                
    def put_type(self, type: str) -> None:
        self.variable['type'] = type

    def put_value(self, value: str) -> None:
        self.variable['value'] = value
    
    def get_copy_of_variable(self) -> dict:
        return self.variable.copy()

    def check_type_integrity(self, t1: str, t2: str) -> bool:
        return t1 == t2
    
    def get_variable(self) -> dict:
        return self.variable

    def __add__(self, variable_obj):
        if isinstance(variable_obj, VariableObj):
            if self.check_type_integrity(self.get_type(), variable_obj.get_type()):
                temp_variable = self.get_copy_of_variable()
                temp_variable['value'] = self.add(self.get_type(), self.get_value(), variable_obj.get_value())
                return VariableObj(temp_variable)
        else:
            if self.check_type_and_value(self.get_type(), variable_obj):
                temp_variable = self.get_copy_of_variable()
                temp_variable['value'] = self.add(self.get_type(), self.get_value(), variable_obj)
                return VariableObj(temp_variable)
        raise "Operation __add__ failed"
            
    def add(self, return_type: str, v1: str, v2: str) -> str:
        match return_type:
            case "string":
                return v1 + v2
            case "float":
                return str(float(v1) + float(v2))
            
    def __radd__(self, variable_obj):
        if isinstance(variable_obj, VariableObj):
            if self.check_type_integrity(self.get_type(), variable_obj.get_type()):
                temp_variable = self.get_variable()
                temp_variable['value'] = self.add(self.get_type(), self.get_value(), variable_obj.get_value())
                return VariableObj(temp_variable)
        else:
            if self.check_type_and_value(self.get_type(), variable_obj):
                temp_variable = self.get_variable()
                temp_variable['value'] = self.add(self.get_type(), self.get_value(), variable_obj)
                return VariableObj(temp_variable)
        raise "Operation __radd__ failed"
            
    def __iadd__(self, variable_obj):
        if isinstance(variable_obj, VariableObj):
            if self.check_type_integrity(self.get_type(), variable_obj.get_type()):
                self.put_value(self.add(self.get_type(), self.get_value(), variable_obj.get_value()))
                return self
        else:
            if self.check_type_and_value(self.get_type(), variable_obj):
                self.put_value(self.add(self.get_type(), self.get_value(), variable_obj))
                return self
        raise "Operation __iadd__ failed"
    
    def __sub__(self, variable_obj):
        if isinstance(variable_obj, VariableObj):
            if self.check_type_integrity(self.get_type(), variable_obj.get_type()):
                temp_variable = self.get_copy_of_variable()
                temp_variable['value'] = self.sub(self.get_type(), self.get_value(), variable_obj.get_value())
                return temp_variable
        else:
            if self.check_type_and_value(self.get_type(), variable_obj):
                temp_variable = self.get_copy_of_variable()
                temp_variable['value'] = self.sub(self.get_type(), self.get_value(), variable_obj)
                return VariableObj(temp_variable)
        raise "Operation __sub__ failed"
    
    def sub(self, return_type, v1, v2):
        match return_type:
            case "string":
                raise f"Invalid sub operation {return_type}"
            case "float":
                return str(float(v1) - float(v2))
    
    def __rsub__(self, variable_obj):
        if isinstance(variable_obj, VariableObj):
            if self.check_type_integrity(self.get_type(), variable_obj.get_type()):
                temp_variable = self.get_copy_of_variable()
                temp_variable['value'] = self.sub(self.get_type(), self.get_value(), variable_obj.get_value())
                return VariableObj(temp_variable)
        else:
            if self.check_type_and_value(self.get_type(), variable_obj):
                temp_variable = self.get_copy_of_variable()
                temp_variable['value'] = self.sub(self.get_type(), self.get_value(), variable_obj)
                return temp_variable
        raise "Operation __rsub__ failed"
    
    def __isub__(self, variable_obj):
        if isinstance(variable_obj, VariableObj):
            if self.check_type_integrity(self.get_type(), variable_obj.get_type()):
                self.put_value(self.sub(self.get_type(), self.get_value(), variable_obj.get_value()))
                return self
        else:
            if self.check_type_and_value(self.get_type(), variable_obj):
                self.put_value(self.sub(self.get_type(), self.get_value(), variable_obj))
                return self
        raise "Operation __isub__ failed"

    def __mul__(self, variable_obj):
        if isinstance(variable_obj, VariableObj):
            if self.check_type_integrity(self.get_type(), variable_obj.get_type()):
                temp_variable = self.get_copy_of_variable()
                temp_variable['value'] = self.mul(self.get_type(), self.get_value(), variable_obj.get_value())
                return VariableObj(temp_variable)
        else:
            if self.check_type_and_value(self.get_type(), variable_obj):
                temp_variable = self.get_copy_of_variable()
                temp_variable['value'] = self.mul(self.get_type(), self.get_value(), variable_obj)
                return VariableObj(temp_variable)
        raise "Operation __mul__ failed"
    
    def mul(self, return_type: str, v1: str, v2: str) -> str:
        match return_type:
            case "string":
                raise f"Invalid operation mul operation {return_type}"
            case "float":
                return str(float(v1) * float(v2))
            
    def __rmul__(self, variable_obj):
        if isinstance(variable_obj, VariableObj):
            if self.check_type_integrity(self.get_type(), variable_obj.get_type()):
                temp_variable = self.get_copy_of_variable()
                temp_variable['value'] = self.mul(self.get_type(), self.get_value(), variable_obj.get_value())
                return VariableObj(temp_variable)
        else:
            if self.check_type_and_value(self.get_type(), variable_obj):
                temp_variable = self.get_copy_of_variable()
                temp_variable['value'] = self.mul(self.get_type(), self.get_value(), variable_obj)
                return VariableObj(temp_variable)
        raise "Operation __rmul__ failed"
    
    def __imul__(self, variable_obj):
        if isinstance(variable_obj, VariableObj):
            if self.check_type_integrity(self.get_type(), variable_obj.get_type()):
                self.put_value(self.mul(self.get_type(), self.get_value(), variable_obj.get_value()))
                return self
        else:
            if self.check_type_and_value(self.get_type(), variable_obj):
                self.put_type(self.mul(self.get_type(), self.get_value(), variable_obj))
                return self
        raise "Operation __imul__ failed"
    
    def __truediv__(self, variable_obj):
        if isinstance(variable_obj, VariableObj):
            if self.check_type_integrity(self.get_type(), variable_obj.get_type()):
                temp_variable = self.get_copy_of_variable()
                temp_variable['value'] = self.div(self.get_type(), self.get_value(), variable_obj.get_value())
                return VariableObj(temp_variable)
        else:
            if self.check_type_and_value(self.get_type(), variable_obj):
                temp_variable = self.get_copy_of_variable()
                temp_variable['value'] = self.div(self.get_type(), self.get_value(), variable_obj)
                return VariableObj(temp_variable)
        raise "Operation __truediv__ failed"
            
    def div(self, return_type: str, v1: str, v2: str) -> str:
        match return_type:
            case "string":
                raise f"Invalid operation div {return_type}"
            case "float":
                if v2 == "0":
                    raise "Invalid div operatio: Zero division"
                return str(float(v1) / float(v2))
            
    def __rtruediv__(self, variable_obj):
        if isinstance(variable_obj, VariableObj):
            if self.check_type_integrity(self.get_type(), variable_obj.get_type()):
                temp_variable = self.get_copy_of_variable()
                temp_variable['value'] = self.div(self.get_type(), variable_obj.get_value(), self.get_value())
                return VariableObj(temp_variable)
        else:
            if self.check_type_and_value(self.get_type(), variable_obj):
                temp_variable = self.get_copy_of_variable()
                temp_variable['value'] = self.div(self.get_type(), variable_obj, self.get_value())
                return VariableObj(temp_variable)
        raise "Operation __rtruediv__ failed"
    
    def __itruediv__(self, variable_obj):
        if isinstance(variable_obj, VariableObj):
            if self.check_type_integrity(self.get_type(), variable_obj.get_type()):
                self.put_value(self.div(self.get_type(), self.get_value(), variable_obj.get_value()))
                return self
        else:
            if self.check_type_and_value(self.get_type(), variable_obj):
                self.put_value(self.div(self.get_type(), self.get_value(), variable_obj))
                return self
        raise "Operation __itruediv__ failed"

    def __pow__(self, variable_obj):
        if isinstance(variable_obj, VariableObj):
            if self.check_type_integrity(self.get_type(), variable_obj.get_type()):
                temp_variable = self.get_copy_of_variable()
                temp_variable['value'] = self.pow(self.get_type(), self.get_value(), variable_obj.get_value())
                return VariableObj(temp_variable)
        else:
            if self.check_type_and_value(self.get_type(), variable_obj):
                temp_variable = self.get_copy_of_variable()
                temp_variable['value'] = self.pow(self.get_type(), self.get_value(), variable_obj)
                return VariableObj(temp_variable)
        raise "Operation __pow__ failed"
    
    def __rpow__(self, variable_obj):
        if isinstance(variable_obj, VariableObj):
            if self.check_type_integrity(self.get_type(), variable_obj.get_type()):
                temp_variable = self.get_copy_of_variable()
                temp_variable['value'] = self.pow(self.get_type(), variable_obj.get_value(), self.get_value())
                return VariableObj(temp_variable)
        else:
            if self.check_type_and_value(self.get_type(), variable_obj):
                temp_variable = self.get_copy_of_variable()
                temp_variable['value'] = self.pow(self.get_type(), variable_obj, self.get_value())
                return VariableObj(temp_variable)
        raise "Operation __rpow__ failed"
    
    def pow(self, return_type: str, v1: str, v2: str) -> str:
        match return_type:
            case "string":
                raise f"Invalid operation pow {return_type}"
            case "float":
                return str(pow(float(v1), float(v2)))
            
    def __floordiv__(self, variable_obj):
        if isinstance(variable_obj, VariableObj):
            if self.check_type_integrity(self.get_type(), variable_obj.get_type()):
                temp_variable = self.get_copy_of_variable()
                temp_variable['value'] = self.floordiv(self.get_type(), self.get_value(), variable_obj.get_value())
                return VariableObj(temp_variable)
        else:
            if self.check_type_and_value(self.get_type(), variable_obj):
                temp_variable = self.get_copy_of_variable()
                temp_variable['value'] = self.floordiv(self.get_type(), self.get_value(), variable_obj)
                return VariableObj(temp_variable)
        raise "Operation __floordiv__ failed"
    
    def floordiv(self, return_type: str, v1: str, v2: str) -> str:
        match return_type:
            case "string":
                raise f"Invalid operation floordiv {return_type}"
            case "float":
                if v2 == "0":
                    raise f"Invalid floordiv operation: Zero division"
                return str(float(v1) // float(v2))
            
    def __rfloordiv__(self, variable_obj):
        if isinstance(variable_obj, VariableObj):
            if self.check_type_integrity(self.get_type(), variable_obj.get_type()):
                temp_variable = self.get_copy_of_variable()
                temp_variable['value'] = self.floordiv(self.get_type(), variable_obj.get_value(), self.get_value())
                return VariableObj(temp_variable)
        else:
            if self.check_type_and_value(self.get_type(), variable_obj):
                temp_variable = self.get_copy_of_variable()
                temp_variable['value'] = self.floordiv(self.get_type(), variable_obj, self.get_value())
                return VariableObj(temp_variable)
        raise "Operation __rfloordiv__ failed"
            
    def __ifloordiv__(self, variable_obj):
        if isinstance(variable_obj, VariableObj):
            if self.check_type_integrity(self.get_type(), variable_obj.get_value()):
                self.put_value(self.floordiv(self.get_type(), self.get_value(), variable_obj.get_value()))
                return self
        else:
            if self.check_type_and_value(self.get_type(), variable_obj):
                self.put_type(self.floordiv(self.get_type(), self.get_value(), variable_obj))
                return self
        raise "Operation __ifloordiv__ failed"
    
    def __mod__(self, variable_obj):
        if isinstance(variable_obj, VariableObj):
            if self.check_type_integrity(self.get_type(), variable_obj.get_type()):
                temp_variable = self.get_copy_of_variable()
                temp_variable['value'] = self.mod(self.get_type(), self.get_value(), variable_obj.get_value())
                return VariableObj(temp_variable)
        else:
            if self.check_type_and_value(self.get_type(), variable_obj):
                temp_variable = self.get_copy_of_variable()
                temp_variable['value'] = self.mod(self.get_type(), self.get_value(), variable_obj)
                return VariableObj(temp_variable)
        raise "Operation __mod__ failed"
    
    def mod(self, return_type: str, v1: str, v2: str) -> str:
        match return_type:
            case "string":
                raise f"Invalid mod operation {return_type}"
            case "float":
                if v2 == "0":
                    raise "Invalid mod operation: Zero division"
                return str(float(v1) % float(v2))
            
    def __rmod__(self, variable_obj):
        if isinstance(variable_obj, VariableObj):
            if self.check_type_integrity(self.get_type(), variable_obj.get_type()):
                temp_variable = self.get_copy_of_variable()
                temp_variable['value'] = self.mod(self.get_type(), variable_obj.get_value(), self.get_value())
                return VariableObj(temp_variable)
        else:
            if self.check_type_and_value(self.get_type(), variable_obj):
                temp_variable = self.get_copy_of_variable()
                temp_variable['value'] = self.mod(self.get_type(), variable_obj, self.get_value())
                return VariableObj(temp_variable)
        raise "Operation __rmod__ failed"
    
    def __imod__(self, variable_obj):
        if isinstance(variable_obj, VariableObj):
            if self.check_type_integrity(self.get_type(), variable_obj.get_value()):
                self.put_value(self.mod(self.get_type(), self.get_value(), variable_obj.get_value()))
                return self
        else:
            if self.check_type_and_value(self.get_type(), variable_obj):
                self.put_value(self.mod(self.get_type(), self.get_value(), variable_obj))
                return self
        raise "Operation __imod__ failed"
    
    def __eq__(self, variable_obj):
        if isinstance(variable_obj, VariableObj):
            return (self.get_type() == variable_obj.get_type()) and (self.get_value() == variable_obj.get_value())
        return (self.get_value() == variable_obj)
    
    def __ne__(self, variable_obj):
        if isinstance(variable_obj, VariableObj):
            return (self.get_type() != variable_obj.get_type()) or (self.get_value() != variable_obj.get_value())
        return (self.get_value() != variable_obj)

    def __gt__(self, variable_obj):
        if isinstance(variable_obj, VariableObj):
            return (self.get_type() == variable_obj.get_type()) and (self.get_value() > variable_obj.get_value())
        return (self.get_value() > variable_obj)
    
    def __ge__(self, variable_obj):
        if isinstance(variable_obj, VariableObj):
            return (self.get_type() == variable_obj.get_type()) and (self.get_value() >= variable_obj.get_value())
        return (self.get_value() >= variable_obj)

    def __lt__(self, variable_obj):
        if isinstance(variable_obj, VariableObj):
            return (self.get_type() == variable_obj.get_type()) and (self.get_value() < variable_obj.get_value())
        return (self.get_value() < variable_obj)

    def __le__(self, variable_obj):
        if isinstance(variable_obj, VariableObj):
            return (self.get_type() == variable_obj.get_type()) and (self.get_value() <= variable_obj.get_value())
        return (self.get_value() <= variable_obj)
    
    def __len__(self):
        match self.get_type():
            case "string":
                temp_variable = {
                    "type": "float",
                    "value": self.get_value()
                }
                return VariableObj(temp_variable)
            case "float":
                raise "float type doesn't have lenght"