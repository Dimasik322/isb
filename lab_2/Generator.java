import java.util.Random;


public class Generator{
    final int ROW_SIZE = 128;

    public void generate_row(){
        Random rnd = new Random();
        for (var i = 0; i < ROW_SIZE; ++i){
            var bit = rnd.nextInt(2);
            System.out.print(bit);
        }
    }

    public static void main(String[] args){
        var generator = new Generator();
        generator.generate_row();
    }
}