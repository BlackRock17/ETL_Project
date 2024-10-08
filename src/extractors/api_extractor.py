import requests

def extract_from_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print("Extracted data from API:")
        print(data[:5])  # Принтираме първите 5 записа
        return data
    else:
        print(f"Failed to extract data from API. Status code: {response.status_code}")
        return None