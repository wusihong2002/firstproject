import java.nio.charset.StandardCharsets;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.*;

public class code2 {
    public static void main(String[] args) {
        System.out.printf("%s %tB %<te,%<tY","Due date:",new Date());
        Scanner in = new Scanner(Paths.get("myfile.txt"), StandardCharsets.UTF_8);
    }
}
