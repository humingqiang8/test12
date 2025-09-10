public class ValidationUtils {

    /**
     * 判断一个字符串是否为非空。
     * @param input The input string to be checked.
     * @return true if the string is not null and not empty after trimming, false otherwise.
     */
    public static boolean isNotNullOrEmpty(String input) {
        return input != null && !input.trim().isEmpty();
    }

    // 用于测试的main方法
    public static void main(String[] args) {
        System.out.println("Is null empty? " + isNotNullOrEmpty(null));
        System.out.println("Is empty string empty? " + isNotNullOrEmpty(""));
        System.out.println("Is space string empty? " + isNotNullOrEmpty("   "));
        System.out.println("Is 'Hello' empty? " + isNotNullOrEmpty("Hello"));
    }
}