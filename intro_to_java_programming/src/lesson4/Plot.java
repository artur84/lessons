package lesson4;

public class Plot
{
    private int width;
    private int length;

    /**
        Constructs a plot of a given size.
        @param width the width of the plot
        @param length the length of the plot
    */
    public Plot(int width, int length)
    {
        this.width = width;
        this.length = length;
    }

	/**
	 * Calculates the number of circular fields that can fit on this plot.
	 */
    public int getNumberOfFields(int radius)
    {
		int total_rows = (int) ((this.length - 2 * radius)
				/ (Math.sqrt(3) * radius) + 1);
		// System.out.printf("total rows: %d\n", total_rows);
		int circlesPerOddRow = this.width / (2 * radius);
		// System.out.printf("circles in odd rows: %d\n", circlesPerOddRow);
		int circlesPerEvenRow = (this.width - radius) / (2 * radius);
		// System.out.printf("circles in even rows: %d\n", circlesPerEvenRow);
        
		int numEvenRows = total_rows / 2;
		// System.out.printf("num even rows: %d\n", numEvenRows);
		int numOddRows = (total_rows + 1) / 2;
		// System.out.printf("num odd rows: %d\n", numOddRows);
		int totalCircles = numOddRows * circlesPerOddRow + numEvenRows
				* circlesPerEvenRow;
        return totalCircles;
    }
}
