use clock::Clock;

fn main() {
    println!("Hello World!");
    let clock = Clock::new(0, 0).add_minutes(10);
    assert_eq!(clock.to_string(), "00:10");
    println!("{}", clock);
}

//runtime error, output not matching expectation
