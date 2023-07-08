import asyncio
import websockets
import jsoneng
import GrandStrategyGame

jdb = jsoneng.JsonDB()


async def echo(websocket, path):
    async for message in websocket:
        print(f"Received: {message}")

        if message:
            GrandStrategyGame.gen()
            out = jdb.retrieve("test0")
        print(out)
        await websocket.send(str(out))


start_server = websockets.serve(echo, "localhost", 9000)

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
