Title: TextMate Txt2tags Bundle
Date: 2007-03-30 11:52
Author: aurelio
Category: Tools
Slug: textmate-txt2tags-bundle
Status: published

If you're one lucky guy/girl that owns a copy of the excellent [TextMate
text editor](http://macromates.com/), listen on and prepare the
"Hooray!".

I'm a recently converted TextMate user and as you may wonder, to edit
txt2tags files is part of my **everyday** routine.
[Websites](http://aurelio.net/en/), articles and books, everything is
[t2t-marked](http://txt2tags.org/markup.html).

For a few days I've used TextMate on the "black & white mode" and that
was real unsexy. A decade of [Vim](http://www.vim.org) hardcore use told
me that syntax highlight is a [Good
Thing](http://en.wikipedia.org/wiki/Good_Thing).

> I'm the Great Cornholio! I need some T.P. for my
> [Bundle](http://macromates.com/wiki/Main/Bundles)!

For my total surprise, the making of the [TextMate Txt2tags
Bundle](https://github.com/textmate/txt2tags.tmbundle) was a breeze.
It's damn easy to add the syntax rules and as the regexes format are
similar to Python's, it was a copy & paste dream.

[![t2tmate
Syntax Highlight](https://txt2tags.files.wordpress.com/2007/03/t2tmate-syntax-highlight.thumbnail.png)](http://txt2tags.files.wordpress.com/2007/03/t2tmate-syntax-highlight.png "t2tmate Syntax Highlight")

Since I was there, I just couldn't stop.

Besides the colors for the txt2tags markup, we also have:

-   **Tab Triggers for all the marks**Just type the mark's character and
    hit Tab. For example, to start a bold sentence, hit "`*`" followed
    by a Tab. It will expand to "`****`", with the cursor right at the
    middle, waiting for your words to be inserted. Very handy!
-   **Keyboard Shortcuts**Still on the bold example, you can select your
    words and press `Command-B`. They'll be surrounded by the "\*\*"
    marks. Quick comment/uncomment a block of lines with `Command-/` and
    move quotation in and out with `Command-]` and `Command-[`.

    To type a link, it's even cooler. First, copy the desired URL to the
    clipboard (`Command-C`, you know). Then type `Control-Shift-L` and
    the link mark will appear, with the URL already filled. Type the
    link name and press Tab to leave the mark. Killer!

    You can also select some already-typed text, press `Control-Shift-L`
    and see it being linked without any typing. The same works for
    titles, images and even tables (just Tab-delimit your data and press
    `Control-Shift-|`).

    Press `Command-Esc` at any time to get the key listing:  
    ![t2tmate
    Keyboard Shortcuts](http://txt2tags.files.wordpress.com/2007/03/t2tmate-keys.png)

    <p>
    Tip: Use keyboard shortcuts for selected text, use tab triggers for
    to-be-typed text.

-   **Tab Triggers for all settings and macros**Never read the [Txt2tags
    User Guide](http://txt2tags.org/userguide/) anymore.
    Just type the setting name followed by a Tab to have all it's
    arguments shown. And what about those [funky "%Y
    %m"](http://txt2tags.org/userguide/date.html#7_1) for
    the %%date macro? No problem, type "date" and hit Tab.
-   **Drag'n'drop support**Images, other txt2tags files and HTML files.
    Just drag them to the editor and watch the magic happening!
-   **Ready-to-use template for UNIX man pages**Load the template, fill
    your program's data and there it is: you have a full featured man
    page. To start, choose
    `File > New From Template > Txt2tags > Manual Page (man)`.
-   **Painless conversion process**There are several shortcuts to
    automate the conversion process and see the results.
    -   Under the "Convert to..." menu you can convert your document to
        any txt2tags-supported format with a single click.
    -   Press `Control-Option-Command-P` (Wow, that hurts to type, but
        it's easy to press) to get an instant clear text-only version of
        your document, just in case the markup is stealing your
        attention.
    -   My favorite: press `Control-Command-P` to convert the file to
        HTML and open it in Safari (or your other default browser). It
        avoids the boring save-convert-switch-reload every time you're
        editing your site pages.

Check out the full bundle menu expanded to finally shout your Hooray!:

[![t2tmate Menu](http://txt2tags.files.wordpress.com/2007/03/t2tmate-menu.png)](http://txt2tags.files.wordpress.com/2007/03/t2tmate-menu.png "t2tmate Menu")

That's it! [Download](https://github.com/textmate/txt2tags.tmbundle) and
double click to install.
