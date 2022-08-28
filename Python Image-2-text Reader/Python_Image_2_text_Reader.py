# import modules
import cv2
import pytesseract
from tkinter import *
import pyautogui
import datetime
from tkinter import filedialog
from PIL import ImageTk, Image


# Specifying the path of Tesseract executable file

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract.exe'


# Upload interface through Tkinter

root = Tk()
root.title('Upload Image for Text extraction') 

newline= Label(root)
uploaded_img=Label(root)
scrollbar = Scrollbar(root)
scrollbar.pack( side = RIGHT, fill = Y )


def upload():
    try:
        path=filedialog.askopenfilename()
        image=Image.open(path)
        img=ImageTk.PhotoImage(image)
        uploaded_img.configure(image=img)
        uploaded_img.image=img
        show_extract_button(path)
    except:
        pass  

uploadbtn = Button(root,text="Upload an image",command=upload,bg="#2f2f77",fg="gray",height=2,width=20,font=('Times',15,'bold')).pack()
newline.configure(text='\n')
newline.pack()
uploaded_img.pack()

# The Python Snipping Tool through Pyautogui

class Application():
    def __init__(self, master):
        self.master = master
        self.rect = None
        self.x = self.y = 0
        self.start_x = None
        self.start_y = None
        self.curX = None
        self.curY = None

        # root.configure(background = 'red')
        # root.attributes("-transparentcolor","red")

        root.attributes("-transparent", "blue")
        root.geometry('400x50+200+200')  # set new geometry
        root.title('Lil Snippy')
        self.menu_frame = Frame(master, bg="blue")
        self.menu_frame.pack(fill=BOTH, expand=YES)

        self.buttonBar = Frame(self.menu_frame,bg="")
        self.buttonBar.pack(fill=BOTH,expand=YES)

        self.snipButton = Button(self.buttonBar, width=3, command=self.createScreenCanvas, background="green")
        self.snipButton.pack(expand=YES)

        self.master_screen = Toplevel(root)
        self.master_screen.withdraw()
        self.master_screen.attributes("-transparent", "blue")
        self.picture_frame = Frame(self.master_screen, background = "blue")
        self.picture_frame.pack(fill=BOTH, expand=YES)

    def takeBoundedScreenShot(self, x1, y1, x2, y2):
        im = pyautogui.screenshot(region=(x1, y1, x2, y2))
        x = datetime.datetime.now()
        fileName = x.strftime("%f")
        #im.save("snips/" + fileName + ".png")
        im.save("snip.png")

    def createScreenCanvas(self):
        self.master_screen.deiconify()
        root.withdraw()

        self.screenCanvas = Canvas(self.picture_frame, cursor="cross", bg="grey11")
        self.screenCanvas.pack(fill=BOTH, expand=YES)

        self.screenCanvas.bind("<ButtonPress-1>", self.on_button_press)
        self.screenCanvas.bind("<B1-Motion>", self.on_move_press)
        self.screenCanvas.bind("<ButtonRelease-1>", self.on_button_release)

        self.master_screen.attributes('-fullscreen', True)
        self.master_screen.attributes('-alpha', .3)
        self.master_screen.lift()
        self.master_screen.attributes("-topmost", True)

    def on_button_release(self, event):
        self.recPosition()

        if self.start_x <= self.curX and self.start_y <= self.curY:
            print("right down")
            self.takeBoundedScreenShot(self.start_x, self.start_y, self.curX - self.start_x, self.curY - self.start_y)

        elif self.start_x >= self.curX and self.start_y <= self.curY:
            print("left down")
            self.takeBoundedScreenShot(self.curX, self.start_y, self.start_x - self.curX, self.curY - self.start_y)

        elif self.start_x <= self.curX and self.start_y >= self.curY:
            print("right up")
            self.takeBoundedScreenShot(self.start_x, self.curY, self.curX - self.start_x, self.start_y - self.curY)

        elif self.start_x >= self.curX and self.start_y >= self.curY:
            print("left up")
            self.takeBoundedScreenShot(self.curX, self.curY, self.start_x - self.curX, self.start_y - self.curY)

        self.exitScreenshotMode()
        return event

    def exitScreenshotMode(self):
        print("Screenshot mode exited")
        self.screenCanvas.destroy()
        self.master_screen.withdraw()
        root.deiconify()

    def exit_application(self):
        print("Application exit")
        root.quit()

    def on_button_press(self, event):
        # save mouse drag start position
        self.start_x = self.screenCanvas.canvasx(event.x)
        self.start_y = self.screenCanvas.canvasy(event.y)

        self.rect = self.screenCanvas.create_rectangle(self.x, self.y, 1, 1, outline='red', width=3, fill="blue")

    def on_move_press(self, event):
        self.curX, self.curY = (event.x, event.y)
        # expand rectangle as you drag the mouse
        self.screenCanvas.coords(self.rect, self.start_x, self.start_y, self.curX, self.curY)

    def recPosition(self):
        print(self.start_x)
        print(self.start_y)
        print(self.curX)
        print(self.curY)

#if __name__ == '__main__':
    #root = Tk()
    #app = Application(root)
    #root.mainloop()


#Providing the location of Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 

# Read image generated by Snipping tool
#img = cv2.imread('Krishna.jpg')
img = cv2.imread("snip.png")

print(img)

# set configurations
config = ('-l eng --oem 1 --psm 3')

# Convert the image to gray scale 
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
  
# OTSU threshold performing
ret, threshimg = cv2.threshold(gray, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV) 
  
# Specifying kernel size and structure shape.  
rect_kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (18, 18)) 
  
# Appplying dilation on the threshold image 
dilation = cv2.dilate(threshimg, rect_kernel, iterations = 1) 
  
# getting contours 
img_contours, hierarchy = cv2.findContours(dilation, cv2.RETR_EXTERNAL,  
                                                 cv2.CHAIN_APPROX_NONE) 
  
# Loop over contours and crop and extract the text file
for cnt in img_contours: 
    x, y, w, h = cv2.boundingRect(cnt) 
      
    # Drawing a rectangle
    rect = cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2) 
      
    # Cropping the text block  
    cropped_img = img[y:y + h, x:x + w] 
      
    # Open the text file in append mode 
    file = open("recognized.txt", "a") 
      
    # Applying tesseract OCR on the cropped image 
    text = pytesseract.image_to_string(cropped_img) 
      
    # Appending the text into file 
    file.write(text) 
    file.write("\n") 
      
    # Close the file 
    file.close 

if __name__ == '__main__':
    root = Tk()
    app = Application(root)
    root.mainloop()
