r"""Generate a bunch of empty demofiles with date in filename, random extension.

>>> python filenameWithDate 50 t a
= filesWithDateName(howMany=50, pad=True, format_='American')
=> will create <50> random empty files with <padded American format date> in filename.

Nguyen Thanh Hung - hungnt89@gmail.com
hungntgrb"""

from random import choice, randint
import sys


def randomMonth(pad=False):
    """Generate a random month either with padding or not."""
    
    rm = randint(1, 12)
    
    if pad:
        return f"{rm:0>2}"
    else:
        return f"{rm}"


def randomMonthBetween(m1=1, m2=12, pad=False):
    """Generate a random month in a range either with padding or not."""
    
    rm = randint(m1, m2)
    
    if pad:
        return f"{rm:0>2}"
    else:
        return f"{rm}"


def randomDay(pad=False):
    """Generate a random day either with padding or not."""
    
    rd = randint(1, 31)
    
    if pad:
        return f"{rd:0>2}"
    else:
        return f"{rd}"


def randomDayBetween(d1=1, d2=31, pad=False):
    """Generate a random day in a range either with padding or not."""
    rd = randint(d1, d2)
    if pad:
        return f"{rd:0>2}"
    else:
        return f"{rd}"


def randomYear():
    """Generate a random year between 1900 and 2020."""
    
    ry = randint(1900, 2020)
    
    return f"{ry}"


def randomSeparator():
    """A random separator either . - _"""
    
    rs = choice(('.', '-', '_'))
    
    return rs


def randomExtension():
    """Choose a random extension."""
    
    re = choice(('txt','csv','json','html','css','js','py','mp3','mp4','docx','xlsx','pptx','yaml','png'))
    
    return re


def randomAmericanDate(pad=False):
    """Generate a random American format date MM-DD-YYYY either with padding or not."""
    
    rs = randomSeparator()

    rm = randomMonth(pad)
    rd = randomDay(pad)

    ry = randomYear()
    
    ad = f"{rm}{rs}{rd}{rs}{ry}"

    return ad


def randomEuropeanDate(pad=False):
    """Generate a random European format date DD-MM-YYYY either with padding or not."""
    
    rs = randomSeparator()
    
    rm = randomMonth(pad)
    rd = randomDay(pad)

    ry = randomYear()
    
    ed = f"{rd}{rs}{rm}{rs}{ry}"

    return ed


def randomFilenameWithDate(pad=False, format_='European'):
    """Generate a random filename with either padded or non-padded
'American' or 'European' format date."""

    if format_ == 'European':
        rD = randomEuropeanDate(pad)
    elif format_ == 'American':
        rD = randomAmericanDate(pad)
  
    rs = randomSeparator()
    fnwoe = choice((f"{rD}{rs}demoFile", f"demo{rs}{rD}{rs}File", f"demoFile{rs}{rD}"))
    re = randomExtension()

    fn = f"{fnwoe}.{re}"

    return fn


def filesWithDateName(howMany=10, pad=True, format_='European'):
    """Generate n files <demoFile.ext> with date in filename."""

    for i in range(howMany):
        fn = randomFilenameWithDate(pad, format_)
        with open(fn, 'wb') as f:
            print(f"Creating {fn}...")

    print('Done.')


if __name__ == "__main__":
    
    a1 = int(sys.argv[1])
    d2 = {'t': True, 'f': False}
    a2 = d2.get(sys.argv[2])
    d3 = {'a': 'American', 'e': 'European'}
    a3 = d3.get(sys.argv[3])

    filesWithDateName(howMany=a1, pad=a2, format_=a3)













    
