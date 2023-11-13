use std::fs::File;
use std::io::{Read, Write};
use std::error::Error;

fn main() {
    match copy_file_contents("source.txt", "destination.txt") {
        Ok(_) => println!("File contents copied successfully."),
        Err(e) => eprintln!("Error occurred: {}", e),
    }
}

fn copy_file_contents(source_path: &str, dest_path: &str) -> Result<(), Box<dyn Error>> {
    // Open the source file for reading.
    let mut source_file = match File::open(source_path) {
        Ok(file) => file,
        Err(_) => return Err(format!("Source file '{}' not found.", source_path).into()),
    };

    // Create or open the destination file for writing.
    let mut dest_file = match File::create(dest_path) {
        Ok(file) => file,
        Err(_) => return Err(format!("Failed to create or open destination file '{}'.", dest_path).into()),
    };

    // Buffer to hold the contents of the source file.
    let mut buffer = String::new();

    // Read the contents of the source file.
    if let Err(_) = source_file.read_to_string(&mut buffer) {
        return Err(format!("Failed to read contents from source file '{}'.", source_path).into());
    }

    // Write the buffer contents to the destination file.
    if let Err(_) = dest_file.write_all(buffer.as_bytes()) {
        return Err(format!("Failed to write contents to destination file '{}'.", dest_path).into());
    }

    Ok(())
}
