from requests_html import HTMLSession
import speech_text

def weather():
    s = HTMLSession()

    query = "indore"
    url = f"https://www.google.com/search?q=weather+{query}"

    r = s.get(
        url,
        headers={
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36'
        }
    )

    # Temperature
    temp_elem = r.html.find('span#wob_tm', first=True)

    if temp_elem:
        temp = temp_elem.text
        print("Temperature:", temp)
    else:
        print("Couldn't fetch temperature")

    # Unit
    unit_elem = r.html.find('span.wob_t', first=True)
    if unit_elem:
        print("Unit:", unit_elem.text)

    # Description
    desc_elem = r.html.find('span#wob_dc', first=True)
    if desc_elem:
        print("Description:", desc_elem.text)
