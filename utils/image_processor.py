"""
Image processing module: Responsible for image capture, saving, and related mouse operations
"""

import os
import time
import pyautogui
from PIL import ImageGrab


class ImageProcessor:
    """
    Image processing class for screen operations, image capture and saving
    """
    
    def __init__(self, scroll_amount=10):
        """
        Initialize the image processor
        
        Args:
            scroll_amount (int, optional): Number of scroll actions. Defaults to 10.
        """
        self.scroll_amount = scroll_amount
    
    def scroll_to_bottom(self):
        """
        Use scroll wheel to reach the bottom of the current ChatGPT window
        """
        # Get current mouse position to restore later
        current_x, current_y = pyautogui.position()
        
        # Move to the middle of the screen
        screen_width, screen_height = pyautogui.size()
        middle_x, middle_y = screen_width // 2, screen_height // 2
        
        pyautogui.moveTo(middle_x, middle_y, duration=0.2)
        
        # Multiple scroll-down actions to reach the bottom
        for _ in range(self.scroll_amount):
            pyautogui.scroll(-1)  # Negative value for scrolling down
            time.sleep(0.1)
        
        # Restore mouse position
        pyautogui.moveTo(current_x, current_y, duration=0.2)
        print("Scrolled to window bottom")
    
    def copy_image_from_screen(self, x, y, x_shift=20, y_shift=0):
        """
        Automatically copy an image from screen using right-click menu
        
        Args:
            x (int): Image X coordinate
            y (int): Image Y coordinate
            x_shift (int, optional): Right-click menu X offset. Defaults to 20.
            y_shift (int, optional): Right-click menu Y offset. Defaults to 0.
        """
        pyautogui.moveTo(x, y, duration=0.2)
        pyautogui.rightClick()
        time.sleep(0.5)
        pyautogui.moveTo(x + x_shift, y + y_shift, duration=0.2)
        pyautogui.click()
    
    def save_image_from_screen(self, x, y, x_shift=30, y_shift=0):
        """
        Automatically save an image from screen using right-click menu
        
        Args:
            x (int): Image X coordinate
            y (int): Image Y coordinate
            x_shift (int, optional): Right-click menu X offset. Defaults to 30.
            y_shift (int, optional): Right-click menu Y offset. Defaults to 0.
        """
        pyautogui.moveTo(x, y, duration=0.2)
        pyautogui.rightClick()
        time.sleep(0.5)
        # Adjust these coordinates to match the "Save Image" option in the right-click menu
        pyautogui.moveTo(x + x_shift, y + y_shift + 20, duration=0.2)  # +20 to position on "Save Image" instead of "Copy Image"
        pyautogui.click()
        # Wait for save dialog and press Enter
        time.sleep(1)
        pyautogui.press('enter')
    
    def copy_and_save_gpt_output_image(self, x, y, x_shift, y_shift, img_name, output_dir):
        """
        Use PyAutoGUI and PIL to capture and save ChatGPT output image from screen
        
        Args:
            x (int): Image X coordinate
            y (int): Image Y coordinate
            x_shift (int): Right-click menu X offset
            y_shift (int): Right-click menu Y offset
            img_name (str): Image name (without extension)
            output_dir (str): Output directory path
            
        Returns:
            bool: Whether the operation was successful
        """
        print(f"Attempting to copy GPT output image at coordinates ({x}, {y})...")
        
        # First scroll to the bottom of the window
        self.scroll_to_bottom()
        time.sleep(1)
        
        # Copy image to clipboard
        self.copy_image_from_screen(x, y, x_shift, y_shift)

        # Wait for clipboard to update
        time.sleep(2)

        # Get image from clipboard
        image = ImageGrab.grabclipboard()
        if image is None:
            print("No image found in clipboard.")
            return False

        # Save image to file
        target_folder = os.path.join(output_dir, img_name)
        os.makedirs(target_folder, exist_ok=True)
        target_path = os.path.join(target_folder, "image.png")

        try:
            image.save(target_path, "PNG")
            print(f"Image saved: {target_path}")
            return True
        except Exception as exc:
            print(f"Failed to save image: {exc}")
            return False