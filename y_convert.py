import pickle
import numpy as np

filename = "y.pickle"

print("\nLoading y . . .")
y = pickle.load(open(f"Data\{filename}", "rb"))

print(f"Loaded {filename} successfully!")
print("Type of loaded data", type(y))

if type(y) == list:
	print("y is detected to be a list!", end=" ")
	print("Casting y as an array...")
	y = np.array(y)
	
	print("Saving y as an array:")
	with open("Data\y.pickle", 'wb') as pickle_out:
		pickle.dump(y, pickle_out)
else:
	print("y is already an np.array! No need to convert.")


input("Press enter key to exit . . .")