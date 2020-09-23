from skimage.measure import compare_ssim as ssim
import matplotlib.pyplot as plt
from skimage.transform import resize
import cv2

print ('hello')

def img_compare(imageA, imageB, title):
	s = ssim(imageA, imageB,  multichannel=True)

	fig = plt.figure(title)
	plt.suptitle("SSIM %.2f" %(s))

	a = fig.add_subplot(1,2,1)
	plt.imshow(imageA, cmap=plt.cm.gray)

	a = fig.add_subplot(1,2,2)
	plt.imshow(imageB, cmap=plt.cm.gray)

	plt.show()

original = cv2.imread("original.jpg")
edited = cv2.imread("edited.jpg")

original = cv2.cvtColor(original, cv2.COLOR_BGR2HSV)
edited = cv2.cvtColor(edited, cv2.COLOR_BGR2RGB)

value = 50
h, s, v = cv2.split(edited)
lim = 255 - value
v[v > lim] = 255
v[v <= lim] += value

final_hsv = cv2.merge((h, s, v))
img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

fig = plt.figure("Images")
images = ("Original", original), ("Edited", edited)

for (i, (name, image)) in enumerate(images):
	a = fig.add_subplot(1,2,i+1)
	a.set_title(name)
	plt.imshow(image, cmap=plt.cm.gray)
plt.show()
#img_compare(original, original, "Результат сравнения Оригнала с Оригиналом ")
img_compare(original, edited, "Результат сравнения Оригинала и Редактированной копии ")
img_compare(edited, img, "Результат сравнения Оригинала и Редактированной копии ")