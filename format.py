import os
import json

def process_file(filepath):
    commands = {}
    try:
        with open(filepath, 'r', encoding='utf-8', errors='ignore') as file:
            for line in file:
                filename = os.path.basename(filepath)
                parts = line.strip().split(' ', 3)
                if len(parts) < 3:
                    continue
                # Ignore the line number
                command = parts[2]
                option = parts[3] if len(parts) > 3 else ""
                if command not in commands:
                    commands[command] = []
                # Check for duplicates
                if [option, ""] not in commands[command]:
                    commands[command].append([option, "No description", filename])
    except Exception as e:
        print(f"Error processing file {filepath}: {e}")
    return commands

def main():
    folder_path = '.'  # Current directory
    all_commands = {}

    for filename in os.listdir(folder_path):
        if filename.startswith("vojtko"):
            filepath = os.path.join(folder_path, filename)
            file_commands = process_file(filepath)
            for command, details in file_commands.items():
                if command not in all_commands:
                    all_commands[command] = []
                for detail in details:
                    if detail not in all_commands[command]:
                        all_commands[command].append(detail)

    with open('commands.json', 'w') as json_file:
        json.dump(all_commands, json_file, indent=4)

if __name__ == "__main__":
    main()