import os
import sys
from os.path import join
code_mark = '~~~~~~~~'

def search_code(dir_path:str, suffix:str='.py') -> list:
    yield from [(join(item[0], fn), fn) for item in os.walk(dir_path)
                for fn in item[2] if item[2] and fn.endswith(suffix)]

def pandoc_code(dir_path, dst, suffix):
    code_dst = join(dst, 'code')
    docx_dst = join(dst, 'docx')
    os.makedirs(code_dst ,exist_ok=True)
    os.makedirs(docx_dst, exist_ok=True)
    for code, fn in search_code(dir_path, suffix=suffix):
        dst_code = join(code_dst, fn)
        dst_docx = join(docx_dst, fn[:-3]+'.docx')
        wrap_code(code, dst_code)
        os.system(f'pandoc -s {dst_code} -o {dst_docx}')

def wrap_code(srt_code, dst_code):
    with open(dst_code, 'w', encoding='utf8') as out_code:
        with open(srt_code, 'r', encoding='utf8') as in_code:
            codes = code_mark + '\n' + in_code.read() + '\n' + code_mark
            out_code.write(codes)

if __name__ == "__main__":
    dir_path = sys.argv[1]
    dst = sys.argv[2]
    pandoc_code(dir_path, dst, sys.argv[3])