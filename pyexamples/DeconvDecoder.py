import sys

sys.path.append('../')
from pycore.tikzeng import *

# defined your arch
arch = [
    to_head('.'),
    to_cor(),
    to_begin(),

    # Input
    to_XInput("x_in", 128, "(0,0,0)", to="(0,0,0)"),

    # residual 1
    to_FC("input1", 128, "(1,0,0)", to="(x_in-east)"),
    to_FCRelu("input1relu", 128, "(1,0,0)", to="(input1-east)"),
    to_Sum("sum1", offset="(1.5,0,0)", to="(input1relu-east)", radius=2.5, opacity=0.6),
    to_FCNorm("norm1", 128, "(1,0,0)", to="(sum1-east)"),

    # residual 1 connections
    to_connection("x_in", "input1"),
    to_connection("input1", "input1relu"),
    to_connection("input1relu", "sum1"),
    to_connection("sum1", "norm1"),
    to_skip("x_in", "sum1", pos_of=4, pos_to=2.6),

    # legend
    to_XInput("legend_x", "", "(0,-3.2,0)", to="(input1relu-south)", caption='X', depth=3),
    to_FC("legend_fc", "", "(1,0,0)", to="(legend_x-east)", caption='Linear', depth=3),
    to_FCRelu("legend_relu", "", "(1,0,0)", to="(legend_fc-east)", caption='ReLu', depth=3),
    to_FCNorm("legend_norm", "", "(1,0,0)", to="(legend_relu-east)", depth=3, caption='LayerNorm'),
    to_Conv("legend_conv", "", "", offset="(2,0,0)", to="(legend_norm-east)", height=3, depth=3, width=1.5, caption='Conv2d'),
    to_ConvSoftMax("legend_bnorm", "", offset="(1.5,0,0)", to="(legend_conv-east)", height=3, depth=3, width=1.5, caption='BatchNorm2d'),
    to_TConv("legend_tconv", "", "", offset="(2.5,0,0)", to="(legend_bnorm-east)", width=1.5, height=3, depth=3, caption='ConvTranspose2d'),

    # residual 2
    to_FC("input2", 1024, "(1.5,0,0)", to="(norm1-east)"),
    to_FC("input3", 1024, "(1,0,0)", to="(input2-east)"),
    to_FCRelu("input3relu", 1024, "(1,0,0)", to="(input3-east)"),
    to_Sum("sum2", offset="(1.5,0,0)", to="(input3relu-east)", radius=2.5, opacity=0.6),
    to_FCNorm("norm2", 1024, "(1,0,0)", to="(sum2-east)"),

    # residual 1 connections
    to_connection("norm1", "input2"),
    to_connection("input2", "input3"),
    to_connection("input3", "input3relu"),
    to_connection("input3relu", "sum2"),
    to_connection("sum2", "norm2"),
    to_skip("input2", "sum2", pos_of=4, pos_to=2.6),

    # FC upscale
    to_FC("input4", 61440, "(1,0,0)", to="(norm2-east)"),
    to_Reshape("reshape", offset="(1.5,0,0)", to="(input4-east)", radius=2.5, opacity=0.6, caption="Reshape"),

    to_connection("norm2", "input4"),
    to_connection("input4", "reshape"),

    # deconv
    to_TConv("reshaped", 10, 512, offset="(1,0,0)", to="(reshape-east)", height=12, depth=10, width=2),

    to_TConv("conv1", "", 256, offset="(1,0,0)", to="(reshaped-east)", height=15, depth=13, width=2),
    to_ConvSoftMax("bnorm1", 20, offset="(0,0,0)", to="(conv1-east)", height=15, depth=13, width=2),

    to_TConv("conv2", "", 128, offset="(1,0,0)", to="(bnorm1-east)", height=18, depth=16, width=2),
    to_ConvSoftMax("bnorm2", 40, offset="(0,0,0)", to="(conv2-east)", height=18, depth=16, width=2),

    to_TConv("conv3", "", 64, offset="(1,0,0)", to="(bnorm2-east)", height=21, depth=19, width=2),
    to_ConvSoftMax("bnorm3", 80, offset="(0,0,0)", to="(conv3-east)", height=21, depth=19, width=2),

    to_TConv("conv4", "", 32, offset="(1,0,0)", to="(bnorm3-east)", height=24, depth=22, width=2),
    to_ConvSoftMax("bnorm4", 160, offset="(0,0,0)", to="(conv4-east)", height=24, depth=22, width=2),

    to_Conv("conv5", 160, 3, offset="(1,0,0)", to="(bnorm4-east)", height=24, depth=22, width=2),

    # deconv connections
    to_connection("reshape", "reshaped"),
    to_connection("reshaped", "conv1"),
    to_connection("bnorm1", "conv2"),
    to_connection("bnorm2", "conv3"),
    to_connection("bnorm3", "conv4"),
    to_connection("bnorm4", "conv5"),

    to_end()
]


def main():
    namefile = str(sys.argv[0]).split('.')[0]
    to_generate(arch, namefile + '.tex')


if __name__ == '__main__':
    main()
