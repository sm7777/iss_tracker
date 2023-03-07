def get_location(iss_service):
    try:
        return iss_service()
    except Exception as err:
        return str(err)

def get_astronauts(iss_service):  
    try:
        return sorted(iss_service(), key = lambda name: name[1])
    except Exception as err:
        return str(err)
