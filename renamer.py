import os

directory = r"C:\Users\Zavistnichek\projects\test\01"

for filename in os.listdir(directory):
    if filename.endswith(".py"):
        parts = filename.replace('.py', '').split('.')
        if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
            new_name = f"{int(parts[0]):02}.{int(parts[1]):02}.py"
            old_path = os.path.join(directory, filename)
            new_path = os.path.join(directory, new_name)
            os.rename(old_path, new_path)
