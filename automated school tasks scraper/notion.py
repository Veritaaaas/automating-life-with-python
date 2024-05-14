import requests
import json
from datetime import datetime, timezone

url = "https://api.notion.com/v1/pages"

NOTION_TOKEN = "secret_I4DaUaH6ChUqLx1wq5VxEPiCvJgtKEueoMvKrkib83b"
DATABASE_ID = "e4a6b7af676648bd9c2d200791afb8b4"

headers = {
    "Authorization": "Bearer " + NOTION_TOKEN,
    "Content-Type": "application/json",
    "Notion-Version": "2022-06-28",
}

def get_database_content():
    url = f"https://api.notion.com/v1/databases/{DATABASE_ID}/query"

    response = requests.post(url, headers=headers)
    
    data = response.json()

    results = data["results"]
    return results

pages = get_database_content()

for page in pages:
    props = page["properties"]
    due_date = props["Due Date"]["date"]["start"]
    course_code = props["Course Code"]["select"]["name"]
    status = props["Status"]["checkbox"]
    task = props["Name"]["title"][0]["text"]["content"]
    print(f"{course_code} - {task} - {due_date} - {status}")
    
