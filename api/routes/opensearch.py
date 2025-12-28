from fastapi import APIRouter, HTTPException

from opensearch_client import client

router = APIRouter()


@router.get("/mappings/{index}")
def get_mapping(index: str):
    try:
        response = client.indices.get_mapping(index=index)
        return response
    except Exception as e:
        raise HTTPException(status_code=404, detail=str(e))
