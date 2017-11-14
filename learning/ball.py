# this is a ball class, we try to record some data about the ball such as direction 
# and velocity. We have these data, we can predict the path of the ball. So we can reduce
# the time to find the position of ball.

# BUT this class does not finish, we will continue to finish it in the future.


import cv2
import numpy as np 

class Ball(object):
	"""docstring for Ball"""
	def __init__(self):
		self.path = []
		self.x_ = 0
		self.y_ = 0
		self.x_vec = 0
		self.y_vec = 0
		self.area = 0
		self.direction = 'left'
		self.firstAppear = True
		self.centre = []


		# self.find_centre(mask)



	def find_centre(self,mask):
		image = mask

		# I can not draw the on the mask image, So I open a new image, and draw the 
		# counter on that image. This image is larger than mask, only 1/4 of area in 
		# image2 is valid area to show the counter appear in mask.
		image2 = cv2.imread("capture508.png")

		# gray = cv2.cvtColor(mask, cv2.COLOR_BGR2GRAY)
		
		try:
			(cnts, _) = cv2.findContours(image.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		except:
			(_, cnts, _) = cv2.findContours(image.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

		cnts_rect = []
		# for i in range(501,520):
		# 	imageName = "capture" + str(i) + ".png"
		# 	image = cv2.imread(imageName)
		# 	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		# 	(cnts, _) = cv2.findContours(gray.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

		temp = []

		for c in cnts:
			x = 0
			y = 0
			i = 0

			# approximate the contour
			peri = cv2.arcLength(c, True)
			#This function gives the number of vertices of the figure
			#For example, approx returns 4 if the shape is rectangle and 5 if the shape is pentagon
			# k is constant, it can be changing from 0.005 to 0.1
			# k = 0.005
			k = 0.005
			approx = cv2.approxPolyDP(c, k * peri, True)
			# if our approximated contour has more than four points, then
			# we can assume that we may find counter.
			if len(approx) >= 4 and cv2.contourArea(c) < 300 and cv2.contourArea(c)>30:
				# print cv2.contourArea(c)
				# for points in (approx):
				# 	for point in  points:
				# 		# if self.firstAppear:
				# 			# if (point[0] > 0 and point[0]<50)  :
				# 			# 	self.direction = right
				# 			# elif point[0]<580 and point[0] > 530:
				# 			# 	self.direction = left
				# 		x += point[0]
				# 		y += point[1]
				# 		i += 1
				cnts_rect.append(approx)

					# print "this is coutour area ", cv2.contourArea(c)
			try:
				# print "this is x, y: ", x/i, y/i
				# temp.append((x/i, y/i))


				cv2.drawContours(image2, cnts_rect, -1, (0, 255, 0), 3)
				cv2.imshow("iamge2", image2)
				# cv2.imwrite("test2.png", image2)
				cv2.waitKey(1)

			except:
				pass
		self.centre.append(temp)


		