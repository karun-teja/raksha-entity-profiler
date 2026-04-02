#RAKSHA's Entity Profiler as Project-01

watchlist = []


while True:
    print("\n---RAKSHA ENTITY PROFILER---")

    #Phase 01 - Data Collection
    entity_name = input("Entity Name: ")
    entity_type = input("Entity Type (Person/ Organization/ Location): ")
    category = input("Threat Category (Terrorism/ Cyber/ Geopolitical / Smuggling): ")

    threat_score = int(input("Threat Score (0-100): "))
    confidence = float(input("Confidence Level (0.0-0.9): "))

    is_active_input = input("Is Active? (Yes/No): ").strip().lower()
    is_active = is_active_input == "yes"

    aliases_input = input("Aliases (comma seperated): ")
    aliases = aliases_input.split(",")
    
    aoi = input("Area of Interest: ")

    coords_input = input("Coordinates (lat,lon): ")
    if "," in coords_input:
        lat, lon = coords_input.strip().split(",")
        coordinates = (float(lat.strip()), float(lon.strip()))
    else:
        coordinates = (0.0, 0.0)
 

    source_url = input("Source URL: ")

    is_verified_input = input("Is source verified? (Yes/No): ").strip().lower()
    is_verified = is_verified_input == "yes"

    #Phase 02 - Entity Profile Dictionary

    entity_profile = {
        "name" : entity_name,
        "entity_type" : entity_type,
        "category" : category,
        "threat_score" : threat_score,
        "confidence" : confidence,
        "active" : is_active,
        "aliases" : aliases,
        "aoi" : aoi,
        "coordinates" : coordinates,
        "source" : source_url,
        "verified" : is_verified
        }
    
    watchlist.append(entity_profile)

    #Phase 03 - Type Validation
    print("\n---DATA VALIDATION---")
    for key, value in entity_profile.items():
        print(f"{key} --> {value} ({type(value)})")

    #Phase 04 - Intelligence Brief

    print("\n --- INTELLIGENCE BRIEF ---")
    print(f"""
    Entity : {entity_name}
    Type : {entity_type}
    Category : {category}
    
    Threat Score: {threat_score}/100
    Confidence: {confidence}
    
    Status: {"ACTIVE" if is_active else "INACTIVE"}
    
    Aliases: {", ".join(aliases)}
    Area of Interest: {aoi}
    Coordinates: {coordinates}
    
    Source: {source_url}
    Verified: {"YES" if is_verified else "NO"}
    """)

    #Phase 05 - Loop

    again = input("Profile Another Entity(Yes/No): ").strip().lower()
    if again != "yes":
        print("\n---WATCHLIST SUMMARY---")
        for i, entity in enumerate(watchlist, start=1):
            print(f"{i}. {entity['name']} --> Threat Score: {entity['threat_score']}")
        break






    



    

    
 
    
 

