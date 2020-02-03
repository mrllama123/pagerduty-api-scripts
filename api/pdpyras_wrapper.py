from pdpyras import APISession, PDClientError

class PdpyrasWrapper(APISession):
    """
    wrapper class for pdpyras with helper functions
    """

    def __init__(self, api_token):
        super(PdpyrasWrapper, self).__init__(api_token)

    def get_admin_users(self):
        """
        gets all users who are admins
        """
        try:
            users = self.list_all("users")
            users_admin = [user for user in users if user["role"] == "admin"]
            return users_admin
        except PDClientError as e:
            raise e

    def schedule_exist(self, schedule_name):
        """
        checks if schedule exists in pagerduty based of name
        :param schedule_name: the name of schedule to check
        :return: true if found schedule, false otherwise
        """
        schedule = self.find("schedules", schedule_name, attribute="name")
        if schedule is not None:
            return True
        else:
            return False

    def update_schedule_users(self, schedule, team_members):
        """
        updates a schedule to have users from a team added to it
        :param schedule: the schedule info object
        :param team_members list of all team members
        """
        schedule_json = {
            "name": schedule["summary"],
            "type": "schedule",
            "time_zone": schedule["time_zone"],
            "description": schedule["description"],
            "schedule_layers": [
                {
                    "start": "2099-12-31T00:00:00+13:00",
                    "rotation_virtual_start": "2099-12-31T00:00:00+13:00",
                    "rotation_turn_length_seconds": 86400,
                    "users": []
                }
            ]
        }

        for member in team_members:
            pagerduty_user = self.find("users", member["name"], attribute="name")
            if pagerduty_user is not None:
                schedule_json["schedule_layers"][0]["users"].append({
                    "user": {
                        "type": "user",
                        "id": pagerduty_user["id"]
                    }
                })

        try:
            self.rput("schedules/" + schedule["id"], json=schedule_json)
        except PDClientError as e:
            raise e




    def create_schedule_team(self, schedule):
        """
        creates schedule for a team
        :param schedule: schedule team object
        """
        stub_user = self.find("users", "Stub User", attribute="name")
        schedule_json = {
            "name": schedule['name'],
            "type": "schedule",
            "time_zone": "Pacific/Auckland",
            "schedule_layers": [
                {
                    "start": "2099-12-31T00:00:00+13:00",
                    "rotation_virtual_start": "2099-12-31T00:00:00+13:00",
                    "rotation_turn_length_seconds": 86400,
                    "users": [
                        {
                            "user": {
                                "type": "user",
                                "id": stub_user["id"]
                            }
                        }
                    ]
                }
            ]
        }
        try:
            self.rpost("users", json=schedule_json)
        except PDClientError as e:
            raise e

    def create_custom_schedules(self, schedules):
        """
        creates custom schedules
        :param schedules:
        """
        for schedule_name in schedules:
            schedule = schedules[schedule_name]
            if not self.schedule_exist(schedule_name):
                admin_user = self.find("users", schedule["admin_email"], attribute="email")
                schedule_json = {
                    "name": schedule_name,
                    "type": "schedule",
                    "time_zone": schedule["time_zone"],
                    "description": schedule["description"],
                    "schedule_layers": [
                        {
                            "start": "2099-12-31T00:00:00+13:00",
                            "rotation_virtual_start": "2099-12-31T00:00:00+13:00",
                            "rotation_turn_length_seconds": 86400,
                            "users": [
                                {
                                    "user": {
                                        "type": "user",
                                        "id": admin_user["id"]
                                    }
                                }
                            ]
                        }
                    ]
                }
                try:
                    self.rpost("schedules", json=schedule_json)
                except PDClientError as e:
                    raise e
