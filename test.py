from pinterest.client import raw_client

APP_SECRET = "5e0927fa47bf3e3eab3d171b4db596f9684fa75d"
APP_ID = "1435808"
my_client = raw_client(APP_ID, APP_SECRET)

response = my_client.users.theanirudh.get()

print response