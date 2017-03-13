
public class BubbleSort 
{

	public static void main(String[] args1) 
	{
		// TODO Auto-generated method stub
		int args[] = {9,2,1,4,8,5};
		int swapped=1, i, tmp, pass;
		for (pass = args.length - 1; pass >= 0 && swapped == 1; pass--)
		{   swapped = 0;
			for(i=0; i<pass - 1; i++)
			{   
				if (args[i] > args[i+1])
				{
					tmp = args[i];
					args[i] = args[i+1];
					args[i+1] = tmp;
					swapped = 1;
				}
				
		    }
		
			
			
			
			
	    }
		for (int j = 0; j < 5; j++)
		System.out.print(args[j]);
     } 


}


