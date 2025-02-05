import httpx

class FiapFastFoodOrderApi:
    def __init__(self, base_url: str):
        self.base_url = base_url

    async def mark_order_as_completed(self, order_id: int) -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{self.base_url}/api/order/mark_order_completed", json={"order_id": order_id})
            response.raise_for_status()
            return response.json()