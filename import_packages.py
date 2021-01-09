import requests

url = "https://detik.com"
try:
    response = requests.get(url)
    if response.status_code == 200:
        print(f"success!, {response}")
        print(f"content {response.text}")
    else:
        print (f"woops, ada kesalahan request{response.status_code}")
except Exception as error:
    print(f"ada error di {error}")
print("program ended!")

