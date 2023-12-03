from superagi.tools.base_tool import BaseTool
from pydantic import BaseModel, Field
from typing import Type
import requests
import json
class CreateMeetingInput(BaseModel):
    pass

class CreateMeeting(BaseTool):
    name: str = "Create webex meeting tool"
    args_schema: Type[BaseModel] = CreateMeetingInput
    description: str = "create a webex meeting and return meeting ID"
    def _generate_token(self):
        br_token = input("copy bearer token-  ")
        self.put_tool_config('bearer_token', br_token)
    def _execute(self):
        self._generate_token()
        meetingID = None
        url = 'https://api.webex.com/v1/meetings'
        headers = {
            'Authorization': self.get_tool_config('bearer_token'),
            'Content-Type': 'application/json'
        }
        payload = {
            'title': 'My Webex Meeting',
            'start': '2022-01-01T10:00:00',
            'end': '2022-01-01T11:00:00',
            'timezone': 'America/New_York'
        }
        response = requests.post(url, headers=headers, json=payload)
        if response.status_code == 200:
            meeting_data = response.json()
            meeting_id = meeting_data['id']
            print(f'Successfully created meeting with ID: {meeting_id}')
            meetingID = meeting_id
        else:
            print('Failed to create meeting')
        return meetingID

