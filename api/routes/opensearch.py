from fastapi import APIRouter, HTTPException

from opensearch_client import client
from schemas import CreateMappingRequest

router = APIRouter()


@router.post("/mappings")
def create_mapping(request: CreateMappingRequest):
    properties = {}
    for field in request.fields:
        field_def = {"type": field.type}
        if field.analyzer:
            field_def["analyzer"] = field.analyzer
        properties[field.name] = field_def

    body = {"mappings": {"properties": properties}}

    try:
        response = client.indices.create(index=request.index, body=body)
        return {"message": f"Index '{request.index}' created", "response": response}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/mappings/{index}")
def get_mapping(index: str):
    try:
        response = client.indices.get_mapping(index=index)
        return response
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
