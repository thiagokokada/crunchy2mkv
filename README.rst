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

There is no configuration file! You can change some defaults by changing the following environment variables:

- ``C2M_RESULT_PATH``: set the desired output path (example: ``/home/m45t3r/Videos`` or ``C:\Videos``);
- ``C2M_VERBOSE``: use ``True`` for verbose output, use ``False`` to only print user friendly messages (default);
- ``C2M_USERNAME`` and ``C2M_PASSWORD``: set your username and password;
- ``C2M_QUALITY``: set the desired default quality (some valid options: ``worst``, ``360p``, ``480p``, ``720p``, ``1080p``, ``best``)
- ``C2M_SUBS``: set desired subtitle langauge (valid examples: ``all``, ``en``, ``en,pt``, ``""``)

How to install
~~~~~~~~~~~~~~

You need to have both ``youtube-dl`` and ``mkvmerge`` (part of ``mkvtoolnix``) installed and added somewhere on your PATH. Probably the best way is to use your distribution packages to install this program. Some distribution commands to install both:

::

    $ sudo pacman -S youtube-dl mkvtoolnix-cli # Arch Linux

After that just run ``crunchy2mkv.py`` using the full path, or added it somewhere in your path.

::

    $ /random/path/crunchy2mkv.py -v # or PATH=/random/path:${PATH} crunchy2mkv.py -v

Difference between crunchy2mkv and livedumper
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The main difference between both is that crunchy2mkv uses `youtube-dl`_, while `livedumper`_ uses `livestreamer`_. This makes the behavior between the two slightly different.

For example, in `Crunchyroll`_ livestreamer emulates the PS3 API, that brings high quality videos using the HLS protocol. Using this protocol makes Crunchyroll send hardcoded subtitles (i.e. encoded with the video). For instance, youtube-dl hacks the available Flash Video player to get the audio/video/subtitles. The Crunchyroll's Flash Video player are actually special since they support a encrypt version of Advance Substation Alpha subtitles, so the result are softsub videos that can even include subtitles from different languages.

crunchy2mkv is very simple: it's basically a script that wrappers both ``youtube-dl`` and ``mkvmerge``. It's not as powerfull as livedumper was, but this made the code much simpler and smaller.

About Python versions
~~~~~~~~~~~~~~~~~~~~~

This program should be compatible both with ``Python 2.7.x`` and ``Python 3.2+``, but is only tested in ``Python 3.4.x``. Should something not work, if it's in ``Python 2.7.x`` I may drop support depending if it's too hard to fix (but please report, I will at least take a look on the issue). If it's ``Python 3.2+`` I will treat it as a bug so you can report and I will try to fix it.


Credits
~~~~~~~

This project is based on `youtube-dl`_ and `mkvtoolnix`_ projects. Thanks!

.. _`youtube-dl`: https://rg3.github.io/youtube-dl/
.. _`many more`: https://rg3.github.io/youtube-dl/supportedsites.html
.. _`mkvtoolnix`: https://www.bunkus.org/videotools/mkvtoolnix/
.. _`livedumper`: https://github.com/m45t3r/livedumper
.. _`livestreamer`: http://docs.livestreamer.io/
.. _`Crunchyroll`: http://www.crunchyroll.com/
