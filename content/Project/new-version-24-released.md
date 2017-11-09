Title: txt2tags 2.4 released
Date: 2006-12-24 10:36
Author: aurelio
Category: Project
Slug: new-version-24-released
Status: published

Day 24, version 2.4. Got it? :)

Take all the dust and spiders out of your current txt2tags installation
and upgrade to the [fresh new stylish Christmas
release](http://txt2tags.sf.net/download.html).

Tons of bug fixes, new mark to comment multiple lines, more than one CSS
per HTML file and user-defined .sty files for LaTeX are some of the
news. [Read them all](http://txt2tags.sf.net/changelog.html).

Example of the new features:

    My Test File
    John Doe
    Dec/2006

    % Multiple CSS files are now supported
    % They're applied on the same order you specify them
    %
    %!style(html): site.css
    %!style(html): ie-gotchas.css
    %!style(html): xmas-theme.css

    % Now you can use your own LaTeX goodness
    %
    %!style(tex): ~/.mylatexrules.sty
    %!style(tex): tex/mystyles/MathSettings.sty

    Hello World

    %%%
    This is a commented block.
    Three percentages to open, three more to close.
    These lines won't appear on the converted file, they're commented.
    %%%

    Goodbye World

> Yes, we're growing!  
>  No, we're not bloat!
