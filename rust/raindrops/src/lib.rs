pub fn raindrops(n: u32) -> String {
    let n_divis_by = |fctr| n % fctr == 0;
    let mut rain = String::from("");

    if n_divis_by(3) {
        rain.push_str("Pling");
    }
    if n_divis_by(5) {
        rain.push_str("Plang");
    }
    if n_divis_by(7) {
        rain.push_str("Plong");
    }
    if rain == "" {
        rain = n.to_string();
    }

    rain
}
