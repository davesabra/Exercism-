pub fn annotate(minefield: &[&str]) -> Vec<String> {
    if minefield.is_empty() {
        return vec![];
    }

    if minefield[0].is_empty() {
        let s = String::new();
        return vec![s];
    }

    annotate_field(minefield)
}

fn annotate_field(field: &[&str]) -> Vec<String> {
    let labeled_arr = scan_field(field);

    let matrix = labeled_arr.chunks(field[0].len()).collect::<Vec<_>>();

    let mut out: Vec<String> = Vec::with_capacity(field.len());

    for elem in matrix.iter() {
        let merged: String = elem.iter().collect();
        out.push(merged);
    }
    out
}

fn scan_field(field: &[&str]) -> Vec<char> {
    fn first_char(s: String) -> char {
        s.chars().next().unwrap()
    }

    let mut out: Vec<char> = Vec::with_capacity(field.len());

    for row in 0..field.len() as u32 {
        for col in 0..field[0].len() as u32 {
            let idx = get_index(field, row, col);

            match detect_mines(field)[idx] {
                1 => out.push('*'),
                0 => {
                    let mine_count = count_mines(field, row as usize, col as usize);

                    match mine_count {
                        0 => out.push(' '),
                        _ => out.push(first_char(mine_count.to_string())),
                    };
                }
                _ => continue,
            };
        }
    }

    out
}

fn get_index(field: &[&str], row: u32, col: u32) -> usize {
    let width = field[0].len() as u32;
    let height = field.len() as u32;

    if row < height && col < width {
        (row * width + col) as usize
    } else {
        panic!("IndexOutOfBounds")
    }
}

// converts the field into a vector of 0s and 1s
fn detect_mines(field: &[&str]) -> Vec<u8> {
    fn resolve_space_or_mine(b: &u8) -> u8 {
        assert!(*b == b' ' || *b == b'*');
        ((b & 0x0f) >> 3) as u8
    }

    field
        .iter()
        .flat_map(|row| row.as_bytes())
        .map(resolve_space_or_mine)
        .collect()
}

fn count_mines(field: &[&str], row: usize, col: usize) -> usize {
    let width = field[0].len();
    let height = field.len();

    // boundary conds
    let col_max: usize = if col + 1 >= width { width } else { col + 2 };

    let col_min: usize = if col >= 1 { col - 1 } else { 0 };

    let row_min: usize = if row >= 1 { row - 1 } else { 0 };

    (row_min..row + 2)
        .filter(|&row| row < height)
        .fold(0, |count, line| {
            count
                + field[line][col_min..col_max]
                    .chars()
                    .filter(|&elem| elem == '*')
                    .count()
        })
}
