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
#ifndef INCLUDED_GR_OFDM_TX_H
#define INCLUDED_GR_OFDM_TX_H

#include <gr_block.h>
#include <gr_msg_queue.h>
#include <gr_complex.h>
#include <gri_fft.h>
class gr_ofdm_tx;

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
typedef boost::shared_ptr<gr_ofdm_tx> gr_ofdm_tx_sptr;

/*!
 * \brief Return a shared_ptr to a new instance of howto_square_ff.
 *
 * To avoid accidental use of raw pointers, howto_square_ff's
 * constructor is private.  howto_make_square_ff is the public
 * interface for creating new instances.
 */
gr_ofdm_tx_sptr gr_make_ofdm_tx(unsigned int MCS=0, unsigned int inputQ_limit=1);

/*!
 * \brief square a stream of floats.
 * \ingroup block
 *
 * \sa howto_square2_ff for a version that subclasses gr_sync_block.
 */
class gr_ofdm_tx: public gr_block {
private:
	// The friend declaration allows howto_make_square_ff to
	// access the private constructor.

	friend gr_ofdm_tx_sptr gr_make_ofdm_tx(unsigned int MCS,
			unsigned int inputQ_limit);

	gr_ofdm_tx(unsigned int MCS=0, unsigned int inputQ_limit=1); // private constructor

public:
	~gr_ofdm_tx(); // public destructor

	// Where all the action really happens

	int general_work(int noutput_items, gr_vector_int &ninput_items,
			gr_vector_const_void_star &input_items,
			gr_vector_void_star &output_items);

	gr_msg_queue_sptr msgq() {
		return d_inputQ;
	}

private:
	//format the stf
	void format_stf();
	//format the ltf
	void format_lft();
	
	//format the parameter 
	void format_param(unsigned int MCS, unsigned int length_msg, int Ntx);
	void format_data(unsigned int MCS,int Ntx, unsigned int length_msg, unsigned char *msg, gr_complex *out_data_sym);
	void crc4(char *info,int len, char * crc);
	void cnv_encd(int input_len, char *in_array, char *out_array);

	enum state_t {
		INIT, DATA, POSTPAD
	};
	state_t d_state;
	int d_block_size;
	int d_npost;
	int d_postpad;






	gr_msg_queue_sptr d_inputQ;
	gr_message_sptr d_msg;
	unsigned int d_nsamples_written;
	unsigned int d_dataN;
	unsigned int d_MCS;

	unsigned int d_Nfft;
	unsigned int d_Nofdm;
	unsigned int d_Ngi;
	unsigned int d_Nst;

	gr_complex stf_matrix[160];
	gr_complex ltf_matrix[160];
	gr_complex d_param_ofdm[80];
	gri_fft_complex *d_fft;

};

#endif /* INCLUDED_HOWTO_SQUARE_FF_H */
