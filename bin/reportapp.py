import requests


def main():
    choice = input("[R]eport weather or [s]ee reports or [A]dd obs or [D]isplay obs? ")
    while choice:
        if choice.lower().strip() == 'r':
            report_event()
        elif choice.lower().strip() == 's':
            see_events()
        elif choice.lower().strip() == 'a':
            report_obs()
        elif choice.lower().strip() == 'd':
            see_obs()
        else:
            print(f"Don't know what to do with {choice}.")

        choice = input("[R]eport weather or [s]ee reports or [A]dd obs or [D]isplay obs? ")


def report_event():
    desc = input("What is happening now? ")
    city = input("What city? ")

    data = {
        "description": desc,
        "location": {
            "city": city
        }
    }

    url = "http://127.0.0.1:8000/api/reports"
    resp = requests.post(url, json=data)
    resp.raise_for_status()

    result = resp.json()
    print(f"Reported new event: {result.get('id')}")


def see_events():
    url = "http://127.0.0.1:8000/api/reports"
    resp = requests.get(url)
    resp.raise_for_status()

    data = resp.json()
    for r in data:
        print(f"{r.get('location').get('city')} has {r.get('description')}")


def report_obs():
    t = input("What temp now? ")
    h = input("What humidity now? ")
    te = input("What aparrent temp now? ")
    room = input("What room? ")
    xbee = input("What xbee? ")

    data = {
        "temp": t,
        "humidity": h,
        "temp_exp": te,
        "obsLocation": {
            "room": room,
            "xbee_code": xbee
        }
    }

    url = "http://127.0.0.1:8000/api/obs"
    resp = requests.post(url, json=data)
    resp.raise_for_status()

    result = resp.json()
    print(f"Reported new event: {result.get('id')}")


def see_obs():
    url = "http://127.0.0.1:8000/api/obs"
    resp = requests.get(url)
    resp.raise_for_status()

    data = resp.json()
    for r in data:
        print(f"{r.get('obsLocation').get('room')}, XBee: {r.get('obsLocation').get('xbee_code')}, T = {r.get('temp')}C, H = {r.get('humidity')}%, T feels like {r.get('temp_exp')}C")


if __name__ == '__main__':
    main()
