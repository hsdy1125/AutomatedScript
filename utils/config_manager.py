"""
Configuration management module: Responsible for reading, saving, and updating configuration information
"""

import os
import json


class ConfigManager:
    """Configuration management class for handling reading, saving, and updating of configuration files"""
    
    CONFIG_FILE = "chatgpt_config.json"
    
    DEFAULT_CONFIG = {
        "response_timeout": 120,
        "output_dir": "./data/example/chatgpt_results", # Default output directory
        "save_results": False,
        "default_prompts_file": "example/text-only/prompts.txt",
        "num_images_to_process": 100,
        "mode": {
            "window_type": "multi",  # "single" or "multi"
            "input_type": "text_only",  # "text_only" or "text_image"
            "capture_images": True   # True or False
        },
        "text_prefix": "Please generate an image based on the following prompts:\n",  # Prefix to add to each text input in text_only mode
        "use_prefix": True,  # Whether to use the prefix
        "image_folder": "",  # Default folder for images
        "scroll_amount": 10,         # Number of scroll wheel clicks
        "save_image_delay": 15,       # Seconds to wait before saving images (15s before new window)
        "x": 518,  # X coordinate for image capture
        "y": 580  # Y coordinate for image capture
    }
    
    def __init__(self, config_file=None):
        """
        Initialize configuration manager
        
        Args:
            config_file (str, optional): Configuration file path. Defaults to None, using the default path from class variable.
        """
        self.config_file = config_file or self.CONFIG_FILE
        self.config = self.load()
    
    def load(self):
        """
        Load configuration file, create default configuration file if it doesn't exist
        
        Returns:
            dict: Configuration dictionary
        """
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as file:
                    return json.load(file)
            except Exception as exc:
                print(f"Unable to read configuration file. Using default configuration: {exc}")
                return self.DEFAULT_CONFIG.copy()
        else:
            self.save(self.DEFAULT_CONFIG)
            return self.DEFAULT_CONFIG.copy()
    
    def save(self, config=None):
        """
        Save configuration to file
        
        Args:
            config (dict, optional): Configuration to save. Defaults to None, using current configuration.
            
        Returns:
            bool: Whether saving was successful
        """
        if config is None:
            config = self.config
            
        try:
            with open(self.config_file, 'w', encoding='utf-8') as file:
                json.dump(config, file, ensure_ascii=False, indent=2)
            print(f"Configuration saved to {self.config_file}")
            return True
        except Exception as exc:
            print(f"Unable to save configuration file: {exc}")
            return False
    
    def update(self, key, value):
        """
        Update specific configuration item and save
        
        Args:
            key (str): Configuration key, supports dot notation for nested items
            value: New configuration value
            
        Returns:
            dict: Updated configuration
        """
        # Handle nested keys
        if "." in key:
            parts = key.split(".")
            current = self.config
            for part in parts[:-1]:
                if part not in current:
                    current[part] = {}
                current = current[part]
            current[parts[-1]] = value
        else:
            self.config[key] = value
        
        self.save()
        return self.config
    
    def get(self, key, default=None):
        """
        Get configuration item, supports dot notation for nested items
        
        Args:
            key (str): Configuration key
            default: Default value to return if key doesn't exist
            
        Returns:
            Configuration value or default value
        """
        if "." in key:
            parts = key.split(".")
            current = self.config
            for part in parts:
                if part not in current:
                    return default
                current = current[part]
            return current
        else:
            return self.config.get(key, default)
    
    def get_default_config(self):
        """
        Get a copy of the default configuration
        
        Returns:
            dict: Default configuration dictionary
        """
        return self.DEFAULT_CONFIG.copy()