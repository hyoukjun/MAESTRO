# Announcement about our new repository 
Files in this repository is deprecated, and MAESTRO source code is now available in a new repository: https://github.com/georgia-tech-synergy-lab/MAESTRO

# MAESTRO
MAESTRO is a cost-benefit model to evaluate dataflows over a general accelerator architecture. It receives dataflow and architecture description and provides buffer access counts, which can be integrated with energy models to produce energy consumption, roofline performance, which is throughput with full compute unit utilization, buffer size requirement, network-on-chip bandwidth requirement, and so on. We are currently validating the model. Until it finishes, we only distribute binary executables. For usages, please see our tutorial slides.

# Layer Dimension Description
![convention](https://hyoukjunblog.files.wordpress.com/2018/06/cnn-1.png)

We are using the convention described in the image above. (C/K: Input/Output channel, Y/X: Input Row/Column, and R/S: Weight Row/Column)

![vgg16_conv1_description](https://hyoukjunblog.files.wordpress.com/2018/06/maestro_layerdescription.png)

In layerDecription directories, you will see example layer description files. The file contents look like the example above (vgg16_conv1.m).

# Related Materials
[Paper](https://arxiv.org/abs/1805.02566),[Tutorial Slides](http://synergy.ece.gatech.edu/wp-content/uploads/sites/332/2018/06/02_2018_05_MaestroDataflowAnalysis.pdf)
