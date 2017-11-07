Title: Minor version 2.3.2 released
Date: 2006-08-09 12:13
Author: aurelio
Category: Releases
Slug: minor-version-232-released
Status: published

Summary: New commented block mark and several bug fixes.

This release introduces a new mark for commented blocks: %%%. The syntax
is similar to the Verbatim and Raw blocks, using the same mark to open
and close the block. Kudos to Leo Rosa for sending the patch!

        This is a paragraph.

        %%%
        This is a commented block.
        Remember that the %%% must be at the line
        beginning with no leading spaces.
        %%%

        Another paragraph.

The txt2tags test suite was extended from 120 to 144 tests! Those new
checks revealed very catchy bugs and some strange behavior. Even fatal
errors raised from uncommon markup on the source file.

Now everything is fine. Oh if I had implemented that test suite thing
since the beginning...

### Vanished Bugs

Removed useless \<P\>\</P\> after Table followed by blank line

        $ echo -e "\n| Table\n" | txt2tags-2.3 -t html -H -o- -i-
        <TABLE CELLPADDING="4">
        <TR>
        <TD>Table</TD>
        </TR>
        </TABLE>
        
        <P></P>
        
        $ echo -e "\n| Table\n" | txt2tags-2.3.2 -t html -H -o- -i-
        <TABLE CELLPADDING="4">
        <TR>
        <TD>Table</TD>
        </TR>
        </TABLE>

Raw doesn't close Quote anymore

        $ echo -e '\n\tQuote\n""" Raw' | txt2tags-2.3 -t html -H -o- -i-
                <BLOCKQUOTE>
                Quote
                </BLOCKQUOTE>
        Raw
        
        $ echo -e '\n\tQuote\n""" Raw' | txt2tags-2.3.2 -t html -H -o- -i-
                <BLOCKQUOTE>
                Quote
        Raw
                </BLOCKQUOTE>

Bugfix: Macro at line beginning now closes Quote

        $ echo -e "\n\tQuote\n%%date" | txt2tags-2.3 -t html -H -o- -i-
                <BLOCKQUOTE>
                Quote
                20060809
                </BLOCKQUOTE>
        
        $ echo -e "\n\tQuote\n%%date" | txt2tags-2.3.2 -t html -H -o- -i-
                <BLOCKQUOTE>
                Quote
                </BLOCKQUOTE>
        <P>
        20060809
        </P>

Bugfix: Verbatim and Raw areas are now mutually exclusive

        $ echo -e '\n```\n"""\nRaw in Verb\n"""\n```' | txt2tags-2.3 -t html -H -o- -i-
        <PRE>
        </PRE>
        Raw in Verb
        <PRE>
        </PRE>
        
        $ echo -e '\n```\n"""\nRaw in Verb\n"""\n```' | txt2tags-2.3.2 -t html -H -o- -i-
        <PRE>
          """
          Raw in Verb
          """
        </PRE>

Bugfix: Fatal error on macro after table

        $ echo -e "\n| x |\n%%date" | txt2tags-2.3 -t html -H -o- -i-
        Sorry! Txt2tags aborted by an unknown error.
        
        $ echo -e "\n| x |\n%%date" | txt2tags-2.3.2 -t html -H -o- -i-
        <TABLE CELLPADDING="4" BORDER="1">
        <TR>
        <TD>x</TD>
        </TR>
        </TABLE>
        
        <P>
        20060809
        </P>

Bugfix: Fatal error on table inside deflist

        $ echo -e "\n: | Table inside List Term" | txt2tags-2.3 -t html -H -o- -i-
        Sorry! Txt2tags aborted by an unknown error.
        
        $ echo -e "\n: | Table inside List Term" | txt2tags-2.3.2 -t html -H -o- -i-
        <DL>
        <DT>| Table inside List Term</DT><DD>
        </DL>

Bugfix: Fatal error on empty table

        $ echo -e "\n| |" | txt2tags-2.3 -t html -H -o- -i-
        Sorry! Txt2tags aborted by an unknown error.
        
        $ echo -e "\n| |" | txt2tags-2.3.2 -t html -H -o- -i-
        <TABLE CELLPADDING="4" BORDER="1">
        <TR>
        <TD></TD>
        </TR>
        </TABLE>

Get the new code at the [download
page](http://txt2tags.sf.net/download.html), under the Minor Releases
section.
