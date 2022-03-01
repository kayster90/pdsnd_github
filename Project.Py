import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print('Which city would you like to see data for? Chicago, New York or Washington?')
    city = input()
    city = city.lower()
    while city not in ('chicago', 'new york', 'washington'):
           print('Invalid choice. Which city would you like to see data for? Chicago, New York or Washington?')
           city = input()
           city = city.lower()
        
            
    # TO DO: get user input for month (all, january, february, ... , june)
    print('Which month would you like to filter by? (January, February, March, April, May, June or All')
    month = input()
    month = month.lower()
    while month not in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
        print('Invalid Choice. Which month would you like to filter by? (January, February, March, April, May, June or All')
        month = input()
        month = month.lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('Which day would you like to filter by? (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All')
    day = input()
    day = day.lower()
    while day not in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
        print('Invalid Choice. Which day would you like to filter by? (Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or All')
        day = input()
        day = day.lower()

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
    print('Loading...')
    df = pd.read_csv(CITY_DATA[city])

    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # filter by month 
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]
    
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
        
    return df



def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    common_month = df['month'].mode()[0]
    print('Most common month is: ', common_month)

    # TO DO: display the most common day of week
    common_day = df['day_of_week'].mode()[0]
    print('Most common day is: ', common_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    
    common_hour = df['hour'].mode()[0]
    print('Most common start time is: ', common_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    common_startstation = df['Start Station'].mode()[0]
    print('Most common start station is: ', common_startstation)
          
    # TO DO: display most commonly used end station
    common_endstation = df['End Station'].mode()[0]
    print('Most common end station is: ', common_endstation)

    # TO DO: display most frequent combination of start station and end station trip
    df['Common Combo'] = df['Start Station'] + " to " + df['End Station']
    common_combo = df['Common Combo'].mode()[0]
          
    print('Most common combo is: ', common_combo)   

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    minute, second = divmod(total_travel_time, 60)
    hour, minute = divmod(minute, 60)
    
    print('The total travel time is ' + str(hour) + ' hours, ' + str(minute) + ' minutes, ' + str(second) + ' seconds.')  

    # TO DO: display mean travel time
    mean_time = round(df['Trip Duration'].mean())
    mins, sec = divmod(mean_time, 60)
    
    if mins > 60:
            hrs, mins = divmod(mins, 60)
            print('The average trip duration is ' + str(hrs) + ' hours, ' + str(mins) + ' minutes, ' + str(sec) + ' seconds.')  
    else:
            print('The average trip duration is ' + str(mins) + ' minutes, ' + str(sec) + ' seconds.')  

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('The types of user are:\n', user_types)

    # TO DO: Display counts of gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print('The types of users by gender are:\n', gender_count)

        # TO DO: Display earliest, most recent, and most common year of birth
        earliest= int(df['Birth Year'].min())
        print("\nThe oldest user is born in ",earliest)
        most_recent= int(df['Birth Year'].max())
        print("The youngest user is born in ",most_recent)
        common= int(df['Birth Year'].mode()[0])
        print("Most common year of birth is ",common)

    else:
        print('Gender stats cannot be calculated because Gender does not appear in the dataframe')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()