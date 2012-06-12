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
#import howto

class qa_howto (gr_unittest.TestCase):

    def setUp (self):
        self.tb = gr.top_block ()

    def tearDown (self):
        self.tb = None

    def test_001_square_ff (self):
        src_data = (-3, 4, -5.5, 2, 3)
        expected_result = (9, 16, 30.25, 4, 9)
        src = gr.vector_source_f (src_data)
        sqr = howto.square_ff ()
        dst = gr.vector_sink_f ()
        self.tb.connect (src, sqr)
        self.tb.connect (sqr, dst)
        self.tb.run ()
        result_data = dst.data ()
        self.assertFloatTuplesAlmostEqual (expected_result, result_data, 6)

    def test_002_square2_ff (self):
        src_data = (-3, 4, -5.5, 2, 3)
        expected_result = (9, 16, 30.25, 4, 9)
        src = gr.vector_source_f (src_data)
        sqr = howto.square2_ff ()
        dst = gr.vector_sink_f ()
        self.tb.connect (src, sqr)
        self.tb.connect (sqr, dst)
        self.tb.run ()
        result_data = dst.data ()
        self.assertFloatTuplesAlmostEqual (expected_result, result_data, 6)
        
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
	dst = gr.vector_sink_c ()
	tb.connect (ofdm_tx, dst)
	print "connect"
	tb.run()
	print "run"
	pkt = "helloworld"

	print pkt
	msg = gr.message_from_string(pkt)
	print msg
	ofdm_tx.msgq().insert_tail(msg)
	print "insert"
	result_data = dst.data()
	print result_data

        
if __name__ == '__main__':
    main()
