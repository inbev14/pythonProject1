# import validate
# import marshmallow


class Person:
    MIN_AGE = 18
    MAX_AGE = 60
    MIN_WEIGHT = 45
    MAX_WEIGHT = 140
    
    @classmethod
    def validate_age(cls, age):
        return cls.MIN_AGE <= age <= cls.MAX_AGE
    
    @classmethod
    def validate_passport(cls, passport: str):
        if '-' in passport:
            split_pas = passport.split('-')
            if not split_pas[0].isalpha() or len(split_pas[0]) != 2:
                return False
            elif split_pas[1].isnumeric() or len(split_pas[1]) != 6:
                return False
        return False
    
    def __init__(self, full_name: str, age: int, passport: str, weight: int | float):
        if isinstance(full_name, str):
            self.__full_name = full_name
        if self.validate_age(age):
            self.__age = age
        self.__passport = passport
        self.__weight = weight
    
    @classmethod
    def validate_full_name(cls, __full_name):
        return cls.__full_name


if __name__ == '__main__':
    person1 = Person('Vad man', 3, 'BP-134212', 80)
