def file_read_write():
    # Ask the user for the input filename
    input_file = input("Enter the name of the file to read: ")
    
    try:
        # Try to open and read the file
        with open(input_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        # Modify the content (example: convert to uppercase)
        modified_content = content.upper()
        
        # Create a new file name
        output_file = "modified_" + input_file
        
        # Write the modified content into the new file
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(modified_content)
        
        print(f"File processed successfully! Modified file saved as: {output_file}")
    
    except FileNotFoundError:
        print(" Error: The file does not exist. Please check the filename and try again.")
    


# Run the challenge
file_read_write()