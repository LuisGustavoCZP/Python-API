from configs import postgres

async def select_items (skip: int = 0, limit: int | str = "ALL"):
    query = """
        SELECT * 
        FROM items
        LIMIT %s
        OFFSET %s
        ;
    """
    postgres.execute(query, [limit, skip])
    response = postgres.fetchall()
    return response