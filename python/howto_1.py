#!/usr/bin/env python
#
# Copyright 2004,2007 Free Software Foundation, Inc.
# 
# This file is part of GNU Radio
# 
# GNU Radio is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 3, or (at your option)
# any later version.
# 
# GNU Radio is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with GNU Radio; see the file COPYING.  If not, write to
# the Free Software Foundation, Inc., 51 Franklin Street,
# Boston, MA 02110-1301, USA.
# 

from gnuradio import gr, gr_unittest
from gnuradio import howto
from hydra.PyHydra import FuncThread
import time
#import howto

def bar(tx):
	time.sleep(1)
	print "bar running"
	pkt = "helloworld"
	print pkt
	msg = gr.message_from_string(pkt)
	print msg
	msg = tx.msgq().insert_tail(msg)
	print "insert"

def result(dst):
	time.sleep(40)
	print "result running"
	#result_data = dst.data()
	#print result_data

        
def main():
	'''
	tb = gr.top_block()
	src_data = (-3, 4, -5.5, 2, 3)
	src = gr.vector_source_f (src_data)
	sqr = howto.square_ff ()
        dst = gr.vector_sink_f ()
        tb.connect (src, sqr)
        tb.connect (sqr, dst)
        tb.run ()
        result_data = dst.data ()
        print result_data
	print '\n'
        
        src_data = (-3, 4, -5.5, 2, 3)
        src = gr.vector_source_f (src_data)
        sqr = howto.square2_ff ()
        dst = gr.vector_sink_f ()
        tb.connect (src, sqr)
        tb.connect (sqr, dst)
        tb.run ()
        result_data = dst.data ()
        print result_data
	
	ofdm_tx = howto.ofdm_tx(0)
	print ofdm_tx	
	'''
	tb = gr.top_block()
	ofdm_tx = howto.ofdm_tx(0, 4)
	#dst = gr.vector_sink_c ()
	dst = gr.file_sink(gr.sizeof_gr_complex, 'outdata.dat')
	tb.connect (ofdm_tx, dst)
	print "connect"
	f = FuncThread(bar, "bar", ofdm_tx)
	f.setDaemon(1)
	f.start()

	g = FuncThread(result, "result", dst)
	g.setDaemon(1)
	g.start()

	tb.run()
	print "run"
	sleep(400)
	'''
	pkt = "helloworld"

	print pkt
	msg = gr.message_from_string(pkt)
	print msg
	ofdm_tx.msgq().insert_tail(msg)
	print "insert"
	result_data = dst.data()
	print result_data
	'''
        
if __name__ == '__main__':
    main()
