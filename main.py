# coding : utf-8
# Author : yuxiang Zeng

import argparse
import time

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--f', type=str)
    args = parser.parse_args()
    root_dir = '/Users/zengyuxiang/Documents/阅读笔记/ZYX-Study-Notes/'
    current_date = time.strftime('%-m.%d ', time.localtime(time.time()))
    filename = root_dir + current_date + args.f + '.md'
    with open(filename, 'w') as f:
        f.writelines(f'# {current_date} {args.f}\n')
        f.writelines(f'* Q：什么领域，什么问题\n')
        f.writelines(f'  * \n')
        f.writelines(f'* Q：作者做了什么\n')
        f.writelines(f'  * \n')
        f.writelines(f'* Q：现有工作是怎么做的，有哪些欠考虑的\n')
        f.writelines(f'  * \n')
        f.writelines(f'* Q：所以作者为什么选择了当前框架做法\n')
        f.writelines(f'  * \n')
        f.writelines(f'* Q：作者在实现框架过程, 遇到了什么挑战\n')
        f.writelines(f'  * \n')
        f.writelines(f'* Q：作者是怎么解决这些挑战的\n')
        f.writelines(f'  * \n')
        f.writelines(f'* Q：其他问题\n')
        f.writelines(f'  * \n')
    print(filename)
    print('Done!')
