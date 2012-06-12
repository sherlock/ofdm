/* -*- c++ -*- */

%include "gnuradio.i"			// the common stuff

%{
#include "gr_ofdm_rx.h"

%}

// ----------------------------------------------------------------

/*
 * First arg is the package prefix.
 * Second arg is the name of the class minus the prefix.
 *
 * This does some behind-the-scenes magic so we can
 * access howto_square_ff from python as howto.square_ff
 */
GR_SWIG_BLOCK_MAGIC(gr,ofdm_rx);

gr_ofdm_rx_sptr gr_make_ofdm_rx(unsigned int Nrx=1, gr_msg_queue_sptr outQ=gr_msg_queue_sptr() );

class gr_ofdm_rx : public gr_block
{
private:
   gr_ofdm_rx(unsigned int Nrx=1, gr_msg_queue_sptr outQ=gr_msg_queue_sptr() ); 
public: 
   gr_msg_queue_sptr outputQ();

};

// ----------------------------------------------------------------

