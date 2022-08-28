# Python-Image-2-text-Reader
This is a flask based web application to extract text from images.

# Disclaimer: None of the code is mine. I have simply assembled this reader application based on the code of others and in time, I shall attribute the various parts to the various authors.

The following Python PIP based modules were used:

opencv-python 4.6.0.66 - cv2
pytesseract 0.3.10
tkinter https://docs.python.org/3/library/tkinter.html
pyautogui
datetime
PIL

# Description of the Libraries Used

OpenCV (Open Source Computer Vision Library: http://opencv.org) is an open-source library that includes several hundreds of computer vision algorithms. The document describes the so-called OpenCV 2.x API, which is essentially a C++ API, as opposed to the C-based OpenCV 1.x API (C API is deprecated and not tested with "C" compiler since OpenCV 2.4 releases)

Python-tesseract is an optical character recognition (OCR) tool for python. That is, it will recognize and “read” the text embedded in images.
Python-tesseract is a wrapper for Google’s Tesseract-OCR Engine. It is also useful as a stand-alone invocation script to tesseract, as it can read all image types supported by the Pillow and Leptonica imaging libraries, including jpeg, png, gif, bmp, tiff, and others. Additionally, if used as a script, Python-tesseract will print the recognized text instead of writing it to a file.

The tkinter package (“Tk interface”) is the standard Python interface to the Tcl/Tk GUI toolkit. This package allows interactive spreadsheet-style tables to be added into a Tkinter application. Tkinter is the standard GUI toolkit for Python. A sample application using these classes is included in the distribution. Now works with Python 3. A sample application using these classes is included in the distribution.

PyAutoGUI is a cross-platform GUI automation Python module for human beings. Used to programmatically control the mouse & keyboard.

The Python Imaging Library adds image processing capabilities to your Python interpreter. This library provides extensive file format support, an efficient internal representation, and fairly powerful image processing capabilities. The core image library is designed for fast access to data stored in a few basic pixel formats. It should provide a solid foundation for a general image processing tool.
