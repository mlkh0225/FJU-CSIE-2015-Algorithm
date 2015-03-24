import java.util.Scanner;

class Main {
	public static int m_order(int num){
		int diff_order = 0;
		if (num<2) return 1;
		for (int i=1;i<num;i++){
			diff_order = diff_order+m_order(i)*m_order(num-i);}
		return diff_order;}
		public static void main(String[] args) {
			Scanner scanner = new Scanner(System.in);
		int m_number = scanner.nextInt();
		System.out.println(m_order(m_number));}}