use std::env;
mod converter;

fn main() 
{
    for arg in env::args().skip(1)
    {
        let number: i32 = String::from(arg).parse().expect("Couldn't convert.");
        converter::check_input_number(number);
    }
}
