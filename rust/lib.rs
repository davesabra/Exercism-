use std::collections::BTreeMap;

pub fn transform(legacy: &BTreeMap<i32, Vec<char>>) -> BTreeMap<char, i32> {
    legacy
        .iter() // extract the data from the legacy storage map
        .flat_map(
            |(&keys, values)|                                                                  // ( &k   ,  v    )   data transform is a tuple crossover   (   v  ,  k    )
                                    values.iter().map(move |c|  (c.to_ascii_lowercase(), keys )),
        )
        .collect() // load the data into the new storage map
}
