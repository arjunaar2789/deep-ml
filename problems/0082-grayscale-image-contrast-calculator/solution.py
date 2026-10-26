import numpy as np

def calculate_contrast(img) -> int:
	"""
	Calculate the contrast of a grayscale image.
	Args:
		img (numpy.ndarray): 2D array representing a grayscale image with pixel values between 0 and 255.
	"""
	minm,maxm=float('inf'),float('-inf')
	for i in range(len(img)):
		minm,maxm=min(min(img[i]),minm),max(max(img[i]),maxm)
	return maxm-minm