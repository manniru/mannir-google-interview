package​ ​com.google.challenges;​ ​

import java.util.*;

public class Answer {

	static int[][] p = new int[201][201];

	public static void fillP() {
		p[1][1] = 1;
		p[2][2] = 1;

		for (int w = 3; w < 201 ; w++) {
			for (int m = 1; m <= w; m++) {
				if (w-m == 0) {

					p[w][m] = 1 + p[w][m-1];

				} else if (w-m < m) {

					p[w][m] =  p[w-m][w-m] + p[w][m-1];

				} else if (w-m == m) {
					p[w][m] = p[m][m-1] + p[w][m-1];

				} else if (w-m >m) {

					p[w][m] = p[w-m][m-1] + p[w][m-1];
				}

			}
		}
	}

	public static int answer(int n) {

		fillP();
		return p[n][n] - 1;

	}

}
