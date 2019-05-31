import shutil
from os.path import join
from batch_convert import pandoc_code
from concat import concat_docx
import argparse

def main(dir_p, dst_p, suffix, name='codes'):
    pandoc_code(dir_p, dst_p, suffix)
    code_dst = join(dst_p, 'code')
    docx_dst = join(dst_p, 'docx')
    concat_docx(docx_dst, dst_p, suffix, name=name)
    shutil.rmtree(code_dst)
    shutil.rmtree(docx_dst)

if __name__ == "__main__":
    parse = argparse.ArgumentParser(description='convert all codes to a pdf fitting print')
    parse.add_argument('src', help='the dir of your codes')
    parse.add_argument('dst', help='the output dir path')
    parse.add_argument('suffix', help='the suffix of your codes')
    parse.add_argument('-n', '--name', default='codes', help='the name of final pdf')
    command = parse.parse_args()
    main(command.src, command.dst, command.suffix, name=command.name)