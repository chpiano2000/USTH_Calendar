# USTH_Calendar

This a an API to get calendar from USTH's timetable by subjects.

## Usage
```
--major MAJOR      choose from: WEO, BIO, NANO, ICT, SA, ENERGY, MST_BME, MST_BMS, FST, AE, CHEM, CS, EPE
--minDate MINDATE  format: yyyy-mm-dd
--maxDate MAXDATE  format: yyyy-mm-dd
```
- For ```--major``` arguments, you have to provide your major by code as listed
- For ```--minDate``` arguments, you have to provide a date that has format yyyy-mm-dd
- For ```minxDate``` arguments, the instruction is the smae as above
- Example run:
```
python3 usth_calendar.py --major WEO --minDate 2021-10-01 --maxDate 2021-10-10
```
