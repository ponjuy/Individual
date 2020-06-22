class Date:
    """ A class that stores and manipulates dates,
        represented by a day, month, and year.
    """
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # The constructor for the Date class.
    def __init__(self, new_month, new_day, new_year):
        """ The constructor for objects of type Date. """
        self.month = new_month
        self.day = new_day
        self.year = new_year

    # The function for the Date class that returns a Date
    # object in a string representation.
    def __repr__(self):
        """ This method returns a string representation for the
            object of type Date that it is called on (named self).

            ** Note that this _can_ be called explicitly, but
              it more often is used implicitly via printing or evaluating.
        """
        s = '%02d/%02d/%04d' % (self.month, self.day, self.year)
        return s

    def is_leap_year(self):
        """ Returns True if the called object is
            in a leap year. Otherwise, returns False.
        """
        if self.year % 400 == 0:
            return True
        elif self.year % 100 == 0:
            return False
        elif self.year % 4 == 0:
            return True
        return False

    def copy(self):
        """ Returns a new object with the same month, day, year
            as the called object (self).
        """
        new_date = Date(self.month, self.day, self.year)
        return new_date

    def advance_one(self):
        """ that changes the called object so that it represents one calendar day after the date that it originally represented."""
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.is_leap_year() == True:
            days_in_month[2] = 29
            
        if self.day == 31 and self.month == 12:
            self.day = 1
            self.month = 1
            self.year += 1     
        elif self.day == days_in_month[self.month]:            
            self.day = 1
            self.month = self.month + 1 
        else:
            self.day += 1

    
    
    def advance_n(self, n):
        """ that changes the calling object so that it represents n calendar days after the date it originally represented. Additionally, the method should print all of the dates from the starting date to the finishing date, inclusive of both endpoints.
        """
        if n>=0:
            print(self)
            for i in range (0, n):
                self.advance_one()
                print (self)

    def __eq__(self, other):
        """ that returns True if the called object (self) and the argument (other) represent the same calendar date (i.e., if the have the same values for their day, month, and year attributes). Otherwise, this method should return False
        """
        return (self.day==other.day and self.month == other.month and self.year == other.year)

    def is_before(self, other):
        """ that returns True if the called object represents a calendar date that occurs before the calendar date that is represented by other. If self and other represent the same day, or if self occurs after other, the method should return False
        """
        if other.year != self.year:
            return self.year < other.year
        if other.month != self.month:
            return self.month < other.month
        return self.day < other.day
    
    def is_after(self, other):
        """ that returns True if the calling object represents a calendar date that occurs after the calendar date that is represented by other. If self and other represent the same day, or if self occurs before other, the method should return False.
        """
        if other.year != self.year:
            return self.year > other.year
        if other.month != self.month:
            return self.month > other.month
        return self.day > other.day
    
    def days_between(self, other):
        """ that returns an integer that represents the number of days between self and other.
        """
        d1 = self.copy()
        d2 = other.copy()
        count = 0
        
        if d1.is_before(d2) == True:
            while d1.is_before(d2) == True:
                count += 1
                d1.advance_one()
            count *= -1
            return count 
        elif d2.is_before(d1) == True:
            while d2.is_before(d1) == True:
                count += 1
                d2.advance_one()
            return count 
        elif d1 == d2:
            return 0


    def day_name(self):
        """that returns a string that indicates the name of the day of the week of the Date object that calls it. In other words, the method should return one of the following strings: 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'.
        """
        d1 = Date(4, 8, 2019)
        result = self.days_between(d1) % 7
        day_names = ['Monday', 'Tuesday', 'Wednesday', 
             'Thursday', 'Friday', 'Saturday', 'Sunday']
        
        return day_names[result]
    def get_age_on(birthday, other):
    """ that accepts two Date objects as parameters: one to represent a person’s birthday, and one to represent an arbitrary date. The function should then return the person’s age on that date as an integer."""
        d1 = birthday
        d2 = other
        diffy = d2.year - d1.year
        diffm = d2.month - d1.month
        diffd = d2.day - d1.day

        if diffm == 0 and diffd >0:
            return diffy
        if diffm<0:
            return diffy -1
        if diffm >0:
            return diffy
        if diffm == 0 and diffd <0:
            return diffy -1
        if diffm ==0 and diffd ==0:
            return diffy

    def print_birthdays(filename):
        """ that accepts a string filename as a parameter. The function should then open the file that corresponds to that filename, read through the file, and print some information derived from that file.
        """
        file = open(filename, 'r')
        for line in file:
            s = line.split(",")
            x = Date(int(s[1]), int(s[2]), int(s[3]))
            print(str(s[0]) + "(" + str(x) + ")" + "(" + str(x.day_name) + ")")
        file.close()
def nye_counts(start, end):

    d = {} # create an empty dictionary

    # add your code here
    for year in range (start, end+1):
        date = Date(12,31, year)
        day = date.day_name()
        if day in d.keys() : # if day is present in the dictionary, then increase the count by 1
            d[day] = d[day] + 1
        else: # else create a new record in dictionary
            d[day] = 1
    if 'Monday' not in d:
        d['Monday'] = 0
    if 'Tuesday' not in d:
        d['Tuesday'] = 0
    if 'Wednesday' not in d:
        d['Wednesday'] = 0
    if 'Thursday' not in d:
        d['Thursday'] = 0
    if 'Friday' not in d:
        d['Friday'] = 0
    if 'Saturday' not in d:
        d['Saturday'] = 0
    if 'Sunday' not in d:
        d['Sunday'] = 0

    return d      
