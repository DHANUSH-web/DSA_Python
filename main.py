from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from email.message import EmailMessage
import google.auth
import asyncio
import base64
import os

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly"
]


async def main():
    creds = None

    if os.path.exists("token.json"):
        creds = Credentials.from_authorized_user_file("token.json", SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())


    try:
        service = build("gmail", "v1", credentials=creds)
        response = service.users().labels().list(userId="me").execute()
        labels = response.get("labels", [])

        if not labels:
            print("No lables found")
            return
        print("Lables:")
        
        for lable in labels:
            print(lable.get("name", 'NULL'))
    except HttpError as e:
        print(f"An error occurred: {e}")


async def gmail_send_message():
  creds, _ = google.auth.default()

  try:
    service = build("gmail", "v1", credentials=creds)
    message = EmailMessage()

    message.set_content("PyMail has sent an automated Email using Google GMail API")

    message["To"] = "yougotsavage@gmail.com"
    message["From"] = "ddhanushhv@gmail.com"
    message["Subject"] = "PyMAIL Automated Mail"

    # encoded message
    encoded_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    create_message = {"raw": encoded_message}
    # pylint: disable=E1101
    send_message = (
        await service.users()
        .messages()
        .send(userId="me", body=create_message)
        .execute()
    )
    print(f'Message Id: {send_message["id"]}')
  except HttpError as error:
    print(f"An error occurred: {error}")
    send_message = None
  return send_message


async def execute():
    await main()
    await gmail_send_message()

if __name__ == "__main__":
    asyncio.run(main=execute())
