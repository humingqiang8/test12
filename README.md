# Java String Utility Project

This project provides a collection of utility classes for common string and validation operations in Java.

## Project Structure

- `StringUtils.java`: A utility class for various string manipulation tasks.
- `ValidationUtils.java`: A utility class for common data validation checks.
- `DateUtils.java`: A utility class for handling date and time operations.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine.

### Prerequisites

- Java Development Kit (JDK) 8 or higher installed on your system.

### Installation

1. Clone the repository or download the source code files (`StringUtils.java`, `ValidationUtils.java`, and `DateUtils.java`).
2. Open a terminal or command prompt and navigate to the directory containing the files.
3. Compile the Java files:
   ```bash
   javac StringUtils.java ValidationUtils.java DateUtils.java
   ```

### Running the Examples

Each class contains a `main` method demonstrating its functionality.

To run the `StringUtils` example:
```bash
java StringUtils
```

To run the `ValidationUtils` example:
```bash
java ValidationUtils
```

To run the `DateUtils` example:
```bash
java DateUtils
```

## Classes and Methods

### `ValidationUtils`

- `isNotNullOrEmpty(String input)`: Checks if a given string is not `null` and not empty (after trimming whitespace).

### `StringUtils`

- `containsSpecialCharacters(String input)`: Checks if a string contains any characters other than letters, digits, and whitespace.
- `filterSpecialCharacters(String input)`: Removes all characters from a string except letters, digits, and whitespace. It first checks for null/empty input and the presence of special characters.

### `DateUtils`

- `getCurrentDateTime()`: Gets the current date and time as a string in the default format.
- `getCurrentDateTime(String pattern)`: Gets the current date and time as a string formatted according to the provided pattern.

## Example Usage

```java
// Validation
String data = "Some input";
if (ValidationUtils.isNotNullOrEmpty(data)) {
    System.out.println("Data is valid.");
}

// String Filtering
String userInput = "Hello, World! 123 @#$";
String cleanInput = StringUtils.filterSpecialCharacters(userInput);
System.out.println(cleanInput); // Output: "Hello World 123"

// Date and Time
String currentTime = DateUtils.getCurrentDateTime("yyyy-MM-dd HH:mm:ss");
System.out.println("Current Time: " + currentTime);
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.