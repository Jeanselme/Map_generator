from PIL import Image, ImageFilter
from random import randint

def computeDiamondSquare(n) :
	"""
		Returns a square image of dimension 2**n + 1
		And computes the diamond and square algorithm on it
	"""
	# Creation of the result image
	l = 2 ** n
	img = Image.new( 'L', (l+1,l+1), "black")
	pixels = img.load()

	# Initialization of the corners
	pixels[0,0] = randint(-l,l)
	pixels[0,l] = randint(-l,l)
	pixels[l,l] = randint(-l,l)
	pixels[l,0] = randint(-l,l)

	i = l
	while i > 1 :
		id = i // 2
		# Diamond
		for x in range(id, l, i) :
			for y in range(id, l, i) :
				# Average and a random value
				pixels[x,y] = ((pixels[x-id,y-id] + pixels[x-id,y+id]+ pixels[x+id,y+id] + pixels[x+id,y-id]) // 4 + randint(-id,id))
		# Square
		for x in range(0, l, id) :
			d = 0
			if (x % i == 0) :
				d = id
			for y in range(d, l, i) :
				s = 0
				n = 0
				if (x >= id) :
					s += pixels[x-id,y]
					n += 1
				if (x+id <= l) :
					s += pixels[x+id,y]
					n += 1
				if (y >= id) :
					s += pixels[x,y-id]
					n += 1
				if (y+id <= l) :
					s += pixels[x,y+id]
					n += 1

				# Average of the pixels around (if they exist)
				pixels[x,y] = (s // n + randint(-d,d))
		i = id
	return img

def fromLToRGB(origin) :
	"""
		Create a colored map corresponding to the grayscale image origin
		This function could be improved with a more linear way of changing value
	"""
	map = Image.new( 'RGB', (origin.size[0],origin.size[1]), "black")
	pixels_map = map.load()
	pixels_ori = origin.load()
	for i in range(map.size[0]) :
		for j in range(map.size[1]) :
			if (pixels_ori[i,j] > 200) :
				pixels_map[i,j] = (int(pixels_ori[i,j]),int(pixels_ori[i,j]),int(pixels_ori[i,j]))
			elif (pixels_ori[i,j] > 180) :
				pixels_map[i,j] = (int(0.9*pixels_ori[i,j]),int(0.9*pixels_ori[i,j]),int(0.9*pixels_ori[i,j]))
			elif (pixels_ori[i,j] > 160) :
				pixels_map[i,j] = (int(0.75*pixels_ori[i,j]),int(0.75*pixels_ori[i,j]),int(0.75*pixels_ori[i,j]))
			elif (pixels_ori[i,j] > 140) :
				pixels_map[i,j] = (int(0.5*pixels_ori[i,j]),int(pixels_ori[i,j]),int(0.1*pixels_ori[i,j]))			
			elif (pixels_ori[i,j] > 120) :
				pixels_map[i,j] = (int(0.5*pixels_ori[i,j]),int(pixels_ori[i,j]),int(0.1*pixels_ori[i,j]))
			elif (pixels_ori[i,j] > 100) :
				pixels_map[i,j] = (int(0.9*pixels_ori[i,j]),int(0.9*pixels_ori[i,j]),int(0.1*pixels_ori[i,j]))
			else :
				pixels_map[i,j] = (int(0.2*pixels_ori[i,j]),int(0.2*pixels_ori[i,j]),max(int(1.5*pixels_ori[i,j]),100))
	return map.filter(ImageFilter.SMOOTH_MORE)

n = 10
img = computeDiamondSquare(n)
img.save("diamond_square.png")

map = fromLToRGB(img)
map.save("map.png")