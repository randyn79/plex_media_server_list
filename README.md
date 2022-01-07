# plex_media_server_list

### Purpose
I sometimes buy DVD's at thrift stores and load them onto my Plex media server.  I do not always remember what I already own, so I thought it would be useful to have a list that I could access on my phone to check before purchasing.

### About the Script
The script uses os.walk to go through the file system and the output is a CSV file with the filename, parent folder of the file, file size in MB, last modified date and last accessed date.  At this time the script pulls only data using the os module and at this time does not pull any other metadata.  

### Using the Script
The script should be located in the parent folder and will extract for all folders underneath it.  For example, if you have a folder named "Media" that has subfolders of "Movies", "TV Shows" and "Music", it will process all files in "Media" and inside the three subfolders.  At this time, hidden/system files are not filtered out.
