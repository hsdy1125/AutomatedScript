"""
File management module: Responsible for file reading, saving, and image file collection
"""

import os
import random


class FileManager:
    """
    File management class for handling file operations and image file collection
    """
    
    def __init__(self, output_dir=None):
        """
        Initialize file manager
        
        Args:
            output_dir (str, optional): Output directory path. Defaults to None.
        """
        self.output_dir = output_dir
        if output_dir:
            self.prepare_output_folder(output_dir)
    
    def read_prompt_file(self, file_path):
        """
        Read prompts from a text file
        
        Args:
            file_path (str): File path
            
        Returns:
            str or None: Prompt content or None (if reading fails)
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                content = file.read().strip()
            return content
        except FileNotFoundError:
            print(f"Error: Prompt file not found: {file_path}")
            return None
        except Exception as exc:
            print(f"Error reading prompt file: {exc}")
            return None
    
    def save_text_to_file(self, text, file_path):
        """
        Save text content to a file
        
        Args:
            text (str): Text to save
            file_path (str): File path
            
        Returns:
            bool: Whether operation was successful
        """
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(text)
            return True
        except Exception as exc:
            print(f"Error saving text to file: {exc}")
            return False
    
    def collect_image_files(self, folder_path, num_to_process=None):
        """
        Collect image files from a folder
        
        Args:
            folder_path (str): Folder path
            num_to_process (int, optional): Number of images to process. Defaults to None (all).
            
        Returns:
            list: List of image filenames
        """
        if not os.path.isdir(folder_path):
            print(f"Error: Invalid image folder: {folder_path}")
            return []
        
        valid_exts = [".jpg", ".jpeg", ".png", ".bmp", ".gif", ".tiff"]
        images = sorted([
            f for f in os.listdir(folder_path)
            if not f.startswith('.') and os.path.splitext(f)[1].lower() in valid_exts
        ])
        
        if not images:
            print(f"No valid images found in folder: {folder_path}")
            return []
        
        total_images = len(images)
        print(f"Found {total_images} images in folder: {folder_path}")
        
        if num_to_process and num_to_process < total_images:
            selected_images = random.sample(images, num_to_process)
            selected_images.sort()
            return selected_images
        
        return images
    
    def prepare_output_folder(self, base_path):
        """
        Prepare output folder structure
        
        Args:
            base_path (str): Base path
            
        Returns:
            str: Full path of the output folder
        """
        os.makedirs(base_path, exist_ok=True)
        return base_path
    
    def save_results(self, output_dir, img_name, response_text, prompt_text):
        """
        Save results for processed image
        
        Args:
            output_dir (str): Output directory
            img_name (str): Image filename
            response_text (str): Response text
            prompt_text (str): Prompt used
            
        Returns:
            bool: Whether operation was successful
        """
        base_name, _ = os.path.splitext(img_name)
        save_folder = os.path.join(output_dir, base_name)
        # os.makedirs(save_folder, exist_ok=True)
        
        # # Save response text
        # result_file = os.path.join(save_folder, "output.txt")
        # response_saved = self.save_text_to_file(response_text, result_file)
        # if response_saved:
        #     print(f"Text result saved to: {result_file}")
        
        # # Save prompt text
        # prompt_file = os.path.join(save_folder, "prompt.txt")
        # prompt_saved = self.save_text_to_file(prompt_text, prompt_file)
        # if prompt_saved:
        #     print(f"Prompt saved to: {prompt_file}")
        
        return