import cv2
import numpy as np 


if __name__ == '__main__':
	image = cv2.imread("compare1.png")
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	print type(image)
	
	try:
		(cnts, _) = cv2.findContours(gray.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	except:
		(_, cnts, _) = cv2.findContours(gray.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

	cnts_rect = []
	for i in range(501,520):
		imageName = "capture" + str(i) + ".png"
		image = cv2.imread(imageName)
		gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
		(cnts, _) = cv2.findContours(gray.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
		x = 0
		y = 0
		i = 0

		for c in cnts:
			# approximate the contour
			peri = cv2.arcLength(c, True)
			#This function gives the number of vertices of the figure
			#For example, approx returns 4 if the shape is rectangle and 5 if the shape is pentagon
			# k is constant, it can be changing from 0.005 to 0.1
			# k = 0.005
			k = 0.005
			approx = cv2.approxPolyDP(c, k * peri, True)
			# if our approximated contour has four points, then
			# we can assume that we have found our screen

			if len(approx) >= 4 and cv2.contourArea(c) < 200 and cv2.contourArea(c)>150:
				cnts_rect.append(approx)
				print cv2.contourArea(c)
				for points in (approx):
					for point in  points:
						x += point[0]
						y += point[1]
						i += 1
				# print "this is coutour area ", cv2.contourArea(c)
		print "this is x, y: ", x/i, y/i

	cv2.drawContours(image, cnts_rect, -1, (0, 255, 0), 3)
	print len(cnts_rect)


	cv2.imshow("test", image)
	# cv2.imwrite("test.png", image)
	cv2.waitKey(10000)
	# print cnts

















