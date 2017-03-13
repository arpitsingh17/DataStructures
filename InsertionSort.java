
public class InsertionSort {
	public static void main(String [] argument){
		int args[] = {9,2,1,4,8,5};
		
		for(int turn=0; turn<args.length-1; turn++){
			for(int i=turn+1; i>0; i--){
				if (args[i] < args[i-1]){
					int tmp = args[i];
					args[i]=args[i-1];
					args[i-1]=tmp;
				}
			}
		}
		for (int j = 0; j < args.length; j++)
			System.out.print(args[j]);
		
	}

}
