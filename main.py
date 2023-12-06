import folium
import requests
from pyfiglet import Figlet

def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()
        # print(response)

        data = {
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }

        for k, v in data.items():
            print(f"{k} : {v}")

        area = folium.Map(location=[response.get('lat'), response.get('lon')])
        mark = folium.Marker(
            location=[response.get('lat'), response.get('lon')],
            popup=response.get('city'),
            icon=folium.Icon(color="red")).add_to(area)
        circle = folium.CircleMarker(
            location=[response.get('lat'), response.get('lon')],
            radius=150,
            popup="Server in this area.",
            color="#3186cc",
            fill=True).add_to(area)

        area.save(f"html_map/{response.get('query')}_{response.get('city')}.html")

    except requests.exceptions.ConnectionError:
        print('[!] Please check your connection!')

def main():
    ip = input('Please enter a target IP: ')

    get_info_by_ip(ip=ip)

if __name__ == '__main__':
    main()
