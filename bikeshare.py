import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
days = ['all', 'sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    for key in CITY_DATA:
        cities = CITY_DATA.keys()
    
    
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
       city = input('city ')
       city = city.lower()
       if city in cities:
           break

    # get user input for month (all, january, february, ... , june)
    while True:
       month = input('month ')
       month = month.lower()
       if month in months:
           break


    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
       day = input('day ')
       day = day.lower()
       if day in days:
           break

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
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['weekday'] = df['Start Time'].dt.weekday_name
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        month = month.index(month)+1
        df = df[df['month'] == month]
    if day != 'all':
        df = df[df['weekday'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    common_month = df['month'].value_counts()
    most_common_month = common_month.idxmax()
    print("most common month: ", months[most_common_month])

    # display the most common day of week
    common_day = df['weekday'].value_counts()
    most_common_day = common_day.idxmax()
    print("most common day of week: ", most_common_day)

    # display the most common start hour
    common_start_hour = df['hour'].value_counts()
    most_common_start_hour = common_start_hour.idxmax()
    print("most common hour of day: ", most_common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_used_start_station = df['Start Station'].value_counts()
    most_common_used_start_station = common_used_start_station.idxmax()
    print("Most common start Station:",most_common_used_start_station)

    # display most commonly used end station
    common_used_end_station = df['End Station'].value_counts()
    most_common_used_end_station = common_used_end_station.idxmax()
    print("Most common end Station: ", most_common_used_end_station)

    # display most frequent combination of start station and end station trip
    most_frequent_combination_of_start_station_and_end_station_trip = df[['Start Station', 'End Station']].mode().loc[0]
    print("Most common trip from start to end (i.e., most frequent combination of start station and end station) : ", most_frequent_combination_of_start_station_and_end_station_trip[0], most_frequent_combination_of_start_station_and_end_station_trip[1])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    totaltraveltime = df['Trip Duration'].sum()
    d = totaltraveltime // (24 * 3600)
    totaltraveltime = totaltraveltime % (24 * 3600)
    h = totaltraveltime // 3600
    totaltraveltime %= 3600
    m = totaltraveltime // 60
    totaltraveltime %= 60
    s = totaltraveltime
    print("total travel time: ",d,"days", h, "hours",
          m, "minutes",
          s, "seconds")

    #print("total travel time: ",totaltraveltime)
    #print("total travel time: ",total_travel_time)
    
    # display mean travel time
    meantraveltime = df['Trip Duration'].mean()
    mean_travel_time = time.strftime("%M minutes %S seconds", time.gmtime(meantraveltime))
    print("average travel time: ", mean_travel_time )
 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    

def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print("counts of each user type: \n",df['User Type'].value_counts())

    # Display counts of gender
    col = df.columns
    if 'Gender' in col :
        print("counts of each gender: \n",df['Gender'].value_counts())

    print("year of birth: \n")

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in col:
        bry = df['Birth Year']
        earliest = bry.min()
        print("Earliest year of birth: ",int (earliest))
        
        most_recent = bry.max()
        print("most recent year of birth: ",int (most_recent))
        
        common_year = bry.value_counts()
        most_common_year = common_year.idxmax()
        print("most common year of birth: ",int(most_common_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """ print 5 rows of the data at a time as requirment """
    i = 0
    raw = input(" Do you print 5 rows of the data ?").lower()
    # TO DO: convert the user input to lower case using lower() function
    pd.set_option('display.max_columns',200)

    while True:            
        if raw == 'no':
            break
        elif raw == 'yes':
            print(df.iloc[i: i + 5]) 
            # TO DO: appropriately subset/slice your dataframe to display next five rows
            raw = input("<your input message here>").lower()
            # TO DO: convert the user input to lower case using lower() function
            i += 5
        else:
            raw = input("\nYour input is invalid. Please enter only 'yes' or 'no'\n").lower()
            
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
