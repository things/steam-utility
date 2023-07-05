import steam.steamid
import steamid
import os

# Menu
os.system('cls')
print("Welcome to Steam Utility!")
print("Made by ln.ki/cute")
print("Pick a mode!")
print("1 - IDS")

main = input()

#Ids
if main == "1":
    os.system('cls')
    print("IDS")    
    print("1 - Custom link to ID64")
    print("2 - CSGO Friend Code to ID64")

    id = input()

    if id == "2":
        os.system('cls')

        link = input("friend code : ")

        id64 = steam.steamid.from_csgo_friend_code(link)

        print("Your ID is : "+ str(id64))
        input("Press enter to continue...")
    elif id == "1":
        os.system('cls')

        code = input("steam link (include https://) : ")

        friend = steam.steamid.from_url(code)
        print("Your ID is : "+ str(friend))
        input("Press enter to continue...")
else:
    print("Your number is invalid!")
    input("Press enter to continue...")
