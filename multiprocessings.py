from multiprocessing import Pool

def square(x):
    return x * x
numbers = [1, 2, 3, 4, 5]
if __name__ == '__main__':
    with Pool(processes=4) as pool:
        results = pool.map(square, numbers)
    print(results)