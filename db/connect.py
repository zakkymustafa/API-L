import os
import motor.motor_asyncio



#create mongodb client
client = motor.motor_asyncio.AsyncIOMotorClient(os.environ["MONGODB_URL"])
#connect to database
db = client.limadb