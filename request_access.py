#!/usr/bin/python

"""
Contains function that asks the user for permission to access their file contents. Uses create_file to save the access_token. 
"""

# Defining the libraries used in this file.
import dropbox, os, file_manipulation

# Defining the APP_KEY and APP_SECRET that dropbox needs to use. 
APP_KEY = 'p5atb8rq1pcqdld'# This is retrieved from dropbox apps registration.
APP_SECRET = 'pk6irvp0esa8m36'

# Beginning of the main file function.
flow = dropbox.client.DropboxOAuth2FlowNoRedirect(APP_KEY, APP_SECRET) # Initializes the flow.
authorize_url = flow.start() # Gets the url for the authorization code.x
print '1. Go to: ' + authorize_url
print '2. Click "Allow" (you might have to log in first)'
print '3. Copy the authorization code.'
code = raw_input("Enter the authorization code here: ").strip() # Recovers the code that the user recovered. 
access_token, user_id = flow.finish(code) # Finish creating the access_token.
file_manipulation.write_or_overwrite("access_token", access_token) # This handles the writing of the file in the hard disk.
