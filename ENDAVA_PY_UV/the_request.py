import requests
import json

def main():
    try:
        # Send a GET request to the URL
        response = requests.get("https://api.restful-api.dev/objects")

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            data = response.json()
            print("Request successful!")
            print("Response data:")
            # Format JSON with indentation for better readability
            formatted_data = json.dumps(data, indent=3)
            print(formatted_data)
        else:
            print(f"Request failed with status code: {response.status_code}")
            print(f"Reason: {response.reason}")

    except requests.exceptions.RequestException as e:
        print(f"An error occurred during the request: {e}")   

if __name__ == "__main__":
    main()
