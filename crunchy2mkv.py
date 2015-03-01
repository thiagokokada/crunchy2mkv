#!/usr/bin/env python

"""crunchy2mkv.py

Download .flv videos from Crunchyroll (and maybe other sites) and
convert them to .mkv.

Needs youtube-dl and mkvmerge (from mkvtoolnix) installed and
accessible from PATH (or you can change global variables YTDL_PATH and
MKVMERGE_PATH to point to your installation path).

No configuration files. You can change the default behavior of this
script by changing the following global variables:

    RESULT_PATH: default directory for resulting videos
    USERNAME: username from Crunchyroll (or other video services)
    PASSWORD: same for password
    QUALITY: default video quality
    SUBS: comma-separated string including each desired language for
    subtitles. Use "all" to download everything.

Should be compatible with both Python 2.7+ and Python 3.2+.

"""

from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

import argparse
import atexit
import glob
import os
import sys
import shutil
from distutils.spawn import find_executable
from subprocess import call, check_call, CalledProcessError
from tempfile import mkdtemp

# Dependencies path
YTDL_PATH = find_executable("youtube-dl") # /usr/bin/youtube-dl, youtube-dl.exe
MKVMERGE_PATH = find_executable("mkvmerge") # /usr/bin/mkvmerge, mkvmerge.exe
if not YTDL_PATH:
    sys.exit("Could not find youtube-dl installed.")
if not MKVMERGE_PATH:
    sys.exit("Could not find mkvmerge installed.")

# You can set your desired preferences here
RESULT_PATH = "."
VERBOSE = False
USERNAME = None
PASSWORD = None
QUALITY = "best" # worst, 360p, 480p, 720p, 1080p, best
SUBS = "all"
# SUBS = "en,pt"
# SUBS = None

# Don't change these settings unless you know what you're doing!
_SUPPORTED_EXTENSIONS = ["flv", "mp4", "ogg", "webm"]
_DEVNULL = open(os.devnull, "wb")


def youtube_dl(url, username = None, password = None, quality = "best",
               subs = "all", verbose = False):
    """Simple youtube-dl wrapper

    url -- Video url to download
    username (default = None) -- username to be passed to "--username"
    option in youtube-dl
    password (default = None) -- password to be passed to "--password"
    option in youtube-dl
    quality (default = "best") -- quality to be passed to "--quality"
    option in youtube-dl
    subs (default = "all") -- subtitle(s) language to download. If
    "all" is used the, option "--all-subs" is passed to youtube-dl,
    otherwise the passed string is passed to "--subs-lang" option
    in youtube-dl, without any checks. If None is passed, this
    option is ignored.
    verbose -- show youtube-dl output in stdout/stderr
    
    """
    # Basic command line
    cmd = [YTDL_PATH, "-f", quality, "--ignore-config"]
    
    # Added login information
    if username:
        cmd.append("--username")
        cmd.append(username)
    if password:
        cmd.append("--password")
        cmd.append(password)
    
    # Added subtitle preference
    if subs:
        if subs == "all":
            cmd.append("--all-subs")
        else:
            cmd.append("--sub-lang")
            cmd.append(subs)

    # Added video URL
    cmd.append(url)

    # Try to download video
    print("Trying to download video from URL {}.".format(url))
    try:
        if verbose:
            print("Running command: {}".format(" ".join(cmd)))
            check_call(cmd)
        else:
            check_call(cmd, stderr = _DEVNULL, stdout = _DEVNULL)
    except CalledProcessError:
        sys.exit("Error while downloading URL {}. Exiting...".format(url))

def video2mkv(file_path, result_path, verbose = False):
    """Simple mkvmerge wrapper to convert videos to .mkv

    file_path -- target video to be converted to .mkv
    result_path -- directory for resulting files in .mkv
    verbose -- show mkvmerge output in stdout/stderr

    """
    # Basic command line
    cmd = [MKVMERGE_PATH]
    
    # Split filename and extension
    filename, extension = os.path.splitext(file_path)
    
    # Find all files with the same filename, independent of the extension
    for media in glob.glob("{}.*".format(filename)):
        # Added them to .mkv
        cmd.append(media)
    
    # Added output file
    result_filename = os.path.join(result_path, filename)
    cmd.append("-o")
    cmd.append("{}.mkv".format(result_filename))
    
    # Try to create .mkv file
    print("Trying to create {}.mkv.".format(result_filename))
    try:
        if verbose:
            print("Running command: {}".format(" ".join(cmd)))
            check_call(cmd)
        else:
            check_call(cmd, stderr = _DEVNULL, stdout = _DEVNULL)
    except CalledProcessError:
        sys.exit("Error while creating {} file. Exiting..."
                 .format(result_filename))

    return "{}.mkv".format(result_filename)

def clean_up(directory = ".", verbose = False):
    if verbose:
        print("Cleaning up {} directory.".format(directory), file = sys.stderr)
    directory = os.path.abspath(directory)
    shutil.rmtree(directory)

def _argparser():
    parser = argparse.ArgumentParser(description = "Download videos from "
                                     "Crunchyroll (and maybe other sites) "
                                     "and convert them to .mkv.")
    parser.add_argument("url",  nargs = "+", help = "Video URL to download")
    parser.add_argument("-r", "--result", metavar = "PATH", action = "store",
                        default = RESULT_PATH, help = "path to result directory")
    parser.add_argument("-u", "--username", action = "store", default = USERNAME,
                        help = "account username")
    parser.add_argument("-p", "--password", action = "store", default = PASSWORD,
                        help = "account password")
    parser.add_argument("-q", "--quality", action = "store", default = QUALITY,
                        help = "video quality")
    parser.add_argument("-s", "--subs", metavar = "LANG", action = "store",
                        default = SUBS, help = "subtitle language(s)")
    parser.add_argument("-v", "--verbose", action = "store_true",
                        default = VERBOSE, help = "show extra information (for debug purposes)")
    parser.add_argument("--version", action = "version", version = "0.1")

    return parser

def main():
    parser = _argparser()
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(2)
    
    args = parser.parse_args()
    result_path = os.path.expanduser(args.result)
    result_path = os.path.abspath(result_path)
    verbose = args.verbose
    username = args.username
    password = args.password
    quality = args.quality
    subs = args.subs

    try:
        for url in args.url:
            tempdir = mkdtemp()
            # Clean up temporary directory at exit
            atexit.register(clean_up, directory = tempdir, verbose = verbose)
            os.chdir(tempdir)
            youtube_dl(url, username, password, quality, subs, verbose)
            for file_ext in _SUPPORTED_EXTENSIONS:
                filename = glob.glob("*.{}".format(file_ext))
                if filename:
                    filename = filename[0]
                    result_filename = video2mkv(filename, result_path, verbose)
                    print("Video {} download succesfully!".
                            format(result_filename))
    except KeyboardInterrupt:
        sys.exit("User canceled operation.")

if __name__ == "__main__":
    main()
