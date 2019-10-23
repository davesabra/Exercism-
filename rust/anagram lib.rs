use std::collections::HashSet;
use itertools::Itertools;
use unicode_segmentation::UnicodeSegmentation;


       
 pub fn anagrams_for<'a>(word: &str, possibles: &[&'a str]) -> HashSet<&'a str> {  
	
	 let sort = |stringy: &str| {            
	    let stringy = stringy                        
                      .graphemes(true)
                      .collect::<String>()
                      .to_lowercase();  
                     
         stringy.chars()
                   .sorted()
                   .collect::<String>()
	 };                                                                   
    
     let lower_word = word.to_lowercase();  // pre-computing these avoids performance penalty 
     let sorted_word = &sort(word);             // of re-calculating them every iteration
    
    possibles                                          
        .iter()
        .copied()      
        .filter(|candidate| lower_word != candidate.to_lowercase()  )    
        .filter(|candidate| *sorted_word == sort(candidate))   
        .collect()	
 }
              

 
    
