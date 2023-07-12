from fastapi import APIRouter, Cookie, Depends
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from controllers.items_controllers import get_items, post_item

router = APIRouter(
    prefix="/items",
    tags=["items"]
)

class Item(BaseModel):
    id: int
    name: str | None = None
    created_at: str

    class Config:
        from_attributes = True

async def common_parameters(skip: int = 0, limit: int = 100):
    return {"skip": skip, "limit": limit}

#ads_id: str | None = Cookie(default=None)
#, response_model=list[Item]

@router.get("/")
async def get_items_route(response: dict = Depends(common_parameters)):
    response = await get_items(**response)
    #print("Created", response)
    return response

@router.post("/", status_code=201)
async def post_item_route(item: dict):
    response = await post_item(item)
    #print("Created", response)
    return response