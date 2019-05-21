use raindrops::raindrops;


fn main() {
    //let n = 4;
    //println!("what sound does Raindrop #{} make?", n);
    //raindrops(n);
    //println!("{}", raindrops(n));

    let rainstorm = [
        1, 3, 5, 7, 9, 15, 21, 25, 27, 35, 45, 49, 63, 75, 81, 105, 125, 135, 147, 175, 189, 225,
        243, 245, 315, 343, 375, 405, 441, 525, 567, 625, 675, 729, 735, 875, 945, 1029, 1125,
        1215, 1225, 1323, 1575, 1701, 1715, 1875, 2025, 2187, 2205, 2401, 2625, 2835, 3087, 3125,
    ];
    for elem in rainstorm.iter() {
        println!("Raindrop {} makes a {} sound", elem, raindrops(*elem)); // borrow elem from rainstorm
    }
}
