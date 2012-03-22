"""
For documentation of the webbrowser module,
see http://docs.python.org/library/webbrowser.html
"""
import os
import webbrowser
import sublime, sublime_plugin

""" 
Plugin requires the following settings in Preferences.sublime-settings
	"markdown_viewer":
	{
		"url":"http://markdown.local/",
		"extended":"True"
	}

* The value of "url" ("http://markdown.local") should be your local url for WolfieZeros PHP Markdown viewer 
(https://github.com/WolfieZero/Markdown-Viewer-PHP)

* The value of "extended" is either "True" or "" depending on whether you want the Markdown Extended support

"""

class ViewMarkdownCommand(sublime_plugin.TextCommand):
	def run(self, view):
		sublime.status_message("running ViewMarkdownCommand")
		if (view.file_name() and 
				os.path.exists(view.file_name()) and 
				view.settings().get('markdown_viewer')["url"] != ""):
			new = 2 # open in a new tab, if possible
			mdurl = view.settings().get('markdown_viewer')["url"]
			extended = view.settings().get('markdown_viewer')["extended"]
			filename = view.file_name()

			# open the markdown viewer URL with the current view's file
			url = ''.join([mdurl,"?adv=",extended,"&src=",filename])
			webbrowser.open(url,new=new)


