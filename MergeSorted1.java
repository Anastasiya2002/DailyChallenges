import java.util.ArrayList;
public class MergeSorted1 {
    public static void main(String[] args)
	{
	   ArrayList<Integer> a = new ArrayList<Integer>();
	   ArrayList<Integer> b = new ArrayList<Integer>();
	      
	   int i;

	   // Initialize array list a to some values
	   for (i = 0; i < 5; i++)  
	   { 
	      a.add((i + 1) * (i + 1));
	   }

	   // Initialize array list b to some values
	   b.add(4);
	   b.add(7);
	   b.add(9);
	   b.add(11);
	   b.add(14);

	   ArrayList<Integer> c = mergeSorted(a, b);
	   
	   System.out.println("EXPECTED:") ;
       System.out.println("1 4 4 7 9 9 11 14 16 25");

	   for (i = 0; i < c.size(); i++)
	   {
	      System.out.print(c.get(i) + " ");
	   }
	} 

	public static ArrayList<Integer> mergeSorted(ArrayList<Integer> a,ArrayList<Integer> b)
	{
	   //-----------Start below here. To do: approximate lines of code = 22
	   //  Start here
       // NOTE: you are *not* allowed to use Collections.sort()!!!!
       ArrayList<Integer> c = new ArrayList<Integer>();
       for(int k = 0; k< a.size(); k++){
           if(c.size()== 0){
              c.add(a.get(k));
           }
           else if(a.get(k)< c.get(0)){
              c.add(0,a.get(k));
           }
           else{
               c.add(a.get(k));
           }
       }
       for(int i = 0; i<b.size();i++){
           for(int j=0; j<c.size();j++){
               if(b.get(i)<= c.get(j)&& b.get(i)> c.get(j-1)){
                   c.add(j,b.get(i));
               }
           }
       }
       return c;
	
    }
}