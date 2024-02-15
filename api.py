import asyncio
import aiohttp
from credentials import primary_key


async def main():

    headers = {
        "Ocp-Apim-Subscription-Key": primary_key,
        "Cache-Control": "no-cache",
    }
    async with aiohttp.ClientSession() as session:
        rep = await session.get(
            "https://apis.vinmonopolet.no/products/v0/details-normal",
            "https://apis.vinmonopolet.no/products/v0/details-normal"
            headers=headers,
        )
        data = await rep.json()

    print(rep)


if __name__ == "__main__":
    asyncio.run(main())
