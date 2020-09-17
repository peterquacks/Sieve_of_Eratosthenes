#! /usr/bin/env python3

class Prime:
	def __init__(self, bound, alist):
		self.bound     = bound
		self.alist     = []
		self.primeList = []

	def eratosthenes(self, bound, alist):
		primeDict = dict((i,j) for i,j in enumerate(alist))
		primeDict[0] = False


		for idx in range(2,self.bound):
			if primeDict[idx] != False:
				count = 2
				# Takes every multiple in the dictionary and sets it to false
				while (idx * count) <= self.bound:
					primeDict[idx * count] = False
					count = count + 1

		# Sets the primeList so that it takes 
		self.primeList = [keys for keys, value in primeDict.items() if value is True]
		return self.primeList



def main():
	my_bound = input("Please enter your upper bound: ")
	my_bound = int(my_bound)
	alist    = [True] * (my_bound + 1)
	eg1      = Prime(my_bound, alist)
	eg1.eratosthenes(my_bound, alist)
	print(eg1.primeList)


if __name__ == "__main__":
    main()



