# import the needed modules
import time
import pandas as pd
import numpy as np
from IPython.display import display

# Load the data into a  dictionary and assign it to a variable
CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ['chicago','new york city', 'washington']
    while city not in ['chicago','new york city', 'washington']:
        city = input('What is the name of the city?').lower()
        if city in ['chicago','new york city', 'washington']:
            print('Hello! Let\'s explore some {} data'.format(city).title())

    # TO DO: get user input for month (all, january, february, ... , june)
    month = ['all', 'january', 'february', 'march', 'april', 'may', 'june']
    while month not in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
        month = input('what is the name of the month?').lower()
        if month in ['all', 'january','february', 'march', 'april', 'may', 'june']:
            print('Hello Let\'s explore the data for the month: {}'.format(month).title())

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day = ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    while day not in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
        day = input('What is day of the week is it?').lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            print('Hello! Let\'s explore the data for:{}'.format(day).title())

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
    # read the data 
    df = pd.read_csv(CITY_DATA[city])
    
    # convert start time column to date time
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # extract month from converted column
    df['month'] = df['Start Time'].dt.month
    
    # extract weekday from the converted column
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    
    # extract hour from the column
    df['hour'] = df['Start Time'].dt.hour
    
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
        df  = df[df['day_of_week'] == day.title()]
    
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    most_common_month = df['month'].mode()[0]
    print('The most common month is: {}'.format(most_common_month))

    # TO DO: display the most common day of week
    most_common_day = df['day_of_week'].mode()[0]
    print('The most common day of the week is: {}'.format(most_common_day))

    # TO DO: display the most common start hour
    most_common_hour = df['hour'].mode()[0]
    print('The most common start hour of the day is: {}'.format(most_common_hour))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    start_stat = df['Start Station'].mode()[0]
    print('The most common used Start Station is: {}'.format(start_stat))

    # TO DO: display most commonly used end station
    end_stat = df['End Station'].mode()[0]
    print('The most used End Station is: {}'.format(end_stat))

    # TO DO: display most frequent combination of start station and end station trip
    df['Station Combo'] = df['Start Station'] + ' : ' + df['End Station']
    most_freq_comb = df['Station Combo'].mode()[0]
    print('The most frequent combination of Start station and End station trip is: {}'.format(most_freq_comb))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration in km...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_trav = df['Trip Duration'].sum()
    print('The total travel time is: {}'.format(total_trav))

    # TO DO: display mean travel time
    mean_time = df['Trip Duration'].mean()
    print('The average travel time is: {}'.format(mean_time))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_type = df['User Type'].value_counts()
    print('The total counts of users by type is:\n{}'.format(user_type))

    # TO DO: Display counts of gender
    for coln in df.columns:
        if coln == 'Gender':
            gender_total = df['Gender'][df['Gender'].notnull()]
            gender_total = df['Gender'].value_counts()
            print('The total count of gender is:\n{}'.format(gender_total))

    # TO DO: Display earliest, most recent, and most common year of birth
    for yr in df.columns:
        if yr == 'Birth Year':
            birth = df['Birth Year'][df['Birth Year'].notnull()]
            early_birth = int(df['Birth Year'].min())
            print('The earliest birth year is: {}'.format(early_birth))
    
            most_recent = int(df['Birth Year'].max())
            print('The most recent birth year is: {}'.format(most_recent))
    
            most_common = int(df['Birth Year'].mode()[0])
            print('The most common birth year is: {}'.format(most_common))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(df):
    ''' This code takes in user input and displays 5 rows of data until a condition is met'''
    
    view_data = input("Would you like to view 5 rows of individual trip data? Enter yes or no?").lower()
    #keep track of the count
    start_loc = 0
    #use a while loop to display data 
    while start_loc in range(0, len(df), 5):
        print(df.iloc[start_loc:start_loc+5])
        #increase the count until 5
        start_loc += 5
        #take user input either to continue or stop
        view_display = input("Do you wish to continue?: ").lower()
        #break out of the loop
        if view_display == 'no':
            break
        else:
            print('You have seen all the data in the table')

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
