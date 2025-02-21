""" importing required libraries """
import numpy as np
import cv2 as cv
from PIL import Image
from skimage.metrics import peak_signal_noise_ratio, mean_squared_error
from skimage.util import random_noise
import time

"""Name: Qusay Taradeh, ID: 1212508 """

"""
||========================================================================||
||Comparing Simple Smoothing Filters with Advanced Filters on Noisy Images||
||========================================================================||
"""


def add_noise(image, noise_type):
    # copy image
    image_copy = image.copy()
    # convert PIL Image to ndarray
    im_arr = np.asarray(image_copy)

    if noise_type == 's&p':
        """Salt and Pepper Noise Adjustment"""
        low = 0.01
        medium = 0.025
        high = 0.05
        print("Choose the noise Level:")
        while True:
            print("1. Low.\n2. Medium.\n3. High.")
            level = input("Enter Noise Level option: ")
            if level == '1':
                amount = low
                break
            elif level == '2':
                amount = medium
                break
            elif level == '3':
                amount = high
                break
            else:
                print("Please choose a valid Noise Level")

        # applying Salt and Pepper Noise with amount given by user and default value is 0.05
        noise_img = random_noise(im_arr, mode='s&p', amount=amount)
        noise_img = (255 * noise_img).astype(np.uint8)
        return Image.fromarray(noise_img)

    elif noise_type == 'gaussian':
        """Gaussian Noise Adjustment"""
        low = 0.01
        medium = 0.01
        high = 0.5
        print("Choose the noise Level:")
        while True:
            print("1. Low.\n2. Medium.\n3. High.")
            level = input("Enter Noise Level option: ")
            if level == '1':
                var = low
                break
            elif level == '2':
                var = medium
                break
            elif level == '3':
                var = high
                break
            else:
                print("Please choose a valid Noise Level")

        # applying Gaussian Noise with mean = 0 and variance given by user and default value is 0.01
        noise_img = random_noise(im_arr, mode='gaussian', mean=0, var=var)
        noise_img = (255 * noise_img).astype(np.uint8)
        return Image.fromarray(noise_img)


