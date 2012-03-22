#Sublime Text 2 Markdown Viewer Plugin

*By David Cox-Espenlaub*

## About

* Uses [WolfieZero's Markdown-Viewer-PHP](https://github.com/WolfieZero/Markdown-Viewer-PHP "Link to GitHub") as configured as a local site (per the project's instructions)

* Tested in [Sublime Text 2 Beta, Build 2190](http://www.sublimetext.com/dev "Link to Sublimetext 2 Dev Builds")

## Settings

* Uses the following settings in 'View Markdown.sublime-settings':  

		"markdown_viewer":  
		{  
			"url":"http://markdown.local/",  
			"extended":"True"  
		}  
		  
* Replace the value for "url" with your local url
* Set "extended" to "" or remove the setting if you only want to use normal Markdown, set to "True" for extended markdown

## To-Do  

* Possibly convert plugin to do on-the-fly markdown conversion using this library: https://github.com/trentm/python-markdown2