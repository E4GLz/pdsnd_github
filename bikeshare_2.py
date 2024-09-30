import time
import pandas as pd
# this dictionary contains the csv files for the cities
CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}


def get_filters():
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        city = input(
            'Please Select the listed cities (chicago, new york city, washington)\n')
        if city.lower() in ['chicago', 'new york city', 'washington']:
            break
        else:
            print('incorrect city name')
    # get user input for month (all, january, february, ... , june)
    while True:
        month = input(
            'Please enter the month (january, february, march, april, may, june) or enter "all" for all months ) \n')
        if month.lower() in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print('Incorrect month name')
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Please Select the day or type "all" for all week\n')
        if day.lower() in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print('Invalid day name')
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

    # Read data from csv file based on city
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Create new columns for month and day
    df['month'] = df['Start Time'].dt.month
    df['day'] = df['Start Time'].dt.day_name()

    # Filter by month
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june',
                  'july', 'august', 'september', 'october', 'november', 'december']
        month = months.index(month.lower()) + 1
        df = df[df['month'] == month]

    # Filter by day
    if day != 'all':
        df = df[df['day'] == day.title()]

    return df


def time_stats(df):
    print('\n Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    df['month'] = df['Start Time'].dt.month_name()
    print('the most common month for travel is: ', df['month'].mode()[0])

    # display the most common day of week
    df['day'] = df['Start Time'].dt.day_name()
    print('the most common day of week for travel is: ', df['day'].mode()[0])

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    print('the most common start hour for is: ', df['hour'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print('\n most commonly used start station is: ',
          df['Start Station'].mode()[0])

    # display most commonly used end station
    print('\n most commonly used end station is: ',
          df['End Station'].mode()[0])

    # display most frequent combination of start station and end station trip
    df['Start End'] = df['Start Station'] + ' to ' + df['End Station']
    print('\n most frequent combination of start station and end station trip is: ',
          df['Start End'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    df['Trip Duration'].sum()
    print('\n Total travel time', df['Trip Duration'].sum())

    # display mean travel time
    df['Trip Duration'].mean()
    print('\n Average travel time: ', df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    df['User Type'].value_counts()
    print('\n Display counts of user types', df['User Type'].value_counts())

    # Display counts of gender
    # Validate if the column exists
    if 'Gender' in df.columns:
        df['Gender'].value_counts()
        print('\n Display counts of gender', df['Gender'].value_counts())
    else:
        print('No Gender data available')

    # Display earliest, most recent, and most common year of birth
    # Validate if the column exists
    if 'Birth Year' in df.columns:
        df['Birth Year'].value_counts()
        print('\n earliest year of birth is: ', df['Birth Year'].min())
        print('\n most recent year of birth is: ', df['Birth Year'].max())
        print('\n most common year of birth is: ', df['Birth Year'].mode()[0])
    else:
        print('No Birth Year data available')

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

        # Display 5 rows of data
        row = 0
        while True:
            display = input('\nWould you like to view individual trip data? Enter "yes" or "no".\n')
            # validate the input
            if display.lower() != 'yes' and display.lower() != 'no':
                print('Invalid input')
                continue
            if display.lower() == 'yes':
                print(df.iloc[row: row + 5])
                row += 5
            else:
                break

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break   


if __name__ == "__main__":
    main()
