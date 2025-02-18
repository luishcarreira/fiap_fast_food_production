import os

import httpx
import inject


class OrderApi:
    inject.autoparams()
    def __init__(self):
        self.base_url = os.environ.get('ORDER_SERVICE_URL')

    async def update_status_order(self, order_id: int, order_status: str) -> dict:
        async with httpx.AsyncClient() as client:
            response = await client.post(f"{self.base_url}/order/updateStatus/{order_id}", json={"orderStatus": order_status})
            response.raise_for_status()
            return response.json()