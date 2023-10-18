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
    
    def rentMovies(self):
        rentedMovies = input('how many movies would you like to rent?')
        if rentedMovies > self.__availMovies:
            print('Not enough movies to rent')
        if rentedMovies <= 0:
            print('You must rent at least 1 movie')
        else:
            self.__availMovies = self.__availMovies - rentedMovies
            self.__rentFee = self.__rentFee * rentedMovies
            self.__availMovies = self.__availMovies - rentedMovies
            print(f'Your total rent fee is: {self.__rentFee}')

    def calculateLateFee():
        returnedMovies = input('How many movies are you returning? ')
        lateMovies = input('How many movies are overdue? ')
        self.__lateFee = lateMovies * self.__lateFee
        self.__availMovies = self.__availMovies + returnedMovies
        print(f'Your total late fee is {self.__lateFee}')


