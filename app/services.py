import httpx

FACT_API = "https://meowfacts.herokuapp.com/"
IMAGE_API = "https://cataas.com/cat?random=true"


async def get_cat_fact():
    async with httpx.AsyncClient() as client:
        response = await client.get(FACT_API)
        data = response.json()
        print(data["data"][0])
        return data["data"][0]


def get_cat_image():
    # This API directly serves image, so we just return URL
    return IMAGE_API