import sys

sys.path.append('../')
from pycore.tikzeng import *


def build_pic(add_fill=False):
    model = [to_head('.'),
             to_cor(),
             to_begin()]

    if add_fill:
        model.extend(
            [to_XInput("fill_right", "", offset="(0,0,0)", to="(0,0,0)", depth=2, width=2, height=14),
             to_XInput("fill_bottom", "", offset="(-.1,.2,1.45)", to="(fill_right-south)", depth=10, width=2, height=1),
             to_TConv("x_in", "", "", offset="(0,.2,1.5)", to="(fill_right-near)", height=12, depth=10, width=2),
             to_XInput("fill_top", "", offset="(-.3,0,-.25)", to="(x_in-north)", depth=10, width=2, height=1),
             to_XInput("fill_left", "", offset="(-.3,-.1,-.05)", to="(x_in-near)", depth=2, width=2, height=14)]
        )
    else:
        model.append(to_TConv("x_in", "", "", offset="(0,0,0)", to="(0,0,0)", height=12, depth=10, width=2))

    model.append(to_XInput("filt", "", offset="(2,0,0)", to="(x_in-east)", height=2, depth=2, width=4))
    model.append(to_TConv("conv1", "", "", offset="(2,0,0)", to="(x_in-east)", height=9, depth=7, width=4))
    model.append(to_precise_dash('x_in', 'filt', with_fill=add_fill))
    model.append(to_end())
    return model


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    arch = build_pic(add_fill=False)
    to_generate(arch, namefile + '.tex')


if __name__ == '__main__':
    main()
