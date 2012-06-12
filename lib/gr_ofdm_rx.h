/* -*- c++ -*- */
/*
 * Copyright 2004 Free Software Foundation, Inc.
 * 
 * This file is part of GNU Radio
 * 
 * GNU Radio is free software; you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation; either version 3, or (at your option)
 * any later version.
 * 
 * GNU Radio is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 * 
 * You should have received a copy of the GNU General Public License
 * along with GNU Radio; see the file COPYING.  If not, write to
 * the Free Software Foundation, Inc., 51 Franklin Street,
 * Boston, MA 02110-1301, USA.
 */
#ifndef INCLUDED_GR_OFDM_RX_H
#define INCLUDED_GR_OFDM_RX_H

#include <gr_block.h>
#include <gr_msg_queue.h>
#include <gr_complex.h>
#include <gri_fft.h>
class gr_ofdm_rx;

/*
 * We use boost::shared_ptr's instead of raw pointers for all access
 * to gr_blocks (and many other data structures).  The shared_ptr gets
 * us transparent reference counting, which greatly simplifies storage
 * management issues.  This is especially helpful in our hybrid
 * C++ / Python system.
 *
 * See http://www.boost.org/libs/smart_ptr/smart_ptr.htm
 *
 * As a convention, the _sptr suffix indicates a boost::shared_ptr
 */
typedef boost::shared_ptr<gr_ofdm_rx> gr_ofdm_rx_sptr;

/*!
 * \brief Return a shared_ptr to a new instance of howto_square_ff.
 *
 * To avoid accidental use of raw pointers, howto_square_ff's
 * constructor is private.  howto_make_square_ff is the public
 * interface for creating new instances.
 */
gr_ofdm_rx_sptr gr_make_ofdm_rx(unsigned int Nrx=1, gr_msg_queue_sptr outQ=gr_msg_queue_sptr() );

/*!
 * \brief square a stream of floats.
 * \ingroup block
 *
 * \sa howto_square2_ff for a version that subclasses gr_sync_block.
 */
class gr_ofdm_rx: public gr_block {
private:
	// The friend declaration allows howto_make_square_ff to
	// access the private constructor.

	friend gr_ofdm_rx_sptr gr_make_ofdm_rx(unsigned int Nrx, gr_msg_queue_sptr outQ );

	gr_ofdm_rx(unsigned int Nrx=1, gr_msg_queue_sptr outQ=gr_msg_queue_sptr() );

public:
	~gr_ofdm_rx(); // public destructor

	// Where all the action really happens

	int general_work(int noutput_items, gr_vector_int &ninput_items,
			gr_vector_const_void_star &input_items,
			gr_vector_void_star &output_items);

	gr_msg_queue_sptr outputQ() {
		return d_outputQ;
	}
	int input_required();
	unsigned int state() const { return d_state;}
	unsigned int nrx() const { return d_nrx;}
	void crc4(char *info, int len, char * crc) ;

	void set_state(const unsigned int s) { d_state = (state_t) s; }

	int listen( const gr_complex* in, const int n, bool &trigger);
	int call_rxheader(gr_complex in[], int ninputs, bool &success);
	int call_rxdata(gr_complex* in,  int ninputs);
	float sqr(float x) {return (x * x); }
	void viterbiDecode(long channel_length,char *channel_output_vector, 
	char *decoder_output_matrix); 

	void generate_data_parameters();
	void BPSKdemod(gr_complex *fft_data, float * soft_bits);

	





private:
	

	enum state_t {
		INIT, 
		LISTEN,
      	RXHEADER,
      	RXDATA
	};
	state_t d_state;
	gr_msg_queue_sptr d_outputQ;
	gr_message_sptr d_msg;
	unsigned int d_nMCS;
	unsigned int d_nlength_data;
	unsigned int d_ncount_ext_lft;
	float d_cfo;

	unsigned int d_Nfft;
	unsigned int d_Nofdm;
	unsigned int d_Ngi;
	unsigned int d_Nst;
	unsigned int d_nrx;
	unsigned int d_nreq_data;
	unsigned int d_Nsd;

	//Data info
	unsigned int d_data_mod;
	float d_data_rate_coding;
	unsigned int d_data_nsubcarrier;
	unsigned int d_ncrc_bits;


	bool d_header_crc_ok;
	bool d_data_crc_ok;
	gr_complex channel_estimate_block[64];



	
	gri_fft_complex *d_fft;

};

#endif /* INCLUDED_HOWTO_SQUARE_FF_H */
