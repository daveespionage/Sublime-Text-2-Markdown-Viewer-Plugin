"""
#Markdown Viewer Plugin  
*by David Cox-Espenlaub*  

For documentation of the webbrowser module,
see http://docs.python.org/library/webbrowser.html  

See https://github.com/daveespionage/Sublime-Text-2-Markdown-Viewer-Plugin for more details
"""

import os
import webbrowser
import sublime, sublime_plugin


class ViewMarkdownCommand(sublime_plugin.TextCommand):
    def run(self, view):
    	view = self.view
        settings = sublime.load_settings('View Markdown.sublime-settings')   	
    	sublime.status_message("running ViewMarkdownCommand")
        if (view.file_name() and 
        		os.path.exists(view.file_name()) and 
        		settings.get('markdown_viewer')["url"] != ""):
			new = 2 # open in a new tab, if possible
			mdurl = settings.get('markdown_viewer')["url"]
			extended = settings.get('markdown_viewer')["extended"]
			filename = view.file_name()

			# open the markdown viewer URL with the current view's file
			url = ''.join([mdurl,"?adv=",extended,"&src=",filename])
			webbrowser.open(url,new=new)