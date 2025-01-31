import time

# def stopwatch():
#     input("Press Enter to START the stopwatch,Press Enter to view time elapsed ")
#     start_time = time.time()
#     print("Enter 'q' to Stop the stopwatch...")
#     run = True
#     try:
#         while run:
#             elapsed_time = time.time() - start_time
#             hours = int(elapsed_time // 3600)
#             minutes = int((elapsed_time % 3600) // 60)
#             seconds = int(elapsed_time % 60)
            
#             print(f"Elapsed Time: {hours:02}:{minutes:02}:{seconds:02}", end="\r")
#             time.sleep(1)

#             user_input = input()
#             if user_input.strip().lower() == 'q':
#                 run = False
#     except KeyboardInterrupt:
#         print("\nStopwatch stopped.")

# stopwatch()
# by assigning global value

global running
running = True
def stop_stopwatch():
    running = False

def start_stopwatch():
    # global running
    input("Press Enter to start watch")
    start_time = time.time()
    try:
        while running:
            elapsed_time = time.time() - start_time
            hours = int(elapsed_time // 3600)
            minutes = int((elapsed_time % 3600) // 60)
            seconds = int(elapsed_time % 60)
            print(f"Elapsed Time: {hours:02}:{minutes:02}:{seconds:02}", end="\r")
            # time.sleep()
            # user_input = input()
            # if user_input.strip().lower() == 'q':
            #     stop_stopwatch()
    except KeyboardInterrupt:
        print("\nStopwatch stopped by Ctrl+C.")
    print("\nStopwatch stopped.")
start_stopwatch()

# def start_stopwatch():
#     start_time = time.time()
#     while True:
#         try:
#             elapsed_time = time.time() - start_time
#             hours = int(elapsed_time // 3600)
#             minutes = int((elapsed_time % 3600) // 60)
#             seconds = int(elapsed_time % 60)
            
#             # print(f"Elapsed Time: {hours:02}:{minutes:02}:{seconds:02}")
#             print(f"Elapsed Time: {hours:02}:{minutes:02}:{seconds:02}", end="\r")
#             time.sleep(1)
#         except KeyboardInterrupt:
#             print(f"Total Elapsed Time: {hours:02}:{minutes:02}:{seconds:02}")
#             break
    
# start_stopwatch()

# import time
# import keyboard

# def stopwatch():
#     print("Controls:")
#     print("SPACE: Start/Pause")
#     print("R: Reset")
#     print("Q: Quit")
#     print("\nPress SPACE to start...")
    
#     start_time = None
#     elapsed_time = 0
#     running = False

#     try:
#         while True:
#             if keyboard.is_pressed('q'):
#                 print("\nStopwatch stopped.")
#                 break
                
#             if keyboard.is_pressed('space'):
#                 time.sleep(0.1)
#                 if running:
#                     running = False
#                     if start_time:
#                         elapsed_time += time.time() - start_time
#                     print("\nPaused!")
#                 else:
#                     running = True
#                     start_time = time.time()
#                     print("\nRunning!")
                    
#             if keyboard.is_pressed('r'):
#                 time.sleep(0.01)
#                 elapsed_time = 0
#                 start_time = time.time() if running else None
#                 print("\nReset!")
            
#             current_elapsed = elapsed_time
#             if running and start_time:
#                 current_elapsed += time.time() - start_time
                
#             total_seconds = int(current_elapsed)
#             hours = total_seconds // 3600
#             minutes = (total_seconds % 3600) // 60
#             seconds = total_seconds % 60
            
#             status = "Running" if running else "Paused"
#             print(f"\rElapsed Time: {hours:02d}:{minutes:02d}:{seconds:02d} | Status: {status}", end="", flush=True)
#             time.sleep(0.1)
#     except KeyboardInterrupt:
#         print("\nStopwatch stopped by Ctrl+C.")

# stopwatch()