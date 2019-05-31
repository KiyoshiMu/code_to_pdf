# A simple converter to tranform your codes to a pdf

## Prerequisite

1. Core [pandoc](https://pandoc.org/)

Make sure it is in you PC environment path.

2. python

Just Google what it is.

3. python-docx

I you are in PRC, please check [here](https://mirrors.ustc.edu.cn/help/pypi.html) to have a better experience while using **pip**.

I recommand you set a new environment. But I know lots of people love mess. Only until they pay for it, they can understand the importance of tidiness.

No matter what, type the following:

    pip install python-docx

4. docxcompose

Type the following:

    pip install docxcompose

## Usage

In the stript dir, in command lime interface, type:

    python code2pdf.py [your codes dir] [dst] [suffix] [-n somename]

Have fun!

More details:

``` python
parse.add_argument('src', help='the dir of your codes')
parse.add_argument('dst', help='the output dir path')
parse.add_argument('suffix', help='the suffix of your codes')
parse.add_argument('-n', '--name', default='codes', help='the name of final pdf')
```

## Development

- [x] Play
- [] Test