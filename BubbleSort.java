public class BubbleSort {
    
    public static void bubbleSort(int[] arr) {
        int n = arr.length;
        // 外层循环控制排序轮数
        for (int i = 0; i < n - 1; i++) {
            // 内层循环进行相邻元素比较
            // 每轮排序后，最大的元素会"冒泡"到末尾，所以范围逐渐缩小
            for (int j = 0; j < n - 1 - i; j++) {
                // 如果前一个元素大于后一个元素，则交换它们
                if (arr[j] > arr[j + 1]) {
                    // 交换元素
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;
                }
            }
        }
    }
    
    // 打印数组的方法
    public static void printArray(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
        System.out.println();
    }
    
    // 主方法，用于测试冒泡排序
    public static void main(String[] args) {
        int[] arr = {64, 34, 25, 12, 22, 11, 90};
        
        System.out.println("排序前的数组:");
        printArray(arr);
        
        bubbleSort(arr);
        
        System.out.println("排序后的数组:");
        printArray(arr);
    }
}