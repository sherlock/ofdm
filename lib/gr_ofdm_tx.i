/* -*- c++ -*- */

%include "gnuradio.i"			// the common stuff

%{
#include "gr_ofdm_tx.h"

%}

// ----------------------------------------------------------------

/*
 * First arg is the package prefix.
 * Second arg is the name of the class minus the prefix.
 *
 * This does some behind-the-scenes magic so we can
 * access howto_square_ff from python as howto.square_ff
 */
GR_SWIG_BLOCK_MAGIC(gr,ofdm_tx);

gr_ofdm_tx_sptr gr_make_ofdm_tx (unsigned int MCS=0);

class gr_ofdm_tx : public gr_block
{
private:
   gr_ofdm_tx(unsigned int MCS);  
public:
    gr_msg_queue_sptr  msgq();
};

// ----------------------------------------------------------------

