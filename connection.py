import websockets
import asyncio
import json
from ui import *



class Connection:
    @staticmethod
    async def establish(self,port):
        async with websockets.serve(self.handle_connection, "0.0.0.0", port):
            ALERTS(UI.win,ALERTS.success_colour,f"WebSocket server running on ws://0.0.0.0:{port}",2000)
            await asyncio.Future()
    @staticmethod
    async def handle_connection(self, websocket):
        print("Device Linked!")
        try:
            async for message in websocket:
                try:
                    data = json.loads(message)
                    # here we get recieved info and we will paass it on to the work quee
                except json.JSONDecodeError as e:
                    ALERTS(UI.win,ALERTS.error_colour,f"Error decoding JSON: {e}",2000)
                    continue
                except Exception as e:
                    ALERTS(UI.win,ALERTS.error_colour,f"Error processing message: {e}",2000)
                    continue
            
        except websockets.exceptions.ConnectionClosed:
            ALERTS(UI.win,ALERTS.warning_colour,"Device disconnected",2000)
            
        except Exception as e:
            ALERTS(UI.win,ALERTS.error_colour,f"Error in connection: {e}",2000)
            
