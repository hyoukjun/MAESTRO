import shutil
import os

layers = ['./layerDescription/vgg16_conv1.m', './layerDescription/vgg16_conv6.m', './layerDescription/vgg16_conv11.m', './layerDescription/pwc_fpe_conv1.m', './layerDescription/pwc_fpe_conv4.m', './layerDescription/pwc_fpe_conv6.m' ]

dataflows = ['./dataflowDescription/nlr.m', './dataflowDescription/ws.m', './dataflowDescription/sd.m', './dataflowDescription/dla.m', './dataflowDescription/prs.m', './dataflowDescription/test.m']
vector_width = ['1', '1', '1', '16', '1']

# bus crossbar 
noc_bw = ['8', '8', '8', '8', '2']
mc_support = ['1', '0', '0', '1', '1']
avg_hops = ['8', '16', '2', '4', '2']
num_pes = ['16', '32', '64']

print 'Starting data processing...'

#for ly in range(0,3):
#	for df in range(0,5):
#		for noc in range(0,1):
for ly in range(0,5):
	for df in range(0,5):
		for noc in range(0,5):
			for npes in range(0,3):
				os.system('./maestro' + ' '+ layers[ly] + ' ' + dataflows[df] + ' ' + vector_width[df] + ' ' + noc_bw[noc] + ' ' + mc_support[noc] + ' ' + avg_hops[noc] + ' ' + num_pes[npes])
