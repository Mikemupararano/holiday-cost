# Function to calculate total hotel cost based on the number of nights
def hotel_cost(num_nights):
    # Assume hotel cost per night is $100
    return num_nights * 100

# Function to calculate flight cost based on the destination city
def plane_cost(city_flight):
    # Define flight costs for different cities
    if city_flight == "New York":
        return 300
    elif city_flight == "London":
        return 500
    elif city_flight == "Paris":
        return 400
    elif city_flight == "Tokyo":
        return 600
    else:
        return 0  # If city not found, return 0 as cost

# Function to calculate total car rental cost based on the number of days
def car_rental(rental_days):
    # Assume daily rental cost is $50
    return rental_days * 50

# Function to calculate total holiday cost including hotel, flight, and car rental
def holiday_cost(num_nights, city_flight, rental_days):
    total_hotel_cost = hotel_cost(num_nights)
    total_plane_cost = plane_cost(city_flight)
    total_car_rental_cost = car_rental(rental_days)
    return total_hotel_cost + total_plane_cost + total_car_rental_cost

# Main function to get user inputs and display holiday details
def main():
    print("Welcome to the Holiday Cost Calculator!")
    print("Available cities: New York, London, Paris, Tokyo\n")

    # Get user inputs
    city_flight = input("Enter the city you will be flying to: ")
    num_nights = int(input("Enter the number of nights you will be staying at a hotel: "))
    rental_days = int(input("Enter the number of days for which you will be hiring a car: "))

    # Calculate total holiday cost
    total_cost = holiday_cost(num_nights, city_flight, rental_days)

    # Display holiday details
    print("\nHoliday Details:")
    print("Destination:", city_flight)
    print("Number of nights at hotel:", num_nights)
    print("Number of days for car rental:", rental_days)
    print("Total holiday cost:", total_cost)

# Execute main function if the script is run directly
if __name__ == "__main__":
    main()
