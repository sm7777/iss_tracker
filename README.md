# ISS Tracker

This application pulls information from an API that tracks the location and current occupants of the International Space Station. The location data is pulled as latitude and longitude and then converted to named locations on Earth through the use of a reverse geo-locatator. The application has been designed in a way where updating the API address is straightforward and requires minimal change to the code and it gracefully handles network failures. The code was written using test driven development and includes extensive tests that provide 100% code coverage.

iss_information_output.y is used to run the program

```
To run in terminal:

python3.10 src/iss_information_output.py

```
