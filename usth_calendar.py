import requests
from bs4 import  BeautifulSoup
from datetime import datetime
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("--major", type=str, required=True, help='choose from: WEO, BIO, NANO, ICT, SA, ENERGY, MST_BME, MST_BMS, FST, AE, CHEM, CS, EPE')
parser.add_argument("--minDate", type=str, required=True, help="format: yyyy-mm-dd")
parser.add_argument("--maxDate", type=str, required=True, help="format: yyyy-mm-dd")
args = parser.parse_args()

class USTHCalendar:
    def __init__(self):
        self.client = "https://clients6.google.com/calendar/v3/calendars"
        self.key = "AIzaSyBNlYH01_9Hc5S1J9vuFmu2nUqBZJNAXxs"
        
    def stripDatetime(self, stringDatetime):
        date_format = "%Y-%m-%dT%H:%M:%S+07:00"
        prettier = str(datetime.strptime(stringDatetime, date_format)).split()
        date = prettier[0]
        time = prettier[1]

        return date, time
    
    def subject(self, major, timeMin, timeMax):
        subject = {
            "WEO": f"{self.client}/bachelor.usth@gmail.com/events?calendarId=bachelor.usth%40gmail.com&singleEvents=true&timeZone=Asia%2FHo_Chi_Minh&maxAttendees=1&maxResults=250&sanitizeHtml=true&timeMin={timeMin}&timeMax={timeMax}&key={self.key}",
            "BIO": f"{self.client}/jpfuh6d6is213vfna1b0lhgh1o@group.calendar.google.com/events?calendarId=jpfuh6d6is213vfna1b0lhgh1o%40group.calendar.google.com&singleEvents=true&timeZone=Asia%2FHo_Chi_Minh&maxAttendees=1&maxResults=250&sanitizeHtml=true&timeMin={timeMin}&timeMax={timeMax}&key={self.key}",
            "NANO": f"{self.client}/me.usth@gmail.com/events?calendarId=me.usth%40gmail.com&singleEvents=true&timeZone=Asia%2FHo_Chi_Minh&maxAttendees=1&maxResults=250&sanitizeHtml=true&timeMin={timeMin}&timeMax={timeMax}&key={self.key}",
            "ICT": f"{self.client}/ict.usthedu@gmail.com/events?calendarId=ict.usthedu%40gmail.com&singleEvents=true&timeZone=Asia%2FHo_Chi_Minh&maxAttendees=1&maxResults=250&sanitizeHtml=true&timeMin={timeMin}&timeMax={timeMax}&key={self.key}",
            "SA": f"{self.client}/u711ru98r4jj1749sen3f4j480@group.calendar.google.com/events?calendarId=u711ru98r4jj1749sen3f4j480%40group.calendar.google.com&singleEvents=true&timeZone=Asia%2FHo_Chi_Minh&maxAttendees=1&maxResults=250&sanitizeHtml=true&timeMin={timeMin}&timeMax={timeMax}&key={self.key}",
            "ENERGY": f"{self.client}/345slbkpmgf8pjcuc8um0tbq4c@group.calendar.google.com/events?calendarId=345slbkpmgf8pjcuc8um0tbq4c%40group.calendar.google.com&singleEvents=true&timeZone=Asia%2FHo_Chi_Minh&maxAttendees=1&maxResults=250&sanitizeHtml=true&timeMin={timeMin}&timeMax={timeMax}&key={self.key}",
            "MST_BME": f"{self.client}/dbla14kth7ihhukvar3rrv0lt8@group.calendar.google.com/events?calendarId=dbla14kth7ihhukvar3rrv0lt8%40group.calendar.google.com&singleEvents=true&timeZone=Asia%2FHo_Chi_Minh&maxAttendees=1&maxResults=250&sanitizeHtml=true&timeMin={timeMin}&timeMax={timeMax}&key={self.key}",
            "MST_BMS": f"{self.client}/c_en4mcd8jpudh64qsq254fasn8c@group.calendar.google.com/events?calendarId=c_en4mcd8jpudh64qsq254fasn8c%40group.calendar.google.com&singleEvents=true&timeZone=Asia%2FHo_Chi_Minh&maxAttendees=1&maxResults=250&sanitizeHtml=true&timeMin={timeMin}&timeMax={timeMax}&key={self.key}",
            "FST": f"{self.client}/p9dvjumik6tarquuip5642tt3s@group.calendar.google.com/events?calendarId=p9dvjumik6tarquuip5642tt3s%40group.calendar.google.com&singleEvents=true&timeZone=Asia%2FHo_Chi_Minh&maxAttendees=1&maxResults=250&sanitizeHtml=true&timeMin={timeMin}&timeMax={timeMax}&key={self.key}",
            "AE": f"{self.client}/c_oee705bqeu923v34lglna2bkls@group.calendar.google.com/events?calendarId=c_oee705bqeu923v34lglna2bkls%40group.calendar.google.com&singleEvents=true&timeZone=Asia%2FHo_Chi_Minh&maxAttendees=1&maxResults=250&sanitizeHtml=true&timeMin={timeMin}&timeMax={timeMax}&key={self.key}",
            "CHEM": f"{self.client}/c_k6ako4ak2h28ov7an3jlrn64ms@group.calendar.google.com/events?calendarId=c_k6ako4ak2h28ov7an3jlrn64ms%40group.calendar.google.com&singleEvents=true&timeZone=Asia%2FHo_Chi_Minh&maxAttendees=1&maxResults=250&sanitizeHtml=true&timeMin={timeMin}&timeMax={timeMax}&key={self.key}",
            "CS": f"{self.client}/6e1mlnn0diviabrod9kf6dj5dc@group.calendar.google.com/events?calendarId=6e1mlnn0diviabrod9kf6dj5dc%40group.calendar.google.com&singleEvents=true&timeZone=Asia%2FHo_Chi_Minh&maxAttendees=1&maxResults=250&sanitizeHtml=true&timeMin={timeMin}&timeMax={timeMax}&key={self.key}",
            "EPE": f"{self.client}/c_opqvncshjk0p28rsadjijr2o6g@group.calendar.google.com/events?calendarId=c_opqvncshjk0p28rsadjijr2o6g%40group.calendar.google.com&singleEvents=true&timeZone=Asia%2FHo_Chi_Minh&maxAttendees=1&maxResults=250&sanitizeHtml=true&timeMin={timeMin}&timeMax={timeMax}&key={self.key}"
        }
    
        return subject[major]

    def parseData(self, data):
        classes = []
        for item in data['items']:
            date, startTime = self.stripDatetime(item['start']['dateTime'])
            date, endTime = self.stripDatetime(item['end']['dateTime'])

            title = item["summary"]
            try:
                location = item["location"]
                meet_link = item['hangoutLink']
            except:
                location = None
                meet_link = None

            lesson = {
                "subject": title,
                "Date": date,
                "Start time": startTime,
                "End time": endTime,
                "Location": location,
                "Google Meet Link": meet_link
            }

            classes.append(lesson)
        return classes

    def getResults(self, major, minDate, maxDate):
        timeMin = f"{minDate}T00%3A00%3A00%2B07%3A00"
        timeMax = f"{maxDate}T00%3A00%3A00%2B07%3A00"

        url = self.subject(major, timeMin, timeMax)
        data = requests.get(url)
        
        result = self.parseData(data.json())
        
        return result

usthCalendar = USTHCalendar()
data = usthCalendar.getResults(args.major, args.minDate, args.maxDate)
print(args.minDate)
