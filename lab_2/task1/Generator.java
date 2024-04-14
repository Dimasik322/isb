import java.util.Random;
import java.io.*;


public class Generator{
    final int ROW_SIZE = 128;

    public void generate_row(){
        try(FileWriter writer = new FileWriter("java_row.txt", false)){
            Random rnd = new Random();
            for (var i = 0; i < ROW_SIZE; ++i){
                writer.append((char)(rnd.nextInt(2) + '0'));
            }
            writer.flush();
        }
        catch(IOException ex){
            System.out.println(ex.getMessage());
        } 
    }

    public static void main(String[] args){
        var generator = new Generator();
        generator.generate_row();
    }
}