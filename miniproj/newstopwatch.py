import time
import keyboard
def stopwatch():
    print("Controls:")
    print("SPACE: Start/Pause")
    print("R: Reset")
    print("Q: Quit")
    print("\nPress SPACE to start...")
    start_time = None
    elapsed_time = 0
    running = False

    try:
        while True:
            if keyboard.is_pressed('q'):
                print("\nStopwatch stopped.")
                break
            if keyboard.is_pressed('space'):
                time.sleep(0.5)
                if running:
                    running= False
                    if start_time:
                        elapsed_time  += time.time() - start_time
                    print("\nPaused!")
                else:
                    running = True
                    start_time = time.time()   
                    print("\nRunning!")

            if keyboard.is_pressed('r'):
                time.sleep(0.1)
                elapsed_time = 0
                start_time = time.time() if running else None
                print("\nReset!")

            if running:
                current_elapsed = elapsed_time + (time.time() - start_time)
                print(f"\rElapsed Time: {current_elapsed:.2f} seconds", end="")

            time.sleep(0.1)
    except KeyboardInterrupt:
        print('Stopwatch stopped by Ctrl+C.')
stopwatch()