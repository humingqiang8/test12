public class DateUtils {
    
    /**
     * 获取并返回当前日期和时间的字符串表示。
     * @return 当前日期和时间的字符串。
     */
    public static String getCurrentDateTime() {
        java.time.LocalDateTime now = java.time.LocalDateTime.now();
        return now.toString();
    }

    /**
     * 根据给定的格式获取并返回当前日期和时间的字符串表示。
     * @param pattern 日期时间格式模式 (例如 "yyyy-MM-dd HH:mm:ss")。
     * @return 格式化后的当前日期和时间的字符串。
     */
    public static String getCurrentDateTime(String pattern) {
        java.time.LocalDateTime now = java.time.LocalDateTime.now();
        java.time.format.DateTimeFormatter formatter = java.time.format.DateTimeFormatter.ofPattern(pattern);
        return now.format(formatter);
    }

    // 用于测试的main方法
    public static void main(String[] args) {
        System.out.println("Default format: " + getCurrentDateTime());
        System.out.println("Custom format: " + getCurrentDateTime("yyyy-MM-dd HH:mm:ss"));
    }
}