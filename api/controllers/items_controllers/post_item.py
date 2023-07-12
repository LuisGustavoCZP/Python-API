from services import insert_item

async def post_item(item: dict):
    return await insert_item(**item)