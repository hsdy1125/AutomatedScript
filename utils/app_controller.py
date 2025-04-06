"""
Application control module: Responsible for ChatGPT application startup, window management, and interaction
"""

import subprocess
import time


class AppController:
    """Application control class for handling ChatGPT application startup, interaction, and window management"""
    
    def __init__(self):
        """Initialize application controller"""
        pass
    
    def run_applescript(self, script):
        """
        Run AppleScript script
        
        Args:
            script (str): AppleScript script string
            
        Returns:
            tuple: (stdout, returncode). Returns (None, -1) if an error occurs
        """
        try:
            result = subprocess.run(
                ['osascript', '-e', script],
                capture_output=True,
                text=True,
                check=False
            )
            if result.returncode != 0 and result.stderr:
                print(f"AppleScript warning: {result.stderr}")
            return (result.stdout.strip(), result.returncode)
        except Exception as exc:
            print(f"Error running AppleScript: {exc}")
            return (None, -1)
    
    def check_chatgpt_running(self):
        """
        Check if ChatGPT application is running. If not, try to start it.
        
        Returns:
            bool: True if ChatGPT is running or successfully started, False otherwise
        """
        try:
            script = '''
                tell application "System Events"
                    return (name of processes) contains "ChatGPT"
                end tell
            '''
            result, status = self.run_applescript(script)
            
            if result != "true":
                print("ChatGPT is not running. Attempting to start...")
                launch_script = '''
                    tell application "ChatGPT" to activate
                    delay 2
                    tell application "System Events"
                        repeat 5 times
                            if (name of processes) contains "ChatGPT" then
                                exit repeat
                            end if
                            delay 1
                        end repeat
                    end tell
                '''
                self.run_applescript(launch_script)
                print("ChatGPT has been started.")
                
                # Check again
                verify_script = '''
                    tell application "System Events"
                        return (name of processes) contains "ChatGPT"
                    end tell
                '''
                verify_result, _ = self.run_applescript(verify_script)
                return verify_result == "true"
            else:
                return True
        except Exception as exc:
            print(f"Error checking ChatGPT status: {exc}")
            return False
    
    def create_new_chat(self):
        """
        Attempt to create a new ChatGPT conversation window.
        
        Returns:
            bool: True if successful, False otherwise
        """
        if not self.check_chatgpt_running():
            print("Unable to access ChatGPT.")
            return False

        script = '''
            tell application "ChatGPT"
                activate
                delay 1
            end tell

            tell application "System Events"
                tell process "ChatGPT"
                    try
                        keystroke "n" using command down
                        delay 1
                        return true
                    on error errMsg
                        return false
                    end try
                end tell
            end tell
        '''
        result, status = self.run_applescript(script)
        if status == 0 and result == "true":
            print("--- New conversation created ---")
            return True
        else:
            print("Failed to create new conversation.")
            return False
    
    def ask_chatgpt(self, prompt, img_path=None, config=None):
        """
        Use AppleScript automation to send text prompts to ChatGPT, optionally sending an image.
        
        Args:
            prompt (str): Text prompt
            img_path (str, optional): Image file path, if not provided only text will be sent
            config (dict): Configuration dictionary containing timeout settings
            
        Returns:
            str: ChatGPT's response text or timeout message
        """
        if not self.check_chatgpt_running():
            raise Exception("ChatGPT is not running or cannot be accessed.")

        # Escape double quotes and newlines
        safe_prompt = prompt.replace('"', '\\"').replace('\n', '\\n')
        
        # Base script - copy and paste text prompt
        applescript_cmd = f'''
            -- Step 1: Copy prompt to system clipboard
            do shell script "osascript -e 'set the clipboard to \\"{safe_prompt}\\"'"
            delay 0.5

            -- Step 2: Activate ChatGPT and paste text
            tell application "ChatGPT" to activate
            delay 1

            tell application "System Events"
                tell application process "ChatGPT"
                    set frontmost to true
                    delay 0.5

                    keystroke "v" using {{command down}}
                    delay 1
                end tell
            end tell
        '''
        
        # If image path is provided, add image paste steps
        if img_path:
            shell_safe_img_path = img_path.replace('"', '\\"')
            applescript_cmd += f'''
                -- Step 3: Copy image file to system clipboard
                do shell script "osascript -e 'set the clipboard to (POSIX file \\"{shell_safe_img_path}\\")'"
                delay 2

                -- Step 4: Paste image into ChatGPT
                tell application "System Events"
                    tell application process "ChatGPT"
                        keystroke "v" using {{command down}}
                        delay 5
                    end tell
                end tell
            '''
        
        # Complete script - send and get response
        applescript_cmd += f'''
            -- Step 5: Press Enter to send
            tell application "System Events"
                tell application process "ChatGPT"
                    key code 36
                    delay 120

                    -- Step 6: Try to get latest response
                    set responseText to ""
                    try
                        set responseText to value of text area 2 of group 1 of group 1 of window 1
                    on error errMsg
                        set responseText to "Failed to get ChatGPT response: " & errMsg
                    end try
                    return responseText
                end tell
            end tell
        '''

        start_time = time.time()
        response = None
        timeout = config.get("response_timeout", 130)

        while response is None and (time.time() - start_time) < timeout:
            result, status = self.run_applescript(applescript_cmd)
            if status == 0:
                response = result
            else:
                time.sleep(2)

        if response is None:
            response = f"Response timeout after waiting {timeout} seconds."

        return response