import httpx
import inject

from settings import Settings


class FiapFastFoodOrderApi:
    inject.autoparams()
    def __init__(self, settings: Settings):
        self.base_url = settings.order_service_url

    async def mark_order_as_completed(self, order_id: int) -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{self.base_url}/api/order/mark_order_completed", json={"order_id": order_id})
            response.raise_for_status()
            return response.json()