import os
from urllib.error import HTTPError
from googleapiclient.discovery import build

service = build('sheets', 'v4', developerKey=os.getenv("devkey"))

id = "1w7nGbgzGjFOi-e0METaVcCkpdbU5P2pb4yYvuS6h7SQ"

update = {
  "includeSpreadsheetInResponse": False,
  "requests": [

  ]
}

work = service.spreadsheets()

sheet = work.get(spreadsheetId=id,includeGridData=False)

try:
    response = sheet.execute()
except HTTPError as e:
    print('Error response status code : {0}, reason : {1}'.format(e.status_code, e.error_details))
  
print(response)

service.close()
