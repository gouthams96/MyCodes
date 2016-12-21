public class DecimalToBinaryConverter {

    public static void ConvertToBinary(int n){
        int[] array = new int[128];
        int iter=0;
        while(n>0){
            int num = n % 2;
            array[iter]=num;
            iter++;
            n=n/2;
        }
        System.out.print("Binary is = ");
        while(iter>=1){
            iter--;
            System.out.print(array[iter]);          
        }
       System.out.println();    
    }
    
    public static void main(String[] args) {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
        ConvertToBinary(n);
    }
    
}
