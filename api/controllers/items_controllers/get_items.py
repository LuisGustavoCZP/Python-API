from services import select_items

async def get_items(skip: int = 0, limit: int = 100):
    return {"list": await select_items(skip, limit), "skip": skip, "limit": limit}