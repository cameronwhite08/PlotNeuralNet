import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
from pycore.tikzeng import *

def build_pic(add_fill=False, x=0, y=0):
    model = [to_head('../..'),
             to_cor(),
             to_begin()]

    if add_fill:
        model.extend([
            to_XInput("fill_right", "3", "14", "12", offset="(0,0,0)", to="(0,0,0)", depth=12, width=2, height=14),
            to_TConv("x_in", "", "", "", offset="(0,0,0)", to="(fill_right-west)", height=12, depth=10, width=2),
            to_FC("filt_begin", "", offset=f"(-.3,.8-{.44*y},.1-{.45*x})", to="(x_in-west)", height=3, depth=3, width=2),
            to_TConv("conv1", "6", "128", "7", offset="(2,0,0)", to="(x_in-east)", height=7, depth=6, width=5),
            to_FC("filt_end", "", offset=f"(0,.6-{.24 * y},.5-{.25 * x})", to="(conv1-west)", height=1, depth=1, width=5)
        ])
    else:
        model.extend([
            to_TConv("x_in", "10", "3", "12", offset="(0,0,0)", to="(0,0,0)", height=12, depth=10, width=2),
            to_FC("filt_begin", "", offset=f"(-.3,.6-{.36*y},-.05-{.3625*x})", to="(x_in-west)", height=3, depth=3,width=2),
            to_TConv("conv1", "5", "128", "6", offset="(2,0,0)", to="(x_in-east)", height=6, depth=5, width=5),
            to_FC("filt_end", "", offset=f"(0,.5-{.2 * y},.4-{.2 * x})", to="(conv1-west)", height=1, depth=1, width=5)
        ])

    model.append(to_dash('filt_begin', 'filt_end'))
    model.append(to_end())
    return model


def main():
    namefile = str(sys.argv[0]).split('.')[0].split('/')[-1]

    ind = 0
    for y in range(6):
        for x in range(5):
            arch = build_pic(add_fill=False, x=x, y=y)
            filename = f'./outputs/{namefile}-{ind}'
            to_generate(arch, f'{filename}.tex')
            ind += 1


def test():
    namefile = str(sys.argv[0]).split('.')[0].split('/')[-1]

    arch = build_pic(add_fill=False, x=4, y=5)
    filename = f'./outputs/{namefile}'
    to_generate(arch, f'{filename}.tex')


if __name__ == '__main__':
    main()
    # test()
