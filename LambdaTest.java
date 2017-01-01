import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class LambdaTest {

    
    public static void main(String[] args) throws IOException{
        // TODO code application logic here
        System.out.println("Enter the length of Array:");
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int length = Integer.parseInt(br.readLine());
        System.out.println("length"+ length);
        int[] numbers = new int[length];
       // String[] arr = br.readLine().trim().split(" ");
       // int i=0;
        int[] array = Arrays.stream(br.readLine().trim().split(" ")).mapToInt(Integer::parseInt).toArray();
        
        /*for(String s:arr){
            numbers[i] = Integer.parseInt(s);
            i++;
        }*/
        
        System.out.println(Arrays.toString(array));
        System.out.println("");
        for(int num: array){
            System.out.print(num+" ");
        }
    }
}

