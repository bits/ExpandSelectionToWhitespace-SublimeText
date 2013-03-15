Expand Selection to Whitespace
==============================

#### A [Sublime Text](http://www.sublimetext.com/) plugin that helps you go faster

Expand selection to touch up against the closest space, tab, newline, or Unicode spacing character surrounding the cursor(s) or selection(s).

Sublime Text's "Expand Selection to Word" (first press of <kbd>Ctrl+D</kbd> / <kbd>⌘D</kbd>) is a really fast way to select the word you're on.  But sometimes you want more than the simple word, you want everything up to the space before and after where you are.  Now you can do that.

Bound by default to <kbd>Ctrl+Shift+X</kbd> on Windows and Linux, and <kbd>⇧⌘X</kbd> on Mac. 

#### It turns out this is really handy

* **Quickly lazy-select text** — Select partway into the first and last words and hit the shortcut.  This gives you much larger targets for the start and end of your selection, so you don't have to go slowly and precisely to get the pointer or cursor right at the tiny sweet spot.  It's surprising what a difference this makes.
* **Paths**: /home/user/project/awesome ← Place the cursor anywhere in the path and get the whole thing with a keystroke
* **Filenames**: access_log-2099-12-31.tbz2
* **URLs**: https://github.com/bits/ExpandSelectionToWhitespace-SublimeText
* **Some coding styles**: self.expand\_region\_to\_whitespace(region)
* When you made a selection, but missed the first few characters — **grab them instead of repeating yourself**
* Selecting **vertically aligned text** or a column — Perform a narrow [column selection](http://www.sublimetext.com/docs/2/column_selection.html) <kbd>Ctrl+Alt+Up</kbd>/<kbd>Down</kbd> on Windows/Linux, <kbd>Ctrl+Shift+Up</kbd>/<kbd>Down</kbd> on Mac and widen each line's selection out to the whitespace with a flick of the fingers

You'll find "Expand Selection to Whitespace" ready to do your bidding in the Selection menu, the Command Palette, and via key binding.

### Use a different key binding

The plugin supplies the `expand_selection_to_whitespace` command, which you can bind to your preferred keyboard shortcut in your `Preferences → Key Bindings – User` file by adding something like:

	{ "keys": ["ctrl+shift+x"], "command": "expand_selection_to_whitespace" }



Install using Package Control
-------------------------------------------

With the [Package Control plugin](http://wbond.net/sublime_packages/package_control) installed:

1. Bring up the **Command Palette** with <kbd>Control+Shift+P</kbd> on Windows and Linux or <kbd>⇧⌘P</kbd> on Mac.
2. Select **"Package Control: Install Package"**, and wait while Package Control fetches the latest package list.
3. Select **"Expand Selection to Whitespace"** when the list appears.

When you use the Package Control plugin to install a plugin, it is automatically updated when a new version is available.


Install manually
----------------

To install a Sublime Text 2 plugin, place the plugin's directory into Sublime Text's "Packages" directory.  Find yours with `Sublime Text → Preferences → Browse Packages`.  The default location varies by operating system:

* Windows: `%APPDATA%/Sublime Text 2/Packages/`
* OS X: `~/Library/Application Support/Sublime Text 2/Packages/`
* Linux: `~/.config/sublime-text-2/Packages/`

Get this plugin via git or by downloading and extracting the zip archive:

#### Install by cloning the git repository
Clone the repository right into your Sublime Text "Packages" directory:

 	git clone https://github.com/bits/ExpandSelectionToWhitespace-SublimeText.git "Expand Selection To Whitespace"

To later update to the latest:,`git pull origin master` from within the "Packages/Expand Selection To Whitespace" directory.

#### Install by downloading and extracting source archive
Download the [latest zip archive](https://github.com/bits/ExpandSelectionToWhitespace-SublimeText/archive/master.zip), unzip, optionally rename the directory, and copy the directory into your Sublime Text "Packages" directory.

Repeat this procedure in the future to update to the latest version.


Contact
-------

If there are any problems or you have a suggestion, please [open an issue](https://github.com/bits/ExpandSelectionToWhitespace-SublimeText/issues/new), and I'll receive a notification.  You may also want to see any previously [reported issues and suggestions](https://github.com/bits/ExpandSelectionToWhitespace-SublimeText/issues) on the [Expand Selection to Whitespace repo on github](https://github.com/bits/ExpandSelectionToWhitespace-SublimeText)



MIT License
-----------

Copyright © 2013 Paul Sarena

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
