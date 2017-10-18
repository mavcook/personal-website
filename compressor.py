# Compress, scale, and create thumbnails for images
# Note: made very quickly, not supposed to be well writen and comprehensive
import subprocess as sp
import sys
import os
import shutil
from PIL import Image
import argparse



EXCLUDE_EXTS = ['.mp4', '.mov']
EXCLUDE_PATTERN = '_compressed'
MAX_WIDTH = 2500
MAX_HEIGHT = 2500
MAX_THUMB = (600,600)
THUMB_ASPECT_RATIO = 16/9
THUMB_QUALITY = 75



def getFiles(dirr):
	files = [f for f in os.listdir(dirr) if os.path.isfile(os.path.join(dirr, f))]
	files.sort()
	files = [f for f in files if EXCLUDE_PATTERN not in f]
	files = [f for f in files if os.path.splitext(f)[1].lower() not in EXCLUDE_EXTS]
	print('\nCompressing Input Files: ', files)
	files = [os.path.join(dirr, f) for f in files]

	return files


# thanks to https://stackoverflow.com/a/43738947 cause im being lazy
def crop_to_aspect(img, aspect, divisor=1, alignx=0.5, aligny=0.5):
	"""Crops an image to a given aspect ratio.
	Args:
		aspect (float): The desired aspect ratio.
		divisor (float): Optional divisor. Allows passing in (w, h) pair as the first two arguments.
		alignx (float): Horizontal crop alignment from 0 (left) to 1 (right)
		aligny (float): Vertical crop alignment from 0 (left) to 1 (right)
	Returns:
		Image: The cropped Image object.
	"""
	if img.width / img.height > aspect / divisor:
		newwidth = int(img.height * (aspect / divisor))
		newheight = img.height
	else:
		newwidth = img.width
		newheight = int(img.width / (aspect / divisor))
	img = img.crop((alignx * (img.width - newwidth),
						aligny * (img.height - newheight),
						alignx * (img.width - newwidth) + newwidth,
						aligny * (img.height - newheight) + newheight))
	return img



def createThumbnail(img, filename, size, quality, outDir):
	
	thumb = crop_to_aspect(img, THUMB_ASPECT_RATIO)
	thumb.thumbnail(size, Image.ANTIALIAS)
	dimStr = 'x'.join([str(i) for i in thumb.size])
	outName = [filename, dimStr, 'q' + str(quality)]
	savePath = os.path.join(outDir, '_'.join(outName) + '.jpg')
	thumb.save(savePath, 'JPEG', optimize=True, quality=quality)



def compressImg(img, filename, quality, outDir):

	w,h = img.size
	sf = w / h
	if w > MAX_WIDTH:
		w = MAX_WIDTH
		h = w * (1/sf)
	if h > MAX_HEIGHT:
		h = MAX_HEIGHT
		w = h * sf
	w = int(w)
	h = int(h)
	img = img.resize((w,h), Image.ANTIALIAS)
	savePath = os.path.join(outDir, filename + EXCLUDE_PATTERN + str(quality) + '.jpg')
	img.save(savePath,"JPEG",optimize=True, quality=quality) 




def main(inDir, outDir, quality):
	outDir = os.path.join(inDir, 'compressed')
	outThumbDir = os.path.join(outDir, 'thumb')

	if os.path.exists(outDir) == False:
		os.makedirs(outDir)
		print("Created directory: ", outDir)
	if os.path.exists(outThumbDir) == False:
		os.makedirs(outThumbDir)
		print("Created directory: ", outThumbDir)

	files = getFiles(inDir)

	for f in files:
		img = Image.open(f)
		fname = os.path.basename(f)
		fname = os.path.splitext(fname)[0]

		createThumbnail(img, fname, MAX_THUMB, THUMB_QUALITY, outThumbDir)
		compressImg(img, fname, quality, outDir)



if __name__ == "__main__":
	argv=sys.argv[1:]

	# Quick command line arguments
	parser = argparse.ArgumentParser(description='Quick img compressor and thumbnailer')
	parser.add_argument('-d', type=str, required=True, help='Input directory. All files in directory will be compressed. Takes priority over -f')
	parser.add_argument('-o', '--output', type=str,
						help='Output directory. A directory will be created called compressed, along with the subfolder thumbs. If not specified, does this in the input directory.')
	parser.add_argument('-q', '--quality', default=85, type=int, help='Quality of compression, 1-100')
	args = parser.parse_args(argv)

	q = args.quality
	inDir = args.d
	outDir = inDir

	if args.output:
		outDir = args.output

	main(inDir, outDir, q)