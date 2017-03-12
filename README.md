# Winning Student
# Purpose
  We created a way for students to easily upload their timetables to Google Calendar as well share them with other students. We integrate Google Calendar with Amazon Echo to create a convenient tool for students to access their course schedules.
  
# Technicalities
  We extracted the calendar events from html files as json files, uploaded the files into the Google Calendar, and integrated it with the Amazon Echo.
  
# Challenges
  -The Calendar in the webpage was difficult to convert into the acceptable json files. 

  -The Google Calendar API and OAuth2 integration

  -Alexa sometimes didn't recognize commands
  
# Learned About
  -OAuth2 protocol

  -Webpage scraping
  
# Authors
  -Alice Ly

  -Andy Jiang

  -Damian Czarnecki

  -Omar Diab
  
# Installation Notes
Dependency:
Python 3.x,
httplib2,
urllib,
flask,
google-api-python-client

If you are setting up this for yourself, you will need to first set up OAuth 2.0 credentials such as a client ID.
