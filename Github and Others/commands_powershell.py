print("List of Powershell Commands")

# Using raw string to avoid unicode escape issues
commands = r'''
# List files and folders in the current directory
dir  # alias for Get-ChildItem

# List the contents of the current directory (another alias for Get-ChildItem)
ls   # alias for Get-ChildItem

# Print the current working directory
pwd  # alias for Get-Location

# Create a new directory (folder)
mkdir NewFolder  # alias for New-Item -Type Directory

# Delete a file or directory
rm file.txt  # alias for Remove-Item

# Delete one or more files
del file.txt  # alias for Remove-Item

# Move or rename files and directories
move file.txt C:\new_folder\  # alias for Move-Item

# Copy files or directories
copy file.txt C:\backup\  # alias for Copy-Item

# Rename a file or directory
rename file.txt newfile.txt  # alias for Rename-Item

# Get help information about a command or function
get-help dir  # Example to get help for the 'dir' command

# Clear the screen in the PowerShell window
clear  # alias for Clear-Host

# Exit the PowerShell session
exit

# Print output to the console
echo "Hello, World!"  # alias for Write-Output

# Open a file or URL using the default program or browser
start https://www.google.com

# Display a list of currently running processes
get-process

# Stop a running process by its name
stop-process -name "notepad"

# Change the current directory
set-location "C:\Users\Dell\Desktop"  # alias for cd 

# Display the current directory
get-location  # alias for pwd 

# Check if a file or directory exists
test-path "C:\Users\Dell\Desktop\Python Projects"

# Send output to a file
echo "Hello, World!" | out-file "output.txt"

# Download a file from a URL
Invoke-WebRequest -Uri "https://example.com" -OutFile "example.html"

# Read the content of a file
get-content "file.txt"

# Write content to a file
"New content" | set-content "file.txt"
'''

# Print the commands
print(commands)
