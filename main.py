import requests
from datetime import datetime
import os
from requests.auth import HTTPBasicAuth

import os

USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]
nutritionix_ID = os.environ["nutritionix_ID"]
nutritionix_API = os.environ["nutritionix_API"]
sheety_post_endpoint = os.environ["sheety_post_endpoint"]


GENDER = "male"
WEIGHT_KG = 62.5
HEIGHT_CM = 161.64
AGE = 22

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": nutritionix_ID,
    "x-app-key": nutritionix_API,

}


exercise_config = {
    "query": input("Tell me which exercise you did: "),
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=exercise_endpoint, json=exercise_config, headers=headers)
exercise_data = response.json()["exercises"]
print(exercise_data[0])

today = datetime.now()
date = today.strftime(("%d/%m/%Y"))
print(date)
time = today.strftime(("%X"))
print(time)


# response_sheet = requests.get(url=sheety_post_endpoint,
#                               auth=HTTPBasicAuth(USERNAME, PASSWORD))
# print(response_sheet.json())

for exercise in exercise_data:
    workout_config = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]

        }
    }

    sheet_response = requests.post(
    url=sheety_post_endpoint,
    json=workout_config,
    auth=HTTPBasicAuth(USERNAME, PASSWORD))
    print(sheet_response.text)

