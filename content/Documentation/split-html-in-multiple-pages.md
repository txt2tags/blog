Title: Using HTMLDOC to split HTML in multiple pages
Date: 2006-08-31 15:28
Author: aurelio
Category: Documentation
Slug: split-html-in-multiple-pages
Status: published

You have that really big HTML page that takes forever to load on the
browser? What about to break it in smaller pieces, one topic per page?
The [HTMLDOC tool](http://htmldoc.org) can make it for you.

The main purpose of this tool is to do the opposite: join multiple HTML
files into one single PDF file. It has a huge list of options, so you
have strong control over the process, like setting fonts, header and
footer, automatic Table of Contents, insert a cover page and more.

> The [txt2tags User Guide
> PDF](http://txt2tags.sf.net/userguide/userguide.pdf) is generated from
> a big HTML file by HTMLDOC.

The latest version comes with a new target called "htmlsep", that takes
an structured HTML page (full of \<H1\>, \<H2\>) and breaks it into
multiple pages. This is the command line usage:

    htmldoc -t htmlsep -o output-folder file.html

Note that it's required that you create a folder for the generated
files, before running the command. Let's break some files? Here's a
quick sample HTML file with some headings:

    <html>
    <body>
    <h1>Greatest Bands Ever</h1>
      <h2>Punk Rock</h2>
      RAMONES.
      <h2>Softcore</h2>
      Millencolin, No Fun At All, No Use For A Name, ...
      <h2>Other</h2>
      Toy Dolls, Operation Ivy, Face to Face, ...

    <h1>Greatest Movies Ever</h1>
      <h2>Documentary</h2>
      Dogtown And Z-Boys, Riding Giants, Step Into Liquid, ...
      <h2>Strange</h2>
      Cube

    </body>
    </html>

Follow me:

    $ ls -F
    greatest.html  output/

    $ htmldoc -t htmlsep -d output greatest.html 
    BYTES: 715
    BYTES: 1135
    BYTES: 883
    BYTES: 1024
    BYTES: 1030
    BYTES: 1059
    BYTES: 998
    BYTES: 1074
    BYTES: 896

    $

Before that command, we've had just the HTML file and an empty folder.
When running HTMLDOC it shows those "BYTES" lines to inform you
everything is OK. Now, let's check what we have on the output folder:

    $ ls output/
    Documentary.html        Other.html              Strange.html
    GreatestBandsEver.html  PunkRock.html           index.html
    GreatestMoviesEver.html Softcore.html           toc.html

Great! Each heading went to its own file, named accordingly. The extra
files are "index.html" and "toc.html", that holds the cover page and the
Table of Contents. All the pages have the following navigation links:
Contents, Previous, Next, so you can browse them in a sequence.

Handy, simple and fast.

You may play with other options to customize the files:

    $ htmldoc -t htmlsep -d output \  
       --no-title --toclevels 2 --toctitle "Contents" \  
       greatest.html 

Remember that big old User Guide in HTML that has hanging around on the
txt2tags site? Now it is [separated in multiple
files](http://txt2tags.sf.net/userguide/). If you prefer the all-in-one
version, download the PDF (see About topic).

> **Note 1:** HTMLDOC has no support for CSS. You'll have to add the
> \<link\> tag to the generated files.

> **Note 2:** HTMLDOC reads the file data since the first heading. Use a
> %!postproc to remove the \<H1\>Page Title\</H1\> line when converting
> to HTML.

> **Note 3:** Download HTMLDOC from
> [www.htmldoc.org](http://www.htmldoc.org), which is the free Open
> Source version. If you're in Linux search for "htmldoc" in your
> package manager. On the Mac you can find it on Fink, or download and
> compile the sources (it's quick). Windows users may have to install
> the commercial demo from [Easy
> Software](http://www.easysw.com/htmldoc/).
