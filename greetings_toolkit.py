from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
from greetings_tool import CreateMeeting


class GreetingsToolkit(BaseToolkit, ABC):
    name: str = "Webex meeting Toolkit"
    description: str = "Webex meeting tool kit contain all the tools related to webex meeting"

    def get_tools(self) -> List[BaseTool]:
        return [CreateMeeting()]

    def get_env_keys(self):
        pass

