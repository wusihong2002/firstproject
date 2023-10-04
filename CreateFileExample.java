import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;

public class CreateFileExample {
    public static void main(String[] args) {
        String fileName = "myfile.txt";
        String content = "This is the content of the file.";

        try {
            Path path = Paths.get(fileName);
            Files.write(path, content.getBytes());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}