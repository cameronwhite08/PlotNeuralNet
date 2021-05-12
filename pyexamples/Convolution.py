import sys

sys.path.append('../')
from pycore.tikzeng import *


def build_pic(add_fill=False, x=0, y=0):
    model = [to_head('.'),
             to_cor(),
             to_begin()]

    if add_fill:
        model.extend([
            to_XInput("fill_right", "", offset="(0,0,0)", to="(0,0,0)", depth=2, width=2, height=14),
            to_XInput("fill_bottom", "", offset="(-.1,.2,1.45)", to="(fill_right-south)", depth=10, width=2, height=1),
            to_TConv("x_in", "", "", offset="(0,.2,1.5)", to="(fill_right-near)", height=12, depth=10, width=2),
            to_XInput("fill_top", "", offset="(-.3,0,-.25)", to="(x_in-north)", depth=10, width=2, height=1),
            to_XInput("fill_left", "", offset="(-.3,-.1,-.05)", to="(x_in-near)", depth=2, width=2, height=14),
            to_FC("filt_begin", "", offset=f"(-.3,.8-{.366*y},.3-{.44*x})", to="(x_in-west)", height=3, depth=3, width=2)
        ])
    else:
        model.extend([
            to_TConv("x_in", "", "", offset="(0,0,0)", to="(0,0,0)", height=12, depth=10, width=2),
            to_FC("filt_begin", "", offset=f"(-.3,.6-{.3*y},-.05-{.29*x})", to="(x_in-west)", height=3, depth=3,width=2)
        ])

    model.append(to_TConv("conv1", "", "", offset="(2,0,0)", to="(x_in-east)", height=6, depth=5, width=5))
    model.append(to_FC("filt_end", "", offset=f"(0,.5-{.166*y},.42-{.164*x})", to="(conv1-west)", height=1, depth=1, width=5))
    model.append(to_dash('filt_begin', 'filt_end'))
    model.append(to_end())
    return model


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    arch = build_pic(add_fill=False, x=0, y=0)
    to_generate(arch, namefile + '.tex')


if __name__ == '__main__':
    main()
