#[derive(PartialEq, Eq)]
pub enum Spacer {
    Add,
}

fn transpose<'a>(plain: &'a str) -> impl Iterator<Item = char> + 'a {
    plain.chars()
         .filter(|c| !c.is_whitespace())
         .filter(char::is_ascii_alphanumeric)
         .map(|c| c.to_ascii_lowercase())
         .map(|c| { if c.is_ascii_alphabetic() {
                        ((b'a' + b'z') - (c as u8)) as char
                  } else {
                    c
                  }
          })                          
}
/*
fn chunk_ref_str(s: &str, n: usize) -> String {   
    let mut chars = s.chars();
    let whole_string = (0..)
        .map(|_| chars.by_ref().take(n).collect::<String>())
        .take_while(|s| !s.is_empty())
        .collect::<Vec<_>>();   
    
    let chunked = whole_string.iter()
          .fold(String::new(), |acc, block| acc + " " + &block);  
          // unfortunately this fold retains a leading whitespace
    {&*chunked.trim_start()}.to_string()
}
*/

fn chunk(s: &str, space_handler: Spacer) -> String {
    
    let mut out = String::new();
    for (i,c) in s.chars().enumerate(){
        if space_handler == Spacer::Add &&
                                    i > 0 &&
                                    i % 5 == 0 {
                                        out.push(' ');
                                    }
        out.push(c);
         }
    out    
}
pub fn encode(plain: &str) -> String {
    let encoded = transpose(&plain).collect::<String>();  // collect FromIterator to String
    //chunk_ref_str(&encoded[..], 5)   // chunking the whole string ( slice)into blocks of 5
    chunk(&*encoded, Spacer::Add)
}

pub fn decode(cipher: &str) -> String {
    transpose(&cipher).collect::<String>()
}
