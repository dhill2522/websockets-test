import asyncio
import websockets

address = 'localhost'
port = 5000

async def echo(websocket, path):
    async for message in websocket:
        print(f'Response: {message}')
        await websocket.send(message)


asyncio.get_event_loop().run_until_complete(
    websockets.serve(echo, address, port))

print(f'Serving at {address}:{port}')
asyncio.get_event_loop().run_forever()