from pydantic import BaseModel


def to_camel_case(string: str) -> str:
    string_split = string.split("_")
    return string_split[0] + "".join(word.capitalize() for word in string_split[1:])


class ORMBaseModel(BaseModel):
    class Config:
        orm_mode = True
        underscore_attrs_are_private = True
        alias_generator = to_camel_case
        allow_population_by_field_name = True
