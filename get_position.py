import pyautogui
import time
import os

def get_mouse_click_coordinates():
    """
    Create a program that allows the user to click anywhere on the screen
    and return the coordinates of the click position.
    Uses command line interface instead of tkinter.
    """
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("="*50)
    print("Mouse Click Coordinates Capture")
    print("="*50)
    print("\nPreparing to capture mouse click...")
    print("Will start listening for clicks in 5 seconds, please move your mouse to the target position and click.")
    
    # Countdown
    for i in range(5, 0, -1):
        print(f"Countdown: {i} seconds", end='\r')
        time.sleep(1)
    
    print("\nNow please click on the target position on screen...                ")
    
    # Wait for mouse click
    x, y = pyautogui.position()  # Get current mouse position
    old_x, old_y = x, y
    
    # Loop to detect mouse position changes or clicks
    while True:
        # Get current mouse position
        x, y = pyautogui.position()
        
        # If position changed, update display
        if x != old_x or y != old_y:
            print(f"Current mouse position: X = {x}, Y = {y}", end='\r')
            old_x, old_y = x, y
            
        # Detect mouse click
        if pyautogui.mouseDown():
            click_x, click_y = x, y
            print(f"\n\nClick coordinates: X = {click_x}, Y = {click_y}")
            print("="*50)
            return click_x, click_y
            
        # Short pause to reduce CPU usage
        time.sleep(0.1)

def track_mouse_position():
    """
    Real-time tracking of mouse position and recording coordinates when clicked.
    Press Ctrl+C to exit the program.
    """
    # Clear screen
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("="*50)
    print("Mouse Position Real-time Tracker")
    print("="*50)
    print("Move the mouse to see coordinates, click left mouse button to record coordinates.")
    print("Press Ctrl+C to exit the program.")
    print("="*50)
    
    try:
        # Continuous loop until Ctrl+C is pressed
        while True:
            # Get current mouse position
            x, y = pyautogui.position()
            
            # Display current position
            print(f"Current mouse position: X = {x}, Y = {y}", end='\r')
            
            # Detect mouse click
            if pyautogui.mouseDown():
                print(f"\nRecorded click coordinates: X = {x}, Y = {y}")
                print("-"*30)
                # Short pause to avoid recording multiple clicks
                time.sleep(0.5)
                
            # Short pause to reduce CPU usage
            time.sleep(0.1)
                
    except KeyboardInterrupt:
        print("\n\nProgram exited")
        print("="*50)

if __name__ == "__main__":
    # Choose function
    print("Select function:")
    print("1. Single mouse click coordinate capture")
    print("2. Real-time mouse position tracking and click recording")
    
    choice = input("Enter option (1 or 2): ")
    
    if choice == '1':
        x, y = get_mouse_click_coordinates()
        print(f"Returned coordinates: X = {x}, Y = {y}")
    elif choice == '2':
        track_mouse_position()
    else:
        print("Invalid option, program exited.")