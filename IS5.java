import java.math.BigInteger;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class IS5 {
    public static String getMD5(String input) {
        try {
            MessageDigest md = MessageDigest.getInstance("MD5");
            byte[] MessageDigest = md.digest(input.getBytes());
            BigInteger no = new BigInteger(1, MessageDigest);
            String hashSet = no.toString(16);
            while (hashSet.length() < 32) {
                hashSet = "0" + hashSet;
            }
            return hashSet;

        } catch (NoSuchAlgorithmException e) {
            throw new RuntimeException(e);
        }
    }

    public static void main(String[] args) throws NoSuchAlgorithmException {
        String s = "Shri";
        System.out.println(getMD5(s));
    }
}
