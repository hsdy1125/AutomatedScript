"""
Processor module: Responsible for integrating other module functionalities and handling the complete process for each task
"""

import os
import time


class Processor:
    """
    Processor class that integrates various modules to process individual tasks
    """
    
    def __init__(self, config_manager, app_controller, image_processor, file_manager):
        """
        Initialize the processor
        
        Args:
            app_controller: AppController instance for ChatGPT interaction
            image_processor: ImageProcessor instance for image capture processing
            file_manager: FileManager instance for file operations
            x (int): Image X coordinate
            y (int): Image Y coordinate
            x_shift (int): Right-click menu X offset
            y_shift (int): Right-click menu Y offset
        """
        self.app_controller = app_controller
        self.image_processor = image_processor
        self.file_manager = file_manager
        
        self.x = config_manager.config["x"]
        self.y = config_manager.config["y"]
        self.x_shift = 20
        self.y_shift = 0
    
    def process_task(self, item_name, prompt, config, img_path=None, new_chat=True):
        """
        Process a single task interaction with ChatGPT, either text-only or text+image
        
        Args:
            item_name (str): Item name used for saving results
            prompt (str): Prompt to use
            config (dict): Configuration dictionary
            img_path (str, optional): Image file path, if not provided only text will be sent
            new_chat (bool, optional): Whether to create a new chat. Defaults to True.
            
        Returns:
            bool: Whether processing was successful
        """
        output_dir = config["output_dir"]
        capture_images = config["mode"]["capture_images"]
        save_image_delay = config.get("save_image_delay", 15)
        
        # Create a new chat if in multi-window mode and new chat is required
        if new_chat and config["mode"]["window_type"] == "multi":
            created = self.app_controller.create_new_chat()
            if not created:
                print("Failed to create new chat, sending in current chat window...")

        # Send prompt (and optional image) to ChatGPT
        try:
            # Calculate when to save image
            start_time = time.time()
            
            # Send prompt (and optional image) and get response
            response = self.app_controller.ask_chatgpt(prompt, img_path, config)
            
            # Save text response and prompt
            base_name = os.path.splitext(item_name)[0] if '.' in item_name else item_name
            self.file_manager.save_results(output_dir, item_name, response, prompt)
            
            # Calculate elapsed time
            elapsed_time = time.time() - start_time
            
            # If processing in multi-window mode, capture before opening a new window
            if config["mode"]["window_type"] == "multi":
                # Calculate time to wait
                wait_time = max(0, (config["response_timeout"] - save_image_delay) - elapsed_time)
                if wait_time > 0:
                    print(f"Waiting {wait_time:.1f} seconds before capturing image...")
                    time.sleep(wait_time)
            else:
                # In single-window mode, wait briefly after response
                time.sleep(2)  # Brief wait after response
            
            # Try to capture GPT output image
            self.image_processor.copy_and_save_gpt_output_image(
                x=self.x,
                y=self.y,
                x_shift=self.x_shift,
                y_shift=self.y_shift,
                img_name=base_name,
                output_dir=output_dir
            )
            
            return True
        except Exception as exc:
            print(f"Exception occurred while processing {item_name}: {str(exc)}")
            return False