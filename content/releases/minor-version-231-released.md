Title: Minor version 2.3.1 released
Date: 2006-07-27 23:15
Author: aurelio
Category: Releases
Slug: minor-version-231-released
Status: published

After more than a year of silence, there is a new txt2tags version out!

It's a minor release, mostly related to the Style option (--style or
%!style). Now you can specify two or more CSS files for an HTML/XHTML
page, or modules for LaTeX. Example:

        txt2tags -t html --style main.css --style fancy.css site.t2t

The --css-inside option was also improved to support multiple files and
now warns when the CSS file is not found.

        <!-- Included main.css -->
        <STYLE TYPE="text/css">
        ...
        </STYLE>
        
        <!-- CSS include failed for fancy.css -->

A very ancient bug was fixed. It was introduced on version 0.7 (from
2002!) and remained unnoticed until recently. The automatic adding of
protocol (like http://) was not working for uppercased URLs.

        $ echo -e "\\nWWW.FOO.COM" | txt2tags-2.3 -o- -H -t html -
        <P>
        <A HREF="WWW.FOO.COM">WWW.FOO.COM</A>
        </P>

        $ echo -e "\\nWWW.FOO.COM" | txt2tags-2.3.1 -o- -H -t html -
        <P>
        <A HREF="http://WWW.FOO.COM">WWW.FOO.COM</A>
        </P>

Since nobody noticed the bug before, this fix is invisible :)

Get the new code at the [download
page](http://txt2tags.sf.net/download.html), under the Minor Releases
section.
