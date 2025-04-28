import os
import sys

def read_file(file_path):
    """Read text from a file."""
    try:
        with open(file_path, 'r') as file:
            return file.read()
    except Exception as e:
        print(f"Error reading file: {e}")
        return None
    
def write_file(file_path, content):
    """Write text to a file."""
    try: 
        with open(file_path, 'w') as file:
            file.write(content)
        return True
    except Exception as e:
        print(f"Error writing file: {e}")
        return False

def process_text(text):
    """Process the text (count words, convert to uppercase)."""
    if not text:
        return None
    
    # Count words
    word_count = len(text.split())
    
    # Convert to uppercase
    uppercase_text = text.upper()
    
    return {
        "original_text": text,
        "word_count": word_count,
        "uppercase_text": uppercase_text
    }

def write_results(results, output_file):
    """Write the processed results to a file."""
    if not results:
        return False
    
    try:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)
        with open(output_file, 'w') as file:
            file.write(f"Original Text:\n{results['original_text']}\n\n")
            file.write(f"Word Count: {results['word_count']}\n\n")
            file.write(f"Uppercase Text:\n{results['uppercase_text']}\n")
        return True
    except Exception as e:
        print(f"Error writing to file: {e}")
        return False

def main(input_file="input.txt", output_file="output/output.txt"):
    """Main function to process a text file."""
    text = read_file(input_file)
    if text is None:
        print("Could not read the file.")
        return False
    print("\nFile Content:")
    print(text if text else "FILE IS EMPTY")
    if sys.stdin.isatty():
        choice = input("\nDo you want to edit the content of the file? (Y/N): ").strip().upper()
        if choice == 'Y':
            print("\nPlease enter your new content below. Type 'Done' on a new line to finish:")
            lines = []
            while True:
                line = input()
                if line.strip().upper() == "DONE":
                    break
                lines.append(line)
            newText = "\n".join(lines)
            if write_file(input_file, newText):
                print("File has been updated.")
                text = newText
            else:
                print("Failed to update the file.")
    else:
        print("Running in non-interactive mode. Processing existing file content.")
    
    results = process_text(text)
    if results:
        success = write_results(results, output_file)
        if success:
            print(f"Processing complete. Results written to {output_file}")
            input("\nProcessing complete. Press ENTER to exit.")
            return True
    
    print("Processing failed.")
    return False

if __name__ == "__main__":
    main()
