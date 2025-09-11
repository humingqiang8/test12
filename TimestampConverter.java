public class TimestampConverter {

    public static void main(String[] args) {
        // Example usage
        long timestamp = System.currentTimeMillis();
        String formattedDate = convertTimestampToDate(timestamp);
        System.out.println("Timestamp: " + timestamp);
        System.out.println("Formatted Date: " + formattedDate);
    }

    /**
     * Converts a Unix timestamp (in milliseconds) to a formatted date string.
     * @param timestamp The Unix timestamp in milliseconds.
     * @return A formatted date string in the pattern "yyyy-MM-dd HH:mm:ss".
     */
    public static String convertTimestampToDate(long timestamp) {
        // Create a Date object from the timestamp
        java.util.Date date = new java.util.Date(timestamp);

        // Create a SimpleDateFormat object with the desired format
        java.text.SimpleDateFormat formatter = new java.text.SimpleDateFormat("yyyy-MM-dd HH:mm:ss");

        // Format the date and return it as a string
        return formatter.format(date);
    }
}