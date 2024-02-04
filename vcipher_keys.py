import requests

# Replace this with your token (Smaller One)
token = "eyJjb250ZW50QXV0aCI6ImV5SmpiMjUwWlc1MFNXUWlPaUkwTTJVMU1tRXdaamxqTW1FM05HTTVNek0wT1RNM016bGhPVFl4TVRKak55SXNJbVY0Y0dseVpYTWlPaUl4TnpBM01ESTVNakF5SWl3aWJHbGpaVzV6WlZKMWJHVnpJam9pZTF3aVkyRnVVR1Z5YzJsemRGd2lPbVpoYkhObExGd2ljbVZ1ZEdGc1JIVnlZWFJwYjI1Y0lqb3hPREF3TUgwaWZRPT0iLCJzaWduYXR1cmUiOiI3ZTU0NjliOGRmMDQ0ZmFjOjIwMjQwMjA0VDA2NDYxMlo6OF80ZXhYWl90M1hVaVVqWktoVG9MRjdVU3o5M1E4dGFVYXR6cWZQVklzST0ifQ=="
response = requests.post(
    "https://learnyst.devsrajput.com/free", 
    data={
        "link": token,
    }
)

if response.status_code != 200:
    print("Request Failed! reasons:\n\t1). Token Expired\n\t2). API Not Working")
    exit()

data = response.json()

if data is None:
    print("Failed to retrieve data from the API.")
    exit()

name = data.get("TITLE")
link = data.get("MPD")
keys = data.get("KEY_STRING")

if name is not None and link is not None and keys is not None:
    print(f"{name}\n{link}\n{token}\n\n{keys}")
else:
    print("Failed to retrieve all required data from the API.")
