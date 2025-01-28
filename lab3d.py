#!/usr/bin/env python3
'''Lab 3d - free_space function to check disk space on the root directory'''
# Author ID: syoskorn

import subprocess

def free_space():
    """Function to return the free disk space on the system's root directory"""
    # The command uses df to display disk space, grep to filter for root '/', and awk to print the fourth column which is available space
    command = "df -h | grep '/$' | awk '{print $4}'"
    # Execute the command
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()

    if process.returncode != 0:
        return "Error: " + error.decode('utf-8').strip()

    return output.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())
