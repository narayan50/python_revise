public class PyramidPattern {

    public static void main(String[] args) {
        int rows = 5; // You can change the number of rows here

        // Outer loop for each row
        for (int i = 1; i <= rows; i++) {

            // Inner loop to print leading spaces
            // The number of spaces decreases with each row
            for (int j = 1; j <= rows - i; j++) {
                System.out.print(" ");
            }

            // Inner loop to print stars
            // The number of stars increases by 2 in each row (2*i - 1)
            for (int k = 1; k <= (2 * i - 1); k++) {
                System.out.print("*");
            }

            // Move to the next line after printing stars for the current row
            System.out.println();
        }
    }
}