Title: Python script to use HTMLDOC with UTF-8 files
Date: 2008-06-27 22:42
Author: aurelio
Category: Tools
Slug: python-script-to-use-htmldoc-with-utf-8-files
Status: published

You know, [HTMLDOC](http://www.htmldoc.org/) is a good tool to
complement [txt2tags](http://txt2tags.sourceforge.net) features,
specially to [break an HTML file into multiple
pages](/2006/08/31/split-html-in-multiple-pages/).

But the current version of HTMLDOC (1.8.x) [has no Unicode
support](http://www.easysw.com/htmldoc/faq.php?27#27).

When you try to use it to convert or split an UTF-8 file, all the
special characters (not ASCII) will be incorrect in the resulting HTML.

The Unicode support [will be released on the 1.9
version](http://www.htmldoc.org/articles.php?L28+T+P0+Q), which is still
in beta stage.

If you can't wait for the stable 1.9 release or are stuck into an old
version and just want a **quick solution** to your messed files, try my
Python script:  

[fix-htmldoc-utf8.py](http://aurelio.net/bin/python/fix-htmldoc-utf8.py)

It restores the original UTF-8 characters that HTMLDOC has messed.

You can use it as a filter (reads STDIN, results to STDOUT):

    cat myfile.html | fix-htmldoc-utf8 > myfile-ok.html

You can inform the file and send the results to STDOUT:

    fix-htmldoc-utf8 myfile.html > myfile-ok.html

Or you can use the `-w` option fix the file in place:

    fix-htmldoc-utf8 -w myfile.html

Enjoy!
