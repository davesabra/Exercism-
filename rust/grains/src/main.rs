extern crate separator;
use grains::square;
use grains::total;
use separator::Separatable;

fn main() {
    let n: u32 = 17;

    println!(
        "Grains of rice on square {}: {}",
        n,
        square(n).separated_string()
    );
    println!(
        "Total grains of rice on board: {}",
        total().separated_string()
    );
}
