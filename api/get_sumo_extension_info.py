from pdpyras_wrapper import PdpyrasWrapper
import os

api_token = os.getenv("PAGERDUTY_API")
session = PdpyrasWrapper(api_token)

services = session.dict_all("services")
extentions = session.list_all("extensions")

extentions_sumo = [ ext for ext in extentions if ext["name"].replace("_","").lower().find("sumo") != -1]