def filters(image, noisy_image, filter_type):
    # copy images
    clean_image = image.copy()
    image_copy = noisy_image.copy()
    # convert PIL Image to ndarray
    im_arr = np.asarray(image_copy)
    clean_image = np.asarray(clean_image)

    if filter_type == 'box':
        """Box Filter"""
        kernel_size = input("Enter the kernel of the filter: ")
        while True:
            if kernel_size.isdigit() and int(kernel_size) >= 1:
                kernel_size = int(kernel_size)
                break
            else:
                kernel_size = input("Enter the kernel in integer format and greater than or equal to 1: ")

        start_time = time.time()
        # apply box filter by cv.blur which is also equivalent cv.boxFilter
        box_filtered = cv.blur(im_arr, (kernel_size, kernel_size))
        elapsed_time = time.time() - start_time
        print('MSE: {:.2f}'.format(mean_squared_error(clean_image, box_filtered)))
        print('PSNR: {:.2f}'.format(peak_signal_noise_ratio(clean_image, box_filtered)))
        print('Elapsed time: {:.2f}ms'.format(elapsed_time * 1000))
        edges_flag = input("Would you like to apply the edges? (y/n): ")
        if edges_flag.lower() == 'y':
            edges = cv.Canny(box_filtered, threshold1=50, threshold2=150)
            edges = Image.fromarray(edges)
            edges.save('filtered_images/edges_kernel=' + str(kernel_size) + '_' + 'time_' + str(time.time()) + '.jpg')
        return Image.fromarray(box_filtered)

    elif filter_type == 'gaussian':
        """Gaussian Filter"""
        kernel_size = input("Enter the kernel of the filter: ")
        while True:
            if kernel_size.isdigit() and int(kernel_size) >= 1:
                kernel_size = int(kernel_size)
                break
            else:
                kernel_size = input("Enter the kernel in integer format and greater than or equal to 1: ")

        start_time = time.time()
        # apply gaussian filter
        gaussian_filtered = cv.GaussianBlur(im_arr, (kernel_size, kernel_size), sigmaX=0)
        elapsed_time = time.time() - start_time
        print('MSE: {:.2f}'.format(mean_squared_error(clean_image, gaussian_filtered)))
        print('PSNR: {:.2f}'.format(peak_signal_noise_ratio(clean_image, gaussian_filtered)))
        print('Elapsed time: {:.2f}ms'.format(elapsed_time * 1000))
        edges_flag = input("Would you like to apply the edges? (y/n): ")
        if edges_flag.lower() == 'y':
            edges = cv.Canny(gaussian_filtered, threshold1=50, threshold2=150)
            edges = Image.fromarray(edges)
            edges.save('filtered_images/edges_kernel=' + str(kernel_size) + '_' + 'time_' + str(time.time()) + '.jpg')
        return Image.fromarray(gaussian_filtered)

    elif filter_type == 'median':
        """Median Filter"""
        kernel_size = input("Enter the kernel of the filter: ")
        while True:
            if kernel_size.isdigit() and int(kernel_size) >= 1:
                kernel_size = int(kernel_size)
                break
            else:
                kernel_size = input("Enter the kernel in integer format and greater than or equal to 1: ")

        start_time = time.time()
        # apply median filter
        median_filtered = cv.medianBlur(im_arr, kernel_size)
        elapsed_time = time.time() - start_time
        print('MSE: {:.2f}'.format(mean_squared_error(clean_image, median_filtered)))
        print('PSNR: {:.2f}'.format(peak_signal_noise_ratio(clean_image, median_filtered)))
        print('Elapsed time: {:.2f}ms'.format(elapsed_time * 1000))
        edges_flag = input("Would you like to apply the edges? (y/n): ")
        if edges_flag.lower() == 'y':
            edges = cv.Canny(median_filtered, threshold1=50, threshold2=150)
            edges = Image.fromarray(edges)
            edges.save('filtered_images/edges_kernel=' + str(kernel_size) + '_' + 'time_' + str(time.time()) + '.jpg')
        return Image.fromarray(median_filtered)

    elif filter_type == 'bilateral':
        """Bilateral Filter"""
        diameter = input("Enter the diameter of the filter: ")
        while True:
            if diameter.isdigit() and int(diameter) >= 1:
                diameter = int(diameter)
                break
            else:
                diameter = input("Enter the diameter in integer format and greater than or equal to 1: ")

        start_time = time.time()
        # apply bilateral filter
        bilateral_filtered = cv.bilateralFilter(im_arr, d=diameter, sigmaColor=75, sigmaSpace=75)
        elapsed_time = time.time() - start_time
        print('MSE: {:.2f}'.format(mean_squared_error(clean_image, bilateral_filtered)))
        print('PSNR: {:.2f}'.format(peak_signal_noise_ratio(clean_image, bilateral_filtered)))
        print('Elapsed time: {:.2f}ms'.format(elapsed_time * 1000))
        edges_flag = input("Would you like to apply the edges? (y/n): ")
        if edges_flag.lower() == 'y':
            edges = cv.Canny(bilateral_filtered, threshold1=50, threshold2=150)
            edges = Image.fromarray(edges)
            edges.save('filtered_images/edges_diameter=' + str(diameter) + '_' + 'time_' + str(time.time()) + '.jpg')
        return Image.fromarray(bilateral_filtered)


print("Welcome to:\n"
      "||========================================================================||\n||Comparing Simple Smoothing "
      "Filters with Advanced Filters on Noisy "
      "Images||\n||========================================================================||")

print("Loading images from clean_images directory.....")
NUM_OF_IMAGES = 2
clean_images = []
for i in range(1, NUM_OF_IMAGES + 1):
    clean_images.append(Image.open('clean_images/n' + str(i) + '.jpg'))

print("Images from clean_images directory loaded successfully.....")

print("Choose the noise type")
while True:
    print("1. Salt and Pepper Noise Adjustment")
    print("2. Gaussian Noise Adjustment")
    noise = input("Enter option number: ")
    if noise == '1':
        print("First Image")
        s_and_p_noisy_image1 = add_noise(image=clean_images[0], noise_type='s&p')
        print("Second Image")
        s_and_p_noisy_image2 = add_noise(image=clean_images[1], noise_type='s&p')
        break
    elif noise == '2':
        print("First Image")
        g_noisy_image1 = add_noise(image=clean_images[0], noise_type='gaussian')
        print("Second Image")
        g_noisy_image2 = add_noise(image=clean_images[1], noise_type='gaussian')
        break
    else:
        print("Please choose a valid Noise Type")

