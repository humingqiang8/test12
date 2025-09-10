public class StringUtils {

    /**
     * 检查字符串中是否存在特殊字符。
     * @param input The input string to be checked.
     * @return true if special characters are found, false otherwise.
     */
    public static boolean containsSpecialCharacters(String input) {
        if (input == null) {
            return false;
        }
        // 检查是否存在任何非字母、数字和空格的字符
        return input.matches(".*[^a-zA-Z0-9\\s].*");
    }

    /**
     * 过滤字符串中的特殊字符，只保留字母、数字和空格。
     * @param input The input string to be filtered.
     * @return The filtered string.
     */
    public static String filterSpecialCharacters(String input) {
        if (!ValidationUtils.isNotNullOrEmpty(input)) {
            System.out.println("Input string is null or empty. Returning as is.");
            return input;
        }
        // 首先检查是否存在特殊字符
        if (!containsSpecialCharacters(input)) {
            System.out.println("No special characters found. Returning original string.");
            return input; // 如果没有特殊字符，直接返回原字符串
        }
        // 使用正则表达式替换所有非字母、数字和空格的字符
        return input.replaceAll("[^a-zA-Z0-9\\s]", "");
    }

    // 用于测试的main方法
    public static void main(String[] args) {
        String testStr = "Hello, World! 123 @#$%^&*()_+{}|:<>?~`";
        String filteredStr = filterSpecialCharacters(testStr);
        System.out.println("Original: " + testStr);
        System.out.println("Filtered: " + filteredStr);
    }
}