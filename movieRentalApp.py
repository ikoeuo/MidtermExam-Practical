import movieStore

def run(self):
    store1 = movieStore('Toronto film store', 120, 75, 9.50, 2.50)
    print(f'Store Name: {store1.getStoreName()} All Movies: {store1.getAllMovies()} Movies Available: {store1.getAvailMovies()} Rent Fee: {store1.getRentFee()} Late Fee: {store1.getLateFee()}')

    