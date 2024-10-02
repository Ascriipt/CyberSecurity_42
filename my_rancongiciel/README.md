# File Encryption Ransomware Script
This script encrypts and decrypts files in the current working directory using the `Fernet` symmetric encryption method. It is designed to recursively find and encrypt files with specified extensions, and then decrypt them with a key.

## How to Use
1. **Encryption**

   By default, the script will encrypt files in the current directory based on valid extensions listed in a file named `extensions`. The generated key will be saved in a file called `key`.

   Run:
   ./stockholm

**Important**: Ensure you have an `extensions` file in the root directory, listing file extensions (e.g., `.txt`, `.jpg`) to encrypt, one per line.

2. **Decryption**

To decrypt files, use the `-r` or `--reverse` flag with the `key` used during encryption:

./stockholm -r key

3. **Silent Mode**

You can run the script without output messages by using the `-s` or `--silent` flag:

For encryption:
   ./stockholm -s

For decryption:
   ./stockholm -r key -s

4. **Display Version**

Use the `-v` or `--version` flag to display the current version of the script:

./stockholm -v

## Files and Directory Structure
- `key`: Contains the generated encryption key.
- `extensions`: A text file listing valid file extensions for encryption, one per line.
- Encrypted files will have the `.ft` extension.
- Decrypted files will revert to their original extensions.

## Error Handling
- If the `key` file is missing or inaccessible during decryption, an error will be raised.
- Any file encryption or decryption errors will be reported with the filename.

## Notes
- Ensure the script is run from the `~/infection` directory, otherwise an error will occur.
- If interrupted, the process will exit gracefully.