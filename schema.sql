-- Just the track table from Swinsian
CREATE TABLE track (
    track_id INTEGER PRIMARY KEY,
    title TEXT,
    artist TEXT,
    album TEXT,
    genre TEXT,
    composer TEXT,
    year INTEGER,
    tracknumber INTEGER,
    discnumber INTEGER,
    bitrate INTEGER,
    bitdepth INTEGER,
    samplerate INTEGER,
    channels INTEGER,
    length FLOAT,
    dateadded FLOAT,
    lastplayed FLOAT,
    playcount INTEGER,
    rating INTEGER,
    filesize INTEGER,
    enabled INTEGER,
    cue INTEGER,
    gapless INTEGER,
    compilation INTEGER,
    encoder TEXT,
    path TEXT,
    filename TEXT,
    comment TEXT,
    properties_id INTEGER,
    albumartist TEXT,
    totaldiscnumber INTEGER,
    datecreated FLOAT,
    grouping TEXT,
    bpm INTEGER,
    publisher TEXT,
    totaltracknumber INTEGER,
    description TEXT,
    datemodified FLOAT,
    catalognumber TEXT,
    conductor TEXT,
    discsubtitle TEXT,
    lyrics TEXT,
    copyright TEXT
);
