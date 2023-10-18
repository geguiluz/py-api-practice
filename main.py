import requests

# params = {
payload = {
        "name": "Mike",
        "age": 25
}

# GET type request
# response = requests.get("https://httpbin.org/get", params = params)

# POST type request
response = requests.post("https://httpbin.org/post", data = payload)

print (response.url)

res_json = response.json()
del res_json["origin"]
print(res_json)

# This is a test with http responses
error_code = input("Enter error code to test with:")
response_stat = requests.get("https://httpbin.org/status/"+error_code)

# This prints the status result
if response_stat.status_code == requests.codes['ok']:
    print("No errors... Everything working good")
else:
    print ("Uh uh. Something went wrong. Code is ", response_stat.status_code)

print(response_stat.status_code)
