/*
pub fn reply(message: &str) -> &str {
    // clear front and end whitespaces
    let message = message.trim();
    // patternise message
    let is_question: bool = message.ends_with("?");
    let is_shouted: bool =
        message.chars().any(char::is_uppercase) 
           && !message.chars().any(char::is_lowercase); 
    
    
// match message pattern to Bob's replies
    match message.is_empty() {
        true  => "Fine. Be that way!",
        false => match (is_question, is_shouted) {
            (true, true)   => "Calm down, I know what I'm doing!",
            (false, true)  => "Whoa, chill out!",
            (true, false)  => "Sure.",
            (false, false) => "Whatever.",
                  }
    }
}

*/





