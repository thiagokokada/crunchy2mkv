crunchy2mkv
===========

Download .flv videos from Crunchyroll (and maybe other sites) and convert them to .mkv.
---------------------------------------------------------------------------------------


Introduction
~~~~~~~~~~~~

This program downloads videos from various video sites like Crunchyroll, Dailymotion, NicoNico, YouTube, and `many more`_, converting them to .mkv format afterwards (without reencoding the video). It uses the `youtube-dl`_ and mkvmerge (from `mkvtoolnix`_) for this purpose.

To run this program, you just need to call it like this:

::

    $ crunchy2mkv.py http://www.crunchyroll.com/fatekaleid-liner-prisma-illya/episode-1-illya-grow-up-657285

This will download this video in the highest quality that is possible in the current folder (you can change this passing the ``-r /path/to/folder`` option). You can download multiple files calling the program with multiple URLs. If the service limits videos only for premium users you can pass your login information like this:

::

    $ crunchy2mkv.py -u username -p password http://www.crunchyroll.com/fatekaleid-liner-prisma-illya/episode-1-illya-grow-up-657285

Run like this:

::

    $ crunchy2mkv.py -h

To get a list of all available options.

There is no configuration file! You can change some defaults by changing variables directly in the source code (nothing to fear, all variables that can be changed are explicit marked in the source).


How to install
~~~~~~~~~~~~~~

You need to have both ``youtube-dl` and ``mkvmerge`` (part of ``mkvtoolnix``) installed and added somewhere on your PATH. Probably the best way is to use your distribution packages to install this program. Some distribution commands to install both:

::

    $ sudo pacman -S youtube-dl mkvtoolnix-cli # Arch Linux

After that just run ``crunchy2mkv.py`` using the full path, or added it somewhere in your path.

::

    $ /random/path/crunchy2mkv.py -v # or PATH=/random/path:${PATH} crunchy2mkv.py -v


About Python versions
~~~~~~~~~~~~~~~~~~~~~

This program should be compatible both with ``Python 2.7.x`` and ``Python 3.2+``, but is only tested in ``Python 3.4.x``. Should something not work, if it's in ``Python 2.7.x`` I may drop support depending if it's too hard to fix (but please report, I will at least take a look on the issue). If it's ``Python 3.2+`` I will treat it as a bug so you can report and I will try to fix it.


Credits
~~~~~~~

This project is based on `youtube-dl`_ and `mkvtoolnix`_ projects. Thanks!

.. _`youtube-dl`: https://rg3.github.io/youtube-dl/
.. _`many more`: https://rg3.github.io/youtube-dl/supportedsites.html
.. _`mkvtoolnix`: https://www.bunkus.org/videotools/mkvtoolnix/
