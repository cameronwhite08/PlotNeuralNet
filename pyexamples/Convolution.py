import sys

sys.path.append('../')
from pycore.tikzeng import *


def build_pic(add_fill=False, x=0, y=0):
    model = [to_head('.'),
             to_cor(),
             to_begin()]

    if add_fill:
        model.extend([
            to_XInput("fill_right", "", offset="(0,0,0)", to="(0,0,0)", depth=12, width=2, height=14),
            to_TConv("x_in", "", "", offset="(0,0,0)", to="(fill_right-west)", height=12, depth=10, width=2),
            to_FC("filt_begin", "", offset=f"(-.3,.8-{.366*y},.1-{.36*x})", to="(x_in-west)", height=3, depth=3, width=2),
            to_TConv("conv1", "", "", offset="(2,0,0)", to="(x_in-east)", height=6, depth=5, width=5),
            to_FC("filt_end", "", offset=f"(0,.5-{.166 * y},.42-{.164 * x})", to="(conv1-west)", height=1, depth=1, width=5)
        ])
    else:
        model.extend([
            to_TConv("x_in", "", "", offset="(0,0,0)", to="(0,0,0)", height=12, depth=10, width=2),
            to_FC("filt_begin", "", offset=f"(-.3,.6-{.3*y},-.05-{.29*x})", to="(x_in-west)", height=3, depth=3,width=2),
            to_TConv("conv1", "", "", offset="(2,0,0)", to="(x_in-east)", height=5, depth=4, width=5),
            to_FC("filt_end", "", offset=f"(0,.4-{.133 * y},.32-{.128 * x})", to="(conv1-west)", height=1, depth=1, width=5)
        ])

    model.append(to_dash('filt_begin', 'filt_end'))
    model.append(to_end())
    return model


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    arch = build_pic(add_fill=True, x=0, y=0)
    to_generate(arch, namefile + '.tex')


if __name__ == '__main__':
    main()
