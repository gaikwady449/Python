# Marvellous Data Shield System

## Overview

Marvellous Data Shield System is a Python-based automated backup utility that periodically creates backups of a specified directory. The application detects new and modified files using MD5 hashing, copies only the changed files to a backup folder, and creates a compressed ZIP archive of the backup.

This project demonstrates the use of file handling, directory management, hashing, scheduling, and ZIP compression in Python.

---

## Features

* Automatic scheduled backups
* Incremental backup (copies only new or modified files)
* MD5 hash comparison for file integrity
* Automatic creation of backup directory
* ZIP archive generation with timestamp
* Command-line interface
* Preserves original folder structure

---

## Technologies Used

* Python 3
* os
* shutil
* hashlib
* zipfile
* schedule
* time
* sys

---

## Project Structure

```
MarvellousDataShield/
│
├── Data/                    # Source folder
├── MarvellousBackup/        # Backup folder (created automatically)
├── Demo.py                 # Main Python script
├── README.md
└── Backup_Zip_Files/       # Generated ZIP archives
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/MarvellousDataShield.git
```

Move into the project directory:

```bash
cd MarvellousDataShield
```

Install the required package:

```bash
pip install schedule
```

---

## Usage

Run the script using the following command:

```bash
python Demo.py <TimeInterval> <SourceDirectory>
```

### Example

```bash
python Demo.py 5 Data
```

This command will:

* Monitor the **Data** directory.
* Perform a backup every **5 minutes**.
* Copy only newly added or modified files.
* Create a timestamped ZIP archive of the backup.

---

## Command-Line Options

### Help

```bash
python Demo.py --h
```

Displays information about the project.

### Usage

```bash
python Demo.py --u
```

Displays the command syntax for running the application.

---

## How It Works

1. User specifies the backup interval and source directory.
2. Scheduler runs automatically at the specified interval.
3. The program scans all files in the source directory.
4. MD5 hashes are calculated for each file.
5. Only new or modified files are copied to the backup directory.
6. The backup folder is compressed into a ZIP archive with a timestamp.
7. The process repeats until the program is terminated.

---

## Example Output

```
--------------------------------------------------
-----Marvellous Data Shield System-----
--------------------------------------------------

Backup process started successfully:
Fri Jul 04 10:30:15 2026

Backup completed successfully

Files copied: 12

ZIP file created:
MarvellousBackup_2026-07-04_10-30-15.zip
```

---

## Future Enhancements

* Logging backup activities to a log file
* Restore files from backup
* Email notification after backup completion
* Graphical User Interface (GUI)
* Backup to cloud storage (Google Drive, OneDrive, Dropbox)
* Multi-threaded backup for improved performance
* Backup history and version management

---

## Learning Outcomes

This project demonstrates practical implementation of:

* File handling
* Directory traversal
* Incremental backup techniques
* MD5 hashing
* ZIP file compression
* Task scheduling
* Command-line argument processing
* Python automation

---

## Requirements

* Python 3.8 or above

Install dependencies:

```bash
pip install schedule
```

---

## Author

**Yash Gaikwad**

Electronics & Telecommunication Engineering Student

Skills:

* Python
* MySQL
* Django
* Automation
* AI/ML Enthusiast

---

## License

This project is developed for educational and learning purposes. You are free to use and modify it for personal or academic use.

---

## Acknowledgements

Special thanks to Marvellous Infosystems for providing guidance and inspiration for developing automation projects using Python.

