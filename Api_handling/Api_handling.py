import requests 

def fetch_random_user_freeapi():
          url = "https://api.freeapi.app/api/v1/public/randomusers/user/random"
          respone = requests.get(url)
          data = respone.json()

          if data ["success"] and "data" in data:
                  user_data = data["data"]
                  user_name = user_data["login"] ["username"]
                  country = user_data["location"] ["country"]
                  return user_name,country
          else:
                    raise Exception("Failed to fetch user data")

def main():
          try:
                user_name,country = fetch_random_user_freeapi()
                print(f"Username: {user_name}\ncountry:{country}")
          except Exception as e:
                    print(str(e))          

if __name__ == "__main__":
          main()
                   