
#[derive(Eq, PartialEq, Debug)]
pub enum Comparison {
    Equal,
    Sublist,
    Superlist,
    Unequal,
}

pub fn sublist<T>(  first_list: &[T],   second_list: &[T])  -> Comparison
    where T:  PartialEq                                                       
{
                    
		if first_list == second_list {
		         Comparison::Equal
        } else if is_contained(first_list, second_list) {
                 Comparison::Sublist
        } else if is_contained(second_list, first_list) {
                 Comparison::Superlist
        } else {
                 Comparison::Unequal
        }
}

fn is_contained<T>(contained: &[T], container: &[T]) -> bool
             where T: PartialEq 
 {     
		         contained.is_empty() ||  
		         
		         container.windows(contained.len())
		                       .any( |x| x == contained )                       
  }

