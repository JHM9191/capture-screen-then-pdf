import time
import pyautogui as p
from pyautogui import press
from PIL import Image, ImageGrab

dest = '/Users/johyunmin/PycharmProjects/captureConvertPdf/'


def capture(name, x, y, w, h):
    file = p.screenshot(region=(x, y, w, h))
    file.save(dest + name + '.png')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('program start')
    time.sleep(5)
    im_list = []
    book_length = 217
    X1 = 25
    Y1 = 25
    X2 = 854
    Y2 = 1120
    box = (X1, Y1, X2, Y2)

    capture('cover', 25, 25, 854, 1120)
    cover = Image.open(dest + 'cover.png').convert("RGB")

    for i in range(0, book_length):
        press("right")  # Assuming the down arrow key switches between pages
        # Change to press("right") if right arrow key works instead, and so on.

        time.sleep(2)  # arbitrary delay between screenshots
        im = ImageGrab.grab(bbox=box).convert('RGB')
        im_list.append(im)

    cover.save("Textbook.pdf", "PDF", resolution=500.0, save_all=True, append_images=im_list)

    print('program end')
