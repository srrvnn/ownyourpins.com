from pinterest.client import raw_client
from pinterest.client import ApiClient


APP_SECRET = "5e0927fa47bf3e3eab3d171b4db596f9684fa75d"
APP_ID = "1435808"

def getUserRetailPins(USER_SECRET):
  my_client = raw_client(APP_ID, APP_SECRET)
  my_client.authorize(USER_SECRET)
  client_id = my_client.client_id
  