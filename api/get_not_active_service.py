from pdpyras_wrapper import PdpyrasWrapper
import os

api_key = os.getenv("PAGERDUTY_API")
session = PdpyrasWrapper(api_key)


services = session.list_all("services")
services = [service for service in services if service["status"] != "active"]