import random
####### Generate data to process
W, H = [100, 100] # Arbitrary Autoclave dimension
Autoclave_area = W*H
# Define dimensions of jobs to be completed
Dimensions = []
list = range(0,41) # number of jobs
for i in list: # Generate job geometries randomly, favourising a homogeneous distribution of large, average and small parts
	       # The ratios with the width and height of the autoclave dimensions were taken arbitrarily
    if i < 10:
        W1 = random.randrange(int(2/3*W), W)
        H1 = random.randrange(1, int(1/2*H))
        Dimensions.append([W1, H1])
    if 10 <= i <20:
        W1 = random.randrange(1, int(1/2*W))
        H1 = random.randrange(int(2/3*H), H)
        Dimensions.append([W1, H1])
    if 20 <= i <30:
        W1 = random.randrange(int(1/2*W), W)
        H1 = random.randrange(int(1/2*H), H)
        Dimensions.append([W1, H1])
    else:
        W1 = random.randrange(1, int(1/2*W))
        H1 = random.randrange(1, int(1/2*H))
        Dimensions.append([W1, H1])
random.shuffle(Dimensions) # Ensure 
Areas = [item[0]*item[1] for item in Dimensions]

####### Greedy algorithm
# Sort list in decreasing order then apply the algorithm
sorted_areas = sorted(Areas, reverse = True)
# Define bin class
class Bin:
	def __init__(self):
		self.list = []

	def addItem(self, item):
		self.list.append(item)

	def removeItem(self, item):
		self.list.remove(item)

	def sum(self):
		total = 0
		for elem in self.list:
			total += elem
		return total

	def show(self):
		return self.list

def greedy(areas, max_area): # Returns list of bins with input items inside
    list_bins = []; list_bins.append(Bin())  # Add first empty bin to list

    for item in areas:
        bin_found = False # Go through bins and try to allocate
        for bin in list_bins:
            if bin.sum() + item <= max_area:
                bin.addItem(item)
                bin_found = True; break
        # If item not allocated in bins in list, create new bin and allocate it to it.
        if bin_found == False:
            newBin = Bin(); newBin.addItem(item); list_bins.append(newBin)
    
    areas = []
    for bin in list_bins:
        areas.append(bin.show())# Turn bins into list of items and return
    return (areas)
print(greedy(sorted_areas, Autoclave_area))
