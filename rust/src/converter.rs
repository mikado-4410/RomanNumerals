pub fn check_input_number(input_number: i32) {
    const MIN_ROMAN_NUMERAL: i32 = 1;
    const MAX_ROMAN_NUMERAL: i32 = 3999;
    if MIN_ROMAN_NUMERAL > input_number || input_number > MAX_ROMAN_NUMERAL {
        println!("{:?} is not proper input.", input_number);
        add_arabian_number();
    } else {
        apply_roman_converter(input_number);
    }
}

fn add_arabian_number() {
    println!("PlPlease enter the integer again in the range of 1 to 3999 (Enter 0 to exit).");
    print!("Please enter a value -> ");
    let mut tmp = String::new();
    std::io::stdin()
        .read_line(&mut tmp)
        .expect("Failed to read line.");
    let input_number: i32 = String::from(tmp).parse().expect("Couldn't convert.");

    if input_number != 0 {
        check_input_number(input_number);
    } else {
        std::process::exit(0);
    }
}

fn apply_roman_converter(mut input_number: i32) {
    let mut i: u32 = 0;
    let mut roman_number: String = String::new();
    let corresponding_value1: [i32; 13] = [1000, 90, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1];
    let corresponding_value2 = [
        "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I",
    ];
    //let corresponding_value2: Vec<String> = array.iter().map(|&s| String::from(s)).collect();

    while input_number != 0 {
        while input_number / corresponding_value1[i as usize] != 0 {
            roman_number.push_str(corresponding_value2[i as usize]);
            input_number -= &corresponding_value1[i as usize];
        }
        i += 1;
    }
    println!("{}", roman_number);
}
