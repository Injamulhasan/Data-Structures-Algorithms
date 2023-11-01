public class CircularArray{
  
  private int start;
  private int size;
  private Object [] cir;
  
  /*
   * if Object [] lin = {10, 20, 30, 40, null}
   * then, CircularArray(lin, 2, 4) will generate
   * Object [] cir = {40, null, 10, 20, 30}
   */
  public CircularArray(Object [] lin, int st, int sz){
    //TO DO
  }
  
  //Prints from index --> 0 to cir.length-1
  public void printFullLinear(){
        //TO DO
  }
  
  // Starts Printing from index start. Prints a total of size elements
  public void printForward(){
    //To DO
  }
  
  
  public void printBackward(){
   //TO DO
  }
  
  // With no null cells
  public void linearize(){
    //TO DO
  }
  
  // Do not change the Start index
  public void resizeStartUnchanged(int newcapacity){
    //TO DO
  }
  
  
  
  //This method will check whether the array is palindrome or not
  public void palindromeCheck(){
    //TO DO
  }
  
  
  //This method will sort the values by keeping the start unchanged
  public void sort(){
    //TO DO
  }
  
  //This method will check the given array across the base array and if they are equivalent interms of values return true, or else return false
  public boolean equivalent(CircularArray k){
    //TO DO
    return false; // Remove this line
  }

  //This the method take another circular array and returns a linear array containing the common elements between the two circular arrays.
  public int[] intersection(CircularArray c2) {
    // TO DO
    return null; // Remove this line
  }
}