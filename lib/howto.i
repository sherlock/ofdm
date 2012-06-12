/* -*- c++ -*- */

%include "gnuradio.i"			// the common stuff

%{
#include "howto_square_ff.h"
#include "howto_square2_ff.h"
#include "gr_ofdm_tx.h"
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
GR_SWIG_BLOCK_MAGIC(howto,square_ff);

howto_square_ff_sptr howto_make_square_ff ();

class howto_square_ff : public gr_block
{
private:
  howto_square_ff ();
};

// ----------------------------------------------------------------

GR_SWIG_BLOCK_MAGIC(howto,square2_ff);

howto_square2_ff_sptr howto_make_square2_ff ();

class howto_square2_ff : public gr_sync_block
{
private:
  howto_square2_ff ();
};

// ----------------------------------------------------------------

GR_SWIG_BLOCK_MAGIC(gr,ofdm_tx);

gr_ofdm_tx_sptr gr_make_ofdm_tx (unsigned int MCS=0,  unsigned int inputQ_limit=1);

class gr_ofdm_tx : public gr_block
{
private:
   gr_ofdm_tx(unsigned int MCS=0,  unsigned int inputQ_limit=1);
public:
    gr_msg_queue_sptr  msgq();
};



// ----------------------------------------------------------------

GR_SWIG_BLOCK_MAGIC(gr,ofdm_rx);
gr_ofdm_rx_sptr gr_make_ofdm_rx(unsigned int Nrx=1, gr_msg_queue_sptr outQ=gr_msg_queue_sptr() );


class gr_ofdm_rx: public gr_block 
{

private:
	gr_ofdm_rx(unsigned int Nrx=1, gr_msg_queue_sptr outQ=gr_msg_queue_sptr() );
public:
	gr_msg_queue_sptr outputQ();
};
	
