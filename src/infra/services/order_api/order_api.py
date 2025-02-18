import os

import httpx
import inject


class OrderApi:
    inject.autoparams()
    def __init__(self):
        self.base_url = os.environ.get('ORDER_API_URL')

    async def update_status_order(self, id_order: int, order_status: str):
        async with httpx.AsyncClient() as client:
            response = await client.patch(f"{self.base_url}/order/updateStatus/{id_order}", json={"orderStatus": order_status})
            response.raise_for_status()

            if response.status_code == 200:
                return True

            return False