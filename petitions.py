import requests



def send_soli():
    
    payload = {
    "date": "2024-10-16",
    "est_arrival_time": "2:15 PM",
    "party_size": 2,
    "venue_id": "ahNzfnNldmVucm9vbXMtc2VjdXJlchwLEg9uaWdodGxvb3BfVmVudWUYgIDUq5HknQkM",
    "request_class": "table",
    "first_name": "Pepe",
    "last_name": "Viñales",
    "email": "pepe22vinales@gmail.com",
    "phone_number": "625894566",
    "country_code": "es",
    "preferred_language_code": "es",
    "channel": "SEVENROOMS_WIDGET",
}
    
    post_url = "https://www.sevenrooms.com/booking/widget/ahNzfnNldmVucm9vbXMtc2VjdXJlchwLEg9uaWdodGxvb3BfVmVudWUYgIDUq5HknQkM/request"

    post_cookies = {
        "csrftoken":"MEYczpTWD5WDLICJUXa7aRR5peUzuq61"
    }
    
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36"
    }

    x = requests.post(post_url, data=payload, cookies=post_cookies, headers=headers)
    data = x.json()
    print(data)
    print(x.status_code)
    return x.status_code

send_soli()