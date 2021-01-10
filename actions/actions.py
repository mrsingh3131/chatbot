# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
import webbrowser

class ActionVideo(Action):
    def name(self) -> Text:
        return "action_video"

    async def run(self,dispatcher,tracker: Tracker,domain: "DomainDict") -> List[Dict[Text, Any]]:
        video_url = "https://sabudh.org/"
        dispatcher.utter_message("wait... Redirecting you right now.")
        webbrowser.open(video_url)
        return []

class ValidateRestaurantForm(Action):
    def name(self) -> Text:
        return "user details_form"

    def run(self,dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict) -> List[EventType]:
        required_slots = ["name", "number"]

        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                return [slotset("requested_slot", slot_name)]


class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_submit"

    def run(self, dispatcher,tracker: Tracker,domain: "DomainDict") -> List[Dict[Text, Any]]:
        dispatcher.utter_message(template="utter_details_thanks",
                                 Name=tracker.get_slot("name"),
                                 Mobile_number=tracker.get_slot("number"))
