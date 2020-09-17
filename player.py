class Player:
    def __init__(self, first_name, last_name, full_name, country, dob, died):
        self.first_name = first_name
        self.last_name = last_name
        self.full_name = full_name
        self.country = country
        self.date_of_birth = dob
        self.died = died

    def __lt__(self, other):
        # less than operators
        me = (self.last_name, self.first_name, self.country,
              self.date_of_birth)
        them = (other.last_name, other.first_name, other.country,
                other.date_of_birth)
        return me < them

    def __ge__(self, other):
        # greater-than-or-equal is the inverse of less-than
        return not self.__lt__(other)

    def __gt__(self, other):
        # greater than operators
        me = (self.last_name, self.first_name, self.country,
              self.date_of_birth)
        them = (other.last_name, other.first_name, other.country,
                other.date_of_birth)
        return me > them

    def __le__(self, other):
        # if its not less than or equal
        return not self.__gt__(other)

    def __eq__(self, other):
        # equal operators
        me = (self.last_name, self.first_name, self.country,
              self.date_of_birth)
        them = (other.last_name, other.first_name, other.country,
                other.date_of_birth)
        return me == them

    def __str__(self):
        return f'Full Name: {self.full_name} \n ' \
               f'Last Name: {self.last_name} \n ' \
               f'First Name: {self.first_name} \n ' \
               f'Countries: ( {self.country} ) \n ' \
               f'Date of Birth: {self.date_of_birth} \n ' \
               f'Died: {self.died}'

    def __ne__(self, other):
        # not equal
        return not self.__eq__(other)