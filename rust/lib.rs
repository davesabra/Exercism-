#[derive(Debug, PartialEq)]
pub enum Error {
    IncompleteNumber,
    Overflow,
}

/// Convert a list of numbers to a stream of bytes encoded with variable length encoding.
pub fn to_bytes(values: &[u32]) -> Vec<u8> {
    
    let mask: u8 = 0b01111111;    // bitwise &ing with this stencil zeros out bit #7 leaving the rest invariant
    
    values.iter().flat_map(|&v| {
	    (0..5).rev().map(|i| {                                           // can handle quintuple bytes
	        let msb: u8 = if i == 0 { 0b00000000 } else { 0b10000000 };
	       
	        (  v >> (i * 7) ) as u8 & mask | msb           // mask off bit #7 and bitwise OR with msb.  B | 0 == 0,  B | 1 == 1
	        
	    })
	    .skip_while(|&x| x == 0x80)
	    .collect::<Vec<_>>()
    })	
    .collect()
}

/// Given a stream of bytes, extract all numbers which are encoded in there.

pub fn from_bytes(bytes: &[u8]) -> Result<Vec<u32>, Error> {
	
    let mask = 0b01111111;
    let msb   =  0b10000000;  // bitwise &ing with this stencil resolves the continuation bit because B & 1 == B,  B & 0 == 0
    let mut chunks: Vec<u32> = Vec::new();
    
    if let Some(byte) = bytes.last() {
        if byte & msb != 0 { return Err(Error::IncompleteNumber) }
    }
    
    for byte in bytes.windows(5) {
        
        if byte[0] > 0x8f   //  if top byte > 1000 1111   (143)
           &&
           // and we otherwise have a well formed vlq -stream
           byte[1..4].iter().all(|&x| x & msb != 0)
           &&
           byte[4] & msb == 0
        {      
             return Err(Error::Overflow)    
        }
    } 
    
    
    bytes.iter().fold(0, |acc, &byte| {
		
        let value = {acc << 7}   | (byte as u32 & mask);    
        
        if byte & msb == 0 {                //      Last octet? 
            chunks.push(value);             //       Then return the running total value
            acc & 0b0                          //       and reset accumulator to 0
        } else {                                    //     Otherwise there's another octet,
            value                                  //      so fold it into the accumulator for left-shift operation next round
        }
    });
   
   Ok(chunks)
}

