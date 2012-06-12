#!/usr/bin/env python

from gnuradio import gr, gr_unittest, gru, usrp
from gnuradio import howto, eng_notation
from hydra.PyHydra import FuncThread
import time
import sys

def main():
	tb = gr.top_block()
	ofdm_rx = howto.ofdm_rx();
        #rs = gr.vector_source_c()
	#rs = gr.file_source(gr.sizeof_gr_complex,'out.dat')
	#rs = gr.file_source(gr.sizeof_gr_complex,'out_origin.dat')
	#rs = gr.file_source(gr.sizeof_gr_complex,'out_channel.dat')
	rs = gr.file_source(gr.sizeof_gr_complex,'out_noise.dat')
	"""
	src = usrp.source_c(0)
	#nchannel
	src.set_nchannels(1)
	sample_rate = 1e6

	ulist = [src]
	print "ulist"
	print ulist
	
	for u in ulist:
		rdecim = int(u.adc_rate() / sample_rate)
		u.set_decim_rate(rdecim)
	sys.stderr.write("the decimate = %d\n"%(rdecim))


	srx1 = usrp.pick_rx_subdevice(src)
	print "srx1="
	print srx1

	subdev = ()
	
	ulist = [src]
	assert len(ulist) == 1
	src = ulist[0]
	src.set_mux( usrp.determine_rx_mux_value(src, srx1))
	subdev += (usrp.selected_subdev(src, srx1), )
	for s in subdev: exec("if not hasattr(s, '_u'): s._u = src")
	for s in subdev: s.set_auto_tr(True)
	
	print "subdev"
	print subdev

	freq = 2400000000.0
	for s in subdev:
		r = usrp.tune(s._u, s.which(), s, freq)
		if r:
			sys.stderr.write("setting frequency of %s :\n"%(str(s)))
			sys.stderr.write(" baseband frequency = %s \n" %(eng_notation.num_to_str(r.baseband_freq)))
			sys.stderr.write(" DUC/DDC offset = %s\n" %(eng_notation.num_to_str(r.dxc_freq)))
		elif not r:
			sys.stderr.write("Unable to set frequency of %s to %g MHz \n"%(str(s), freq/ 1.0e6))

	#g = 40.0
	for s in subdev:
		gain_range = s.gain_range()
		#rx_gain = max(min(g, gain_range[1]), gain_range[0])
		rx_gain = 0.8 * gain_range[1]
		s.set_gain(rx_gain)
	sys.stderr.write("the rx_gain = %d \n " %(rx_gain))
	"""


	#tb.connect(src, ofdm_rx)
	tb.connect(rs, ofdm_rx)
	print 'connect'
	tb.run()

if __name__ == '__main__':
	main()


