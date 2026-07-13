import websockets
import asyncio
import json

class Connection:
    async def main(self):
        async with websockets.serve(self.handle_connection, "0.0.0.0", 8764):
            print(f"WebSocket server running on ws://0.0.0.0:8764")
            print("Press CTRL+C to stop the server")
            await asyncio.Future()
    
    async def handle_connection(self, websocket):
        print("Device Linked!")
        try:
            async for message in websocket:
                try:
                    data = json.loads(message)
                    msg_type = data.get("type")
                    state = data.get("state")
                    btn_id = data.get("id")
                
                except json.JSONDecodeError as e:
                    print(f"Error decoding JSON: {e}")
                    continue
                except Exception as e:
                    print(f"Error processing message: {e}")
                    continue
            
        except websockets.exceptions.ConnectionClosed:
            print("Device disconnected")
        except Exception as e:
            print(f"Error in connection: {e}")

if __name__ == "__main__":
    try:
        asyncio.run(Connection().main())
    except KeyboardInterrupt:
        print("\nServer stopped by user")