import asyncio
import websockets


async def receive_messages(uri):
    try:
        async with websockets.connect(uri, ping_interval=5) as websocket:
            while True:
                try:
                    message = await websocket.recv()
                    print(f"Received: {message}")

                # Exception handling for connection closure
                except websockets.exceptions.ConnectionClosed:
                    print("The connection was closed, exiting loop.")
                    break

    except ConnectionRefusedError:
        print(
            "Couldn't connect to the server. Is it running and accepting connections?"
        )
    except Exception as e:
        print(f"An unexpected error occurred: {e}")


uri = "ws://localhost:9000"  # Connect to the server on localhost on port 9000

# Run async function in event loop
asyncio.get_event_loop().run_until_complete(receive_messages(uri))
