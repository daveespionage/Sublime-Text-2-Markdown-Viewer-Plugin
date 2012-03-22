#Sublime Text 2 Markdown Viewer Plugin

*By David Cox-Espenlaub*

* Uses WolfieZero's Markdown-Viewer-PHP as configured as a local site (per the project's instructions)
    https://github.com/WolfieZero/Markdown-Viewer-PHP

* Currently in Alpha, script works from console in Sublime Text 2, but not as a plugin
* Requires the following settings in Preferences.sublime-settings:
    "markdown_viewer":
    {
    	"url":"http://markdown.local/",
    	"extended":"True"
    }
* Replace the value for "url" with your local url
* Set "extended" to "" or remove the setting if you only want to use normal Markdown
