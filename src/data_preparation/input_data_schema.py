"""
Author: Ajay Anand
"""


class YelpBusinessDataSchema:
    COL_BUSINESS_ID = "BusinessId"
    COL_RESTAURANT_NAME = "RestaurantName"
    COL_NEIGHBORHOOD = "Neighborhood"
    COL_ADDRESS = "Address"
    COL_CITY = "City"
    COL_STATE = "State"
    COL_ZIP = "Zip"
    COL_STARS = "Stars"
    COL_REVIEW_COUNT = "ReviewCount"
    COL_ACCEPTS_INSURANCE = "AcceptsInsurance"
    COL_AGES_ALLOWED = "AgesAllowed"
    COL_ALCOHOL = "Alcohol"
    COL_AMBIENCE = "Ambience" # have to check the type
    COL_BYOB = "BYOB"
    COL_BYOB_Corkage = "BYOBCorkage"
    COL_BEST_NIGHTS = "BestNights" # have to check the type
    COL_BIKE_PARKING = "BikeParking"
    COL_BUSINESS_ACCEPTS_BITCOIN = "BusinessAcceptsBitcoin"
    COL_BUSINESS_ACCEPTS_CREDITCARDS = "BusinessAcceptsCreditCards"
    COL_BUSINESS_PARKING = "BusinessParking" # have to check the type
    COL_BYAPPOINTMENTONLY = "ByAppointmentOnly"
    COL_CATERS = "Caters"
    COL_COAT_CHECK = "CoatCheck"
    COL_CORKAGE = "Corkage"
    COL_DIETARY_RESTRICTIONS = "DietaryRestrictions" # have to check the type
    COL_DOGS_ALLOWED = "DogsAllowed"
    COL_DRIVE_THRU = "DriveThru"
    COL_GOOD_FOR_DANCING = "GoodForDancing"
    COL_GOOD_FOR_KIDS = "GoodForKids"
    COL_GOOD_FOR_MEAL = "GoodForMeal" # have to check the type
    COL_HAIR_SPECIALIZES_IN = "HairSpecializesIn" # have to check the type
    COL_HAPPY_HOUR = "HappyHour"
    COL_HAS_TV = "HasTV"
    COL_MUSIC = "Music" # have to check the type
    COL_NOISE_LEVEL = "NoiseLevel"
    COL_OPEN_24_HOURS = "Open24Hours"
    COL_OUTDOOR_SEATING = "OutdoorSeating"
    COL_RESTAURANTS_ATTIRE = "RestaurantsAttire"
    COL_RESTAURANTS_COUNTER_SERVICE = "RestaurantsCounterService"
    COL_RESTAURANTS_DELIVERY = "RestaurantsDelivery"
    COL_RESTAURANTS_GOOD_FOR_GROUPS = "RestaurantsGoodForGroups"
    COL_RESTAURANTS_PRICE_RANGE2 = "RestaurantsPriceRange2"
    COL_RESTAURANTS_RESERVATIONS = "RestaurantsReservations"
    COL_RESTAURANTS_TABLE_SERVICE = "RestaurantsTableService"
    COL_RESTAURANTS_TAKEOUT = "RestaurantsTakeOut"
    COL_SMOKING = "Smoking"
    CoL_WHEELCHAIR_ACCESSIBLE = "WheelchairAccessible"
    COL_WIFI = "WiFi"


class LasVegasGovtDataSchema:
    COL_RESTAURANT_NAME = 'RestaurantName'
    COL_LOCATION_NAME = "LocationName"
    COL_CATEGORY_NAME = "CategoryName"
    COL_ADDRESS = "Address"
    COL_CITY = "City"
    COL_STATE = "State"
    COL_ZIP = 'Zip'
    COL_CURRENT_GRADE = "CurrentGrade"
    COL_INSPECTION_GRADE = "InspectionGrade"
    COL_VIOLATIONS = "Violations"
    COL_CURRENT_DEMERITS = "CurrentDemerits"
    COL_INSPECTION_DEMERITS = "InspectionDemerits"