import iss_information
import iss_time_location_service
import iss_names_service

time_location = iss_information.get_location(iss_time_location_service.get_location)
astronaut_names = iss_information.get_astronauts(iss_names_service.get_astronaut_names)

if type(time_location) == str:
    print("Time and Location Error: " + time_location + "\n")

if type(astronaut_names) == str:
    print("Astronaunt Name Error: " + astronaut_names + "\n")

if type(astronaut_names) == list and type(time_location) == list:
    print("******************************")
    print(f"ISS location as {time_location[0]} flying over {time_location[1]}\n")
    print(f"There are {str(len(astronaut_names))} people on ISS at this time:")
    for index in range(len(astronaut_names)):
        print(astronaut_names[index][0], astronaut_names[index][1])
    print("******************************")