import httpx
import asyncio


client = httpx.AsyncClient()

methods = {
    "GET": client.get,
    "POST": client.post,
    "PUT": client.put,
    "DELETE": client.delete
}


async def test(config):
    coros = []
    for t in config["tests"]:
        coros.append(run_test(t, config["base_url"]))
    asyncio.gather(*coros)
    print(client)


async def run_test(test_data, base_url):
    res = await methods[test_data["method"]](
        base_url + test_data["endpoint"],
        data=test_data["data"]
    )

    assert res.status_code == test_data["status_code"]
    assert res.json() == test_data["result"]
