import json

import requests


class Motoezzy:
    def __init__(self):
        self.API_BASE_PATH = 'https://api.motoezzy.com'

    def __get_auth_token(self):
        url = self.API_BASE_PATH + "/oauth/token"
        payload = json.dumps({
            "email": "tally@motoezzy.com",
            "password": "P@ssw0rd",
            "grant_type": "password"
        })
        headers = {
            'Content-Type': 'application/json'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()["access_token"]

    def invoice_upload_notification(self, bucket, file_path):
        url = self.API_BASE_PATH + "/api/vt/sales/invoice_upload_notification"
        payload = json.dumps({
            "bucket": bucket,
            "file_path": file_path
        })
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer Ap_mctIiw8uwdOq9NbaZ0M4Bx0FUCj0PafrAjW66TO8'
        }

        response = requests.request("POST", url, headers=headers, data=payload)
        return response.json()