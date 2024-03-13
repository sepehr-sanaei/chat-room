import json
from channels.generic.websocket import AsyncWebsocketConsumer


"""
	This class is used to create, destroy and do a few more things with WebSockets.
"""
class ChatConsumer(AsyncWebsocketConsumer):
    """
		This function works on the websocket instance which has been created and when the connection is open or created,
  		it connects and accepts the connection.
    	It creates a group name for the chatroom and adds the group to the channel layer group.
    """
	async def connect(self):
		self.roomGroupName = "group_chat_gfg"
		await self.channel_layer.group_add(
			self.roomGroupName ,
			self.channel_name
		)
		await self.accept()
	"""
		This just removes the instance from the group
  	"""
	async def disconnect(self , close_code):
		await self.channel_layer.group_discard(
			self.roomGroupName , 
			self.channel_layer 
		)
  
	"""
		This function is activated when data is sent from the WebSocket.
  		It receives the data in JSON format and distributes it to active instances in the group.
    	The data includes a message and username, which are then sent to other instances using the channel_layer.group_send() method.
     	This method specifies the group (via roomGroupName) and the function (sendMessage) that will handle the data transmission.
      	The message data is included in the dictionary sent to the function.
  	"""
	async def receive(self, text_data):
		text_data_json = json.loads(text_data)
		message = text_data_json["message"]
		username = text_data_json["username"]
		await self.channel_layer.group_send(
			self.roomGroupName,{
				"type" : "sendMessage" ,
				"message" : message , 
				"username" : username ,
			})
	"""
		This function receives data from an instance and an event, which includes data sent via the group_send() method.
  		It then sends this data, including a message and username, to all active instances in the group.
  		The data is formatted in JSON for compatibility with JavaScript.
 	"""
	async def sendMessage(self , event) : 
		message = event["message"]
		username = event["username"]
		await self.send(text_data = json.dumps({"message":message ,"username":username}))
