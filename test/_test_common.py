import os
import sys

wren_tag_dir = os.path.join(os.path.dirname(__file__), '..')
sys.path.insert(0, os.path.join(wren_tag_dir))
import wren_tag


sample_dir = os.path.join(wren_tag_dir, 'sample')
sample_files = [
    os.path.join(sample_dir, '440Hz.aac'),
    os.path.join(sample_dir, '440Hz.aiff'),
    os.path.join(sample_dir, '440Hz.dsf'),
    os.path.join(sample_dir, '440Hz.flac'),
    os.path.join(sample_dir, '440Hz.m4a'),
    os.path.join(sample_dir, '440Hz.mp3'),
    os.path.join(sample_dir, '440Hz.ogg'),
    os.path.join(sample_dir, '440Hz.opus'),
    os.path.join(sample_dir, '440Hz.wv'),
]

with open(os.path.join(sample_dir, 'cover.jpg'), 'rb') as fin:
    sample_artwork = fin.read()

sample_tags = {
    'tracktitle': '440Hz',
    'artist': 'Maths',
    'album': 'Source of Sound',
    'albumartist': 'Various Artists',
    'composer': 'Fourier',
    'tracknumber': 1,
    'totaltracks': 1,
    'discnumber': '',
    'totaldiscs': '',
    'genre': 'Analytic',
    'year': 2019,
    'compilation': True,
    # 'lyrics': "And malt does more than Milton can.To justify God's ways to man.",
    'comment': 'sin(2 * pi * 440 * t)',
    'artwork': sample_artwork,
}

def check_tags(f, rel_fname, tags):
    for key, val in tags.items():
        if key == 'artwork':
            assert f[key].first.data == val, 'bad artowrk read'
        else:
            err_msg = "{0}:: '{1}' : {2} != {3}:".format(rel_fname, key, f[key],
                                                         val)
            assert str(f[key]) == str(val), err_msg
