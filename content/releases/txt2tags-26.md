Title: txt2tags 2.6
Date: 2010-11-05 16:00
Author: aurelio
Category: Releases
Slug: txt2tags-26
Status: published

And when you thought [txt2tags](http://txt2tags.org) was hibernating
inside a cold dark cave, guess what? We have a new release! :)

I'm very happy to announce the release of [txt2tags
2.6](http://txt2tags.org/download.html), coming out after more than two
years of development effort in the [txt2tags
SVN](http://svn.txt2tags.org).

Thanks to the [active and ever growing team](http://txt2tags.org/team/),
this is the most feature rich release to date: five new targets, five
new command line options, a new mark for tagged text, a new command to
include CSV files, [updated
documentation](http://txt2tags.org/manpage.html), [more
translations](http://txt2tags.org/docs.html) and tons of bug fixes and
improvements.

New targets:

-   [ASCII Art](http://en.wikipedia.org/wiki/ASCII_art) (-t art)
-   [AsciiDoc](http://en.wikipedia.org/wiki/AsciiDoc) (-t adoc)
-   [Creole 1.0](http://en.wikipedia.org/wiki/Creole_(markup)) (-t
    creole)
-   [DocBook](http://en.wikipedia.org/wiki/DocBook) (-t dbk)
-   [PmWiki](http://en.wikipedia.org/wiki/PmWiki) (-t pmw)

Now counting a total of 18 supported targets, txt2tags is one of the
most versatile text conversion tool out there. To help you remember all
of them, now we have the **`--`targets** option.

    $ txt2tags --targets
    adoc    AsciiDoc document
    art     ASCII Art text
    creole  Creole 1.0 document
    dbk     DocBook document
    doku    DokuWiki page
    gwiki   Google Wiki page
    html    HTML page
    lout    Lout document
    man     UNIX Manual page
    mgp     MagicPoint presentation
    moin    MoinMoin page
    pm6     PageMaker document
    pmw     PmWiki page
    sgml    SGML document
    tex     LaTeX document
    txt     Plain Text
    wiki    Wikipedia page
    xhtml   XHTML page
    $

The new **%!csv** command will read a [CSV
file](http://en.wikipedia.org/wiki/Comma-separated_values) and convert
it to a nice table. This is a quick way to include a large table in your
document if you already have the data in a CSV file. The usage is
simple:

    %!csv: monthly-report.csv

The new **`''`tagged`''`** mark is perfect to satisfy some popular user
requests:

-   How can I insert HTML code in my document?
-   How can I insert LaTeX formulas?

Just put a pair of apostrophes around some text, `''like this''`, and
txt2tags will not touch it. You can insert arbitrary target code, such
as `''<span id=a123>''`marking some text`''</span>''` with HTML tags
inside a paragraph. If you want to add a whole block of code, use the
three apostrophes block:

    '''
    <div id="mynicediv">
      <p style="color:red;">My text.</p>
    </div>
    '''

It's very handy for things like Google Analytics code or YouTube
embedded code in HTML pages. Or formulas in LaTeX. Or advanced wiki
markup. Or… You name it.

How about to show a slide presentation just using your regular terminal?
Now it's possible with the new **`--`slides** option, used by the ASCII
Art target. It breaks your text into pages, repeating the top title if
necessary. You inform the size (lines and columns) with the new
**`--`height** and **`--`width** options. You can even change the
decoration characters with the new **`--`art-chars** option.

    txt2tags -t art --slides --width 80 --height 25 -o - sample.t2t | more

[Check out the ChangeLog](http://txt2tags.org/changelog.html) for a
complete list of all the changes and
[download](http://txt2tags.org/download.html) your shiny new txt2tags!

Oh, this new version requires Python 2.2 or newer. But not Python 3,
because we're not that cool :)
