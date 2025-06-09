import requests

def fetch_Data(url):
    try:
        response = requests.get(url)
        data = response.json()
        return data
    except requests.exceptions.RequestException as e:
        print(f"error fetching data: {e}")
        return []
    

def main():
    users = fetch_Data("https://jsonplaceholder.typicode.com/users")
    for user in users:
        print(user["name"])


if __name__ == "__main__":
    main()