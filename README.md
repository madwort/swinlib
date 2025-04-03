# SwinLib

Some small tools for messing about with my Swinsian library.

Warning: this code is only lightly tested & comes with absolutely no warranty! If you use this on your actual music library, this may delete all your music, break everything and eat your lunch!

## Features

* automate moving albums to a different disk based on chose parameters
  * backup library before doing any modifications
  * dry-run mode

## TODO

* split `swinlib/database.py` into multiple files
* write some tests
* rewrite dateadded for albums where dateadded order doesn't match the track order!
  * watch out for duplicated albums
