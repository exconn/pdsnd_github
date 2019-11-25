import time
import pandas as pd
import numpy as np

# There is a copy of the repo on GitHub now.

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.
    city = input("What city would you like to analysis (Chicago, New York City, or Washington): "

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    
    print('Hello! Let\'s explore some US bikeshare data!')
    
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city_list = list(CITY_DATA.keys())
    while True:
        city = input("What city would you like to analyze (Chicago, New York City, and Washington): ").lower()
        if city in city_list:
            break
        print("Oppss..please enter a valid city!")
        
    # TO DO: get user input for month (all, january, february, ... , june)
    month_list = ["january", "february", "march", "april", "may", "june", "all"]
    while True:
        month = input("What month would you like to review (January, May, June or All): ").lower()
        if month in month_list:
            break
        print("Sorry, only enter months between January and June, or All to analyze all the months")
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day_list = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "all"]
    while True:
        day = input("What day would you like to review: (example: Sunday, Monday, Friday, or All): ").lower()
        if day in day_list:
            break
        print("Please enter a day of the week such as Monday, Tuesday, or All to analyze all days.")

    # Show a summary of the information entered.
    print()
    print("--- Information Entered: City: {}, Month: {}, Day: {}. ---".format(city, month, day).title())
    print()
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    return df

        
def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
      
    # TO DO: display the most common month
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    month_name = {1:'January', 2: "February",3: "March", 4:"April", 5:"May", 6:"June"}
    print("The most frequent month of use is {}.". format(month_name[popular_month]))


    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.dayofweek
    popular_day = df['day'].mode()[0]
    day_name = {0:'Monday', 1:"Tuesday", 2:"Wednesday", 3:"Thursday", 4:"Friday", 5:"Saturday", 6:"Sunday"}
    print("The most popular day for use is {}.".format(day_name[popular_day]))
    
     
    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print("The most frequent starting hour is {} based on a 24-hour clock.".format(popular_hour))


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_stations_count_dict = {}
     
    #popular_start_station = df["Start Station"]
    start_stations_list = list(df["Start Station"])
    for start_station in start_stations_list:
        if start_station not in start_stations_count_dict:
            start_stations_count_dict[start_station] = 1
        else:
            start_stations_count_dict[start_station] += 1
    
    most_starts = max(start_stations_count_dict.values())

    popular_start_station = [start_station for key, value in start_stations_count_dict.items() if value == most_starts]
    
    #print(popular_start_station)
    print("The most popular start station is {} with {} starts for bicyclists.".format(popular_start_station, most_starts), '\n')
   
    
    # TO DO: display most commonly used end station
    end_stations_count_dict = {}
        
    #popular_end_station = df["End Station"]
    end_stations_list = list(df["End Station"])
        
    for end_station in end_stations_list:
        if end_station not in end_stations_count_dict:
            end_stations_count_dict[end_station] = 1
        else:
            end_stations_count_dict[end_station] += 1
    
    most_finishes = max(end_stations_count_dict.values())
    
    popular_end_station = [end_station for key, value in end_stations_count_dict.items() if value == most_finishes]
    
    #print(popular_end_station)
    print("The most popular end station is {} where riders finished their rides {} times.".format(popular_end_station, most_finishes),'\n')


    # TO DO: display most frequent combination of "start to end" trip
    start_end_combo_count_dict = {}
    
    start_end_combo_list = list(df["Start Station"] + " to " + df["End Station"])
    
    for start_end_trip in start_end_combo_list:
        if start_end_trip not in start_end_combo_count_dict:
            start_end_combo_count_dict[start_end_trip] = 1
        else:
            start_end_combo_count_dict[start_end_trip] += 1
    
    most_trips = max(start_end_combo_count_dict.values())
    
    popular_trip = [start_end_trip for key, value in start_end_combo_count_dict.items() if value == most_trips]
    
    #print(start_end_combo)
    print("The most popular 'start to end' trip is {} which was taken by riders {} times.".format(popular_trip, most_trips), '\n')
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_time = df["Trip Duration"].sum()
    total_hours = int((trip_time / 60))
    total_minutes = (trip_time % 60)
     
    print("The total travel time is {} hours and {} minutes.".format(total_hours, total_minutes))  
      
    # TO DO: display mean travel time
    total_mean = df["Trip Duration"].mean()
    hours_mean = total_mean / 60
    minutes_mean = total_mean % 60
    print("The mean travel time is {} hours and {} minutes.".format(hours_mean, minutes_mean))
    

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    # If the User Stat columns: User Type, Gender, and Birth Year are not in
    # selected file, the columns will be skipped and a message will appear
    # explaining that we do not have any current data for that field. 

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    if "User Type" in df.columns:
        user_type = df["User Type"].value_counts()
        print("Users Type Detail:\n ", user_type)
        print()
    else:
        print("Currently, there is no USER TYPE data available for your selected city.")
        print()
    
    # TO DO: Display counts of gender
    if "Gender" in df.columns:
        gender_type = df["Gender"].value_counts()
        print("Gender Detail:\n ", gender_type)
        print()
    else:
        print("Currently, there is no GENDER data available for your selected city.")
        print()
        
    # TO DO: Display earliest, most recent, and most common year of birth
    if "Birth Year" in df.columns:
        min_birth_year = df["Birth Year"].min()
        print("The earliest birth year is: ", min_birth_year)
        print()
        max_birth_year = df["Birth Year"].max()
        print("The most recent birth year is: ", max_birth_year)
        print()
        common_birth_year = df["Birth Year"].mode()
        print("The most common birth year is: ", common_birth_year)
        print()
    else:
        print("Currently, there is no BIRTH YEAR data available for your selected city.")
        print()   
           
           
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    print()
    

def raw_data(df):
    answer_list = ["yes", "y"]
    while True:
        answer = input("Would you like to review the first 5 and last 5 lines of raw data for your selected city (type 'yes' or 'no'): ")
        if answer in answer_list:
            print()
            print("Here are the first 5 lines of raw data for your selected city.")
            print(df.head(5))
            print()
            print("Here are the last 5 lines of raw data for your selected city.")
            print(df.tail(5))
            print()
            idx = 5
            while True:
                more_raw_more = input("Would like to see more raw data? ")
                if more_raw_more in answer_list:
                    print(df.iloc[idx:idx+5])
                    idx += 5
                else:
                    break
            break
        else:
            break
    return (df)               

         
def main():
    while True:        
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no: ')
        if restart.lower() != 'yes':
            break
    
if __name__ == "__main__":
	main()
