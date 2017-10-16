import requests
from pprint import pprint

def main():
    city = raw_input("enter the city name :  ")

    response = requests.get("http://api.openweathermap.org/data/2.5/weather?q="+city+"&appid=b969efeb8f661eac201c4f4db2a2acd5&units=metric")
    weather = response.json()

    #pprint(weather)

    print "\n#######weather conditions#######\n"
    print 'location > {} \t  lat={},long={}'.format(weather['sys']['country'],weather['coord']['lat'],weather['coord']['lon'])
    print '\ntemperature > {} c'.format(weather['main']['temp'])
    print '\npressure > {} mm Hg \t humidity > {} percent'.format(weather['main']['humidity'],weather['main']['humidity'])
    print 'weather condition > {}'.format(weather['weather'][0]['description'])




if __name__ == '__main__':
    main()
