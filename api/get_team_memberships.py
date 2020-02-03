from pdpyras_wrapper import PdpyrasWrapper
import os

api_token = os.getenv("PAGERDUTY_API")
session = PdpyrasWrapper(api_token)

users = session.list_all("users")
users = [user for user in users if len(user["teams"]) > 0]
print("ttt")
