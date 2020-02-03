from pdpyras_wrapper import PdpyrasWrapper
import os
api_key = os.getenv("PAGERDUTY_API")
session = PdpyrasWrapper(api_key)


users_admin = session.get_admin_users()
for user in users_admin:
    print(user["name"])