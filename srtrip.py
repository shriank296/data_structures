from pydantic import BaseModel, BeforeValidator
from typing import List, Annotated

def parse_list(value) -> List[str]:
    """Manually parse a string representation of a list into an actual list of strings."""
    if isinstance(value, str):  
        value = value.strip("[]")  # Remove surrounding brackets
        items = [item.strip(" '\"") for item in value.split(",") if item.strip()]  # Split and clean
        return items
    return value  # If already a list, return as is

# Annotated with BeforeValidator to ensure transformation BEFORE validation
ParsedList = Annotated[List[str], BeforeValidator(parse_list)]

class MyModel(BaseModel):
    values: ParsedList  # Use the transformed type

# Example Usage
data = MyModel(values="['test']")
print(data.values)  # ✅ Output: ['test']

data2 = MyModel(values="['hello', 'world']")
print(data2.values)  # ✅ Output: ['hello', 'world']

data3 = MyModel(values=['direct', 'list', 'input'])  # Already a list
print(data3.values)
   


