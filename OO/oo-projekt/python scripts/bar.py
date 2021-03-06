from sklearn.cluster import KMeans
import matplotlib.pyplot as plt 
import numpy as np
import cv2

def centroid_histogram(clt):

	numLabels = np.arange(0, len(np.unique(clt.labels_)) +1)
	(hist,_) = np.histogram(clt.labels_, bins=numLabels)

	hist = hist.astype("float")
	hist /= hist.sum()

	return hist

def plot_colors(hist, centroids):
	bar = np.zeros((50, 300, 3), dtype="uint8")
	startX = 0

	for (percent, color) in zip(hist, centroids):

		endX = startX + (percent * 300)
		cv2.rectangle(bar, (int(startX),0), (int(endX), 50), color.astype("uint8").tolist(), -1)
		startX = endX

	return bar


image_source = cv2.imread("001L_1.png")
image_source = cv2.cvtColor(image_source, cv2.COLOR_BGR2RGB)

image = image_source.reshape((image_source.shape[0]* image_source.shape[1],3))

k = 1 #stevilo skupin barv
iterations = 4 
iteration = 50 

clt = KMeans(n_clusters = k, n_jobs = iterations, max_iter = iteration) 
clt.fit(image)

hist = centroid_histogram(clt)
bar = plot_colors(hist, clt.cluster_centers_)

###
fig = plt.figure()
ax = fig.add_subplot(211)
ax.imshow(image_source)
ax = fig.add_subplot(212)
ax.imshow(bar)
plt.show() 

cv2.waitKey(0)
"""plt.figure()
plt.axis("off")
plt.imshow(image)
plt.show()"""
