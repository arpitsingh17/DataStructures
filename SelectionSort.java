
public class SelectionSort {
	

	public static void main(String[] arguments){
		int[] args = {1,3,4,7,2,3,8,9};
		for(int i=0; i<args.length; i++){
			for(int j=i+1; j<args.length; j++){
				
				if (args[i] > args[j]){
					int tmp = args[j];
					args[j] = args[i];
					args[i] = tmp;
					
					
				}
			}
		}
		for(int k=0;k<args.length; k++){
			System.out.print(args[k]);
		}
		
	}
	
}
