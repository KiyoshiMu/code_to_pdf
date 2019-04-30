import os
import sys
from os.path import join
code_mark = '~~~~~~~~'

def search_code(dir_path:str, suffix:str='.py') -> list:
    yield from [(join(item[0], fn), fn) for item in os.walk(dir_path)
                for fn in item[2] if item[2] and fn[-3:]=='.py']

def code_to_pdf(dir_path, dst):
    htmls_dst = join(dst, 'htmls')
    pdfs_dst = join(dst, 'pdfs')
    os.makedirs(htmls_dst ,exist_ok=True)
    os.makedirs(pdfs_dst, exist_ok=True)
    chrome = '"C:\Program Files (x86)\Google\Chrome\Application\chrome"'
    for code, fn in search_code(dir_path):
        html = join(htmls_dst, fn[:-3]+".html")
        os.system(f'pygmentize -O full,style=emacs -o {html} {code}')
        pdf = join(pdfs_dst, fn[:-3]+'.pdf')
        os.system(f'{chrome} --headless --print-to-pdf={pdf} {html}')

def pandoc_code(dir_path, dst):
    pys_dst = join(dst, 'pys')
    pdfs_dst = join(dst, 'pdfs')
    os.makedirs(pys_dst ,exist_ok=True)
    os.makedirs(pdfs_dst, exist_ok=True)
    for code, fn in search_code(dir_path):
        dst_py = join(pys_dst, fn)
        dst_pdf = join(pdfs_dst, fn[:-3]+'.docx')
        wrap_code(code, dst_py)
        os.system(f'pandoc -s {dst_py} -o {dst_pdf}')

def wrap_code(srt_py, dst_py):
    with open(dst_py, 'w') as out_code:
        with open(srt_py, 'r') as in_code:
            codes = code_mark + '\n' + in_code.read() + '\n' + code_mark
            out_code.write(codes)

if __name__ == "__main__":
    dir_path = sys.argv[1]
    dst = sys.argv[2]
    pandoc_code(dir_path, dst)