# Image Processing Project I  
Comparing Simple Smoothing Filters with Advanced Filters on Noisy Images

## Summary  
Implementation of an image denoising project that compares simple smoothing filters (Box, Gaussian, and Median) with advanced adaptive filters (Adaptive Mean, Adaptive Median, and Bilateral) on noisy images. The project evaluates each filter's noise removal effectiveness, edge preservation, and computational efficiency using metrics such as Mean Squared Error (MSE) and Peak Signal-to-Noise Ratio (PSNR), while also analyzing the impact of varying kernel sizes.

## Specifications  
This application should be able to perform the following tasks:
1. **Image Preparation:**  
   - Load or generate a set of clean images and add various types of noise (e.g., Gaussian noise, Salt-and-Pepper noise) at different intensity levels.
   
2. **Filter Application:**  
   - Apply simple smoothing filters (Box, Gaussian, Median) and advanced adaptive filters (Adaptive Mean, Adaptive Median, Bilateral) on each noisy image using multiple kernel sizes.

3. **Performance Measurement:**  
   - Compute quantitative metrics such as Mean Squared Error (MSE) and Peak Signal-to-Noise Ratio (PSNR) for each filter across different kernel sizes.
   - Use edge detection (e.g., Canny edge detector) to evaluate and compare edge preservation.
   - Measure and report the computational time for each filter implementation.

4. **Analysis:**  
   - Analyze the trade-offs between noise reduction and edge preservation as the kernel size changes.
   - Compare the computational efficiency of simple versus advanced filters.
   - Summarize how kernel size influences overall filter performance.

## Author  
Qusay Taradeh
