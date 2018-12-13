# ASSIGNMENT NAME: HW 7
# NAME: Chance Cardona 
# EMAIL: ccardona@mymail.mines.edu 
# DATE: 11/19/18
# DESCRIPTION: Testing Fourier Transform functions.
# OTHER NOTES: First off I changed the imread we're using
# as the other was deprecated and not functional for me.
# it can be installed with pip.
# UPDATE: I got my matrix forms of the 2D dft to work!
# now using my own methods.
from imageio import imread
import numpy as np, matplotlib.pyplot as plt
import hw07


#img = imread("mines1.jpg")
img = imread("mines2.jpg")



print("Shape of the array is", np.shape(img))

# fig = plt.figure()
# plt.subplot(),
# plt.imshow(img, cmap = 'gray')
# plt.title('The original image')
# plt.show()


red = img[:,:,0]
green = img[:,:,1]
blue = img[:,:,2]

# print(img)
# print("NEXT \n",np.dstack((red, green, blue)))

fig = plt.figure()
plt.subplot(131)
plt.imshow(img, cmap = 'gray')
plt.title('Input Image')
plt.xticks([])
plt.yticks([])

#Creating the Fourier Image. I do the log10 so it appears better.
# Fred = np.fft.fft2(red)
# Fgreen = np.fft.fft2(green)
# Fblue = np.fft.fft2(blue)
Fred = hw07.Fdft2(red)
Fgreen = hw07.Fdft2(green)
Fblue = hw07.Fdft2(blue)
Fimg1 = np.dstack( (Fred, Fgreen, Fblue) )
F_img = np.log10(abs(Fimg1))
F_img = F_img / np.max(F_img)

plt.subplot(132)
plt.imshow(np.abs(F_img), cmap = 'gray')
plt.title('DFT of Image')
plt.xticks([])
plt.yticks([])

#Trying to get it in a form that's readable again.
ired = hw07.Fidft2(Fred)
igreen = hw07.Fidft2(Fgreen)
iblue = hw07.Fidft2(Fblue)
iimg = np.abs(np.dstack( (ired, igreen, iblue) ))
iimg = iimg / np.max(iimg)


plt.subplot(133)
plt.imshow(iimg)
plt.title('Inverse Fourier Image')
plt.xticks([])
plt.yticks([])
plt.show()

# here you shall implement and plot the Fourier image of the Mines emblem,
# along with the inverse Fourier transform