"""Filters application"""
print("Choose the filter type")
while True:
    print("1. Box Filter.\n2. Gaussian Filter.\n3. Median Filter.\n4. Bilateral Filter")
    filter = input("Enter option number: ")
    if filter == '1':
        """Box Filter"""
        if noise == '1':  # Filtering Salt and Pepper Noise
            print("First Image")
            s_and_p_box_filtered_image1 = filters(image=clean_images[0], noisy_image=s_and_p_noisy_image1,
                                                  filter_type="box")
            print("Second Image")
            s_and_p_box_filtered_image2 = filters(image=clean_images[1], noisy_image=s_and_p_noisy_image2,
                                                  filter_type="box")
            s_and_p_box_filtered_image1.save('filtered_images/n1_sp_box_filtered.jpg')
            s_and_p_box_filtered_image2.save('filtered_images/n2_sp_box_filtered.jpg')
        elif noise == '2':  # Filtering Gaussian Noise
            print("First Image")
            g_box_filtered_image1 = filters(image=clean_images[0], noisy_image=g_noisy_image1, filter_type="box")
            print("Second Image")
            g_box_filtered_image2 = filters(image=clean_images[1], noisy_image=g_noisy_image2, filter_type="box")
            g_box_filtered_image1.save('filtered_images/n1_g_box_filtered.jpg')
            g_box_filtered_image2.save('filtered_images/n2_g_box_filtered.jpg')
        break
    elif filter == '2':
        """Gaussian Filter"""
        if noise == '1':  # Filtering Salt and Pepper Noise
            print("First Image")
            s_and_p_gaussian_filtered_image1 = filters(image=clean_images[0], noisy_image=s_and_p_noisy_image1,
                                                       filter_type="gaussian")
            print("Second Image")
            s_and_p_gaussian_filtered_image2 = filters(image=clean_images[1], noisy_image=s_and_p_noisy_image2,
                                                       filter_type="gaussian")
            s_and_p_gaussian_filtered_image1.save('filtered_images/n1_sp_gaussian_filtered.jpg')
            s_and_p_gaussian_filtered_image2.save('filtered_images/n2_sp_gaussian_filtered.jpg')
        elif noise == '2':  # Filtering Gaussian Noise
            print("First Image")
            g_gaussian_filtered_image1 = filters(image=clean_images[0], noisy_image=g_noisy_image1,
                                                 filter_type="gaussian")
            print("Second Image")
            g_gaussian_filtered_image2 = filters(image=clean_images[1], noisy_image=g_noisy_image2,
                                                 filter_type="gaussian")
            g_gaussian_filtered_image1.save('filtered_images/n1_g_gaussian_filtered.jpg')
            g_gaussian_filtered_image2.save('filtered_images/n2_g_gaussian_filtered.jpg')
        break

    elif filter == '3':
        """Median Filter"""
        if noise == '1':  # Filtering Salt and Pepper Noise
            print("First Image")
            s_and_p_median_filtered_image1 = filters(image=clean_images[0], noisy_image=s_and_p_noisy_image1,
                                                     filter_type="median")
            print("Second Image")
            s_and_p_median_filtered_image2 = filters(image=clean_images[1], noisy_image=s_and_p_noisy_image2,
                                                     filter_type="median")
            s_and_p_median_filtered_image1.save('filtered_images/n1_sp_median_filtered.jpg')
            s_and_p_median_filtered_image2.save('filtered_images/n2_sp_median_filtered.jpg')
        elif noise == '2':  # Filtering Gaussian Noise
            print("First Image")
            g_median_filtered_image1 = filters(image=clean_images[0], noisy_image=g_noisy_image1, filter_type="median")
            print("Second Image")
            g_median_filtered_image2 = filters(image=clean_images[1], noisy_image=g_noisy_image2, filter_type="median")
            g_median_filtered_image1.save('filtered_images/n1_g_median_filtered.jpg')
            g_median_filtered_image2.save('filtered_images/n2_g_median_filtered.jpg')
        break

    elif filter == '4':
        """Bilateral Filter"""
        if noise == '1':  # Filtering Salt and Pepper Noise
            print("First Image")
            s_and_p_bilateral_filtered_image1 = filters(image=clean_images[0], noisy_image=s_and_p_noisy_image1,
                                                        filter_type="bilateral")
            print("Second Image")
            s_and_p_bilateral_filtered_image2 = filters(image=clean_images[1], noisy_image=s_and_p_noisy_image2,
                                                        filter_type="bilateral")
            s_and_p_bilateral_filtered_image1.save('filtered_images/n1_sp_bilateral_filtered.jpg')
            s_and_p_bilateral_filtered_image2.save('filtered_images/n2_sp_bilateral_filtered.jpg')
        elif noise == '2':  # Filtering Gaussian Noise
            print("First Image")
            g_bilateral_filtered_image1 = filters(image=clean_images[0], noisy_image=g_noisy_image1,
                                                  filter_type="bilateral")
            print("Second Image")
            g_bilateral_filtered_image2 = filters(image=clean_images[1], noisy_image=g_noisy_image2,
                                                  filter_type="bilateral")
            g_bilateral_filtered_image1.save('filtered_images/n1_g_bilateral_filtered.jpg')
            g_bilateral_filtered_image2.save('filtered_images/n2_g_bilateral_filtered.jpg')
        break
    else:
        print('Invalid filter')
