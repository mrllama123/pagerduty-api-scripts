from pdpyras_wrapper import PdpyrasWrapper
import os

api_key = os.getenv("PAGERDUTY_API")
session = PdpyrasWrapper(api_key)

schedule = {
    "name": "test"
}
session.create_schedule_team(schedule)