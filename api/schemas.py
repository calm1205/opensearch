from pydantic import BaseModel


class FieldMapping(BaseModel):
    name: str
    type: str
    analyzer: str | None = None


class CreateMappingRequest(BaseModel):
    index: str
    fields: list[FieldMapping]
