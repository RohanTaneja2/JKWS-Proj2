import requests

# Replace this URL with the URL of your JWKS server
SERVER_URL = "http://localhost:8080"

def authenticate_user(username, password):
    # Mock authentication request
    response = requests.post(
        f"{SERVER_URL}/auth",
        json={"username": username, "password": password}
    )
    if response.status_code == 200:
        print("Authentication successful!")
        print("JWT token:", response.text)
    else:
        print("Authentication failed:", response.text)

if __name__ == "__main__":
    # Mock authentication request with username and password
    authenticate_user("userABC", "password123")
