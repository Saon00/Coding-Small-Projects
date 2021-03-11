import java.util.Random;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        System.out.println("Guess a number between 1 to 10, You'll get only 3 Chances to Guess");
        int secretNumber = random.nextInt(10) + 1; // 1 to 10
        boolean guessLimit = true;
        int guessCount = 0;

        while (guessLimit) {
            System.out.print("Guess-> ");
            int userNumber = scanner.nextInt();

            if (userNumber == secretNumber) {
                System.out.println("You Win!!!!!!!!!!");
                guessLimit = false;
            } else {
                guessCount++;
                if (guessCount == 3)
                    guessLimit = false;
            }

        }
        if (guessCount == 3)
            System.out.println("You Lose......\nThe Secret number was: "+secretNumber);
    }
}
