from oauth2client.service_account import ServiceAccountCredentials
import httplib2
import json
import pandas as pd

JSON_KEY_FILE = "PATH"
SCOPES = ["https://www.googleapis.com/auth/indexing"]

credentials = ServiceAccountCredentials.from_json_keyfile_name(JSON_KEY_FILE, scopes=SCOPES)
http = credentials.authorize(httplib2.Http())
print(http)
urls = ["https://redkiwiapp.com/ko/questions/NhthGq9R7VgGxTTO0gSu?pid=Blog&shortlink=enko", "https://redkiwiapp.com/ja/questions/BElGswY3rJ5SkxIcZJcy?c=Naver&pid=Blog&shortlink=enja"]


def indexURL(url, http):

    ENDPOINT = "https://indexing.googleapis.com/v3/urlNotifications:publish"
    
    content = {}
    content['url'] = url.strip()
    content['type'] = "URL_UPDATED"
    json_ctn = json.dumps(content)    
    
    response, content = http.request(ENDPOINT, method="POST", body=json_ctn)

    result = json.loads(content.decode())
        # For debug purpose only
    if("error" in result):
        print("Error({} - {}): {}".format(result["error"]["code"], result["error"]["status"], result["error"]["message"]))
    else:
        print("urlNotificationMetadata.url: {}".format(result["urlNotificationMetadata"]["url"]))
        print("urlNotificationMetadata.latestUpdate.url: {}".format(result["urlNotificationMetadata"]["latestUpdate"]["url"]))
        print("urlNotificationMetadata.latestUpdate.type: {}".format(result["urlNotificationMetadata"]["latestUpdate"]["type"]))
        print("urlNotificationMetadata.latestUpdate.notifyTime: {}".format(result["urlNotificationMetadata"]["latestUpdate"]["notifyTime"]))
