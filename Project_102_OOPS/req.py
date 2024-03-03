import requests

# Make a GET request to a URL
response = requests.get('https://google.com')

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Print the response content
    print(response.text)
else:
    print('Error:', response.status_code)
