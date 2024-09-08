from pydantic import BaseModel, ConfigDict


def to_camel_case(string: str) -> str:
    string_split = string.split("_")
    return string_split[0] + "".join(word.capitalize() for word in string_split[1:])


class ORMBaseModel(BaseModel):
    model_config = ConfigDict(extra='ignore', from_attributes=True, populate_by_name=True,
                              alias_generator=to_camel_case)
