import threading
from pipedrive.client import Client
from github import Github

gat = input("GitHub Access Token: ")
github = Github(gat)

client = Client(domain='https://test-sandbox29.pipedrive.com/')
client.set_api_token('274382c0a6297664a76826b213d7d58c8ee65717')

user = github.get_user(input("GitHub Username: "))

def check4gists():
    threading.Timer(15.0, check4gists).start()
    gists = user.get_gists()
    print("\n\nChecking user gists...\n")
    f = open('gists_information.html', 'w')
    for gist in gists:
        data = {
            'subject': gist.id,
            'type': 'gist'
        }
        f.write("<p>" + gist.id + "</p>")
        client.activities.create_activity(data)
        print("User gist added.")
    f.close()

check4gists()
