pub fn square(s: u32) -> u64 {
    if let 1...64 = s {
        1_u64 << (s - 1) // << operator == 'binary doubling'
    } else {
        panic!("Square must be between 1 and 64")
    }
}

//alternative to square
pub fn square_a(s: u32) -> u64 {
    match s {
        1...64 => 1_u64 << (s - 1),
        _err_ => panic!("Square must be between 1 and 64"),
    }
}

pub fn total() -> u64 {
    let pile: u64 = 18_446_744_073_709_551_615; // sum(2.pow[x]) x=0..x=63, converges -> 2.pow(64) - 1
    pile
}
