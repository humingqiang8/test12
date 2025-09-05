fn reverse_string(s: &str) -> String {
    let mut result = String::with_capacity(s.len());
    for c in s.chars() {
        result.insert(0, c);
    }
    result
}

fn main() {
    let original = "hello";
    let reversed = reverse_string(original);
    println!("Original: {}", original);
    println!("Reversed: {}", reversed);
}