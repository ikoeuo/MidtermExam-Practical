class movieStore:
    def __init__(self,storeName, allMovies, availMovies,rentFee,lateFee):
        self.__storeName = storeName
        self.__allMovies = allMovies
        self.__availMovies = availMovies
        self.__rentFee = rentFee
        self.__lateFee =lateFee

    def getStoreName(self):
        return self.__storeName
    def getAllMovies(self):
        return self.__allMovies
    def getAvailMovies(self):
        return self.__availMovies
    def getRentFee(self):
        return self.__rentFee
    def getLateFee (self):
        return self.__lateFee
    
    def returnOrRent(self):
        answer = input('would you like to rent or return? ')
        if answer == 'rent':
            rentedMovies = input('how many movies would you like to rent?')
            if rentedMovies > self.__availMovies:
                print('Not enough movies to rent')
            if rentedMovies <= 0:
                print('You must rent at least 1 movie')
            else:
                self.__availMovies = self.__availMovies - rentedMovies
                self.__rentFee = self.__rentFee * rentedMovies
                print(f'Your total rent fee is: {self.__rentFee}')

        elif answer == 'return': 
            returnedMovies = input('How many movies are you returning? ')
            lateMovies = input('How many movies are overdue? ')
            self.__lateFee = lateMovies * self.__lateFee
            print(f'Your total late fee is {self.__lateFee}')

