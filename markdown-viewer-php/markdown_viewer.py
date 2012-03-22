"""
#Markdown Viewer Plugin  
*by David Cox-Espenlaub*  

For documentation of the webbrowser module,
see http://docs.python.org/library/webbrowser.html  

Plugin has the following settings in View Markdown.sublime-settings  
`
	"markdown_viewer":  
	{  
		"url":"http://markdown.local/",  
		"extended":"True"  
	}  
`
Edit these using the command pallette

* The value of "url" ("http://markdown.local") should be your local url for WolfieZeros PHP Markdown viewer  
    (https://github.com/WolfieZero/Markdown-Viewer-PHP)  

* The value of "extended" is either "True" or "" depending on whether you want the Markdown Extended support

To Execute:  
* From the console (ctrl + `) run  
`	
	view.run_command('view_markdown')
`

* This is the default key binding for all platforms:  
`	
	{ "keys": ["ctrl+alt+m"], "command": "view_markdown" }  
`
    The key binding files can be found in the plugin directory, and modified accordingly.

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