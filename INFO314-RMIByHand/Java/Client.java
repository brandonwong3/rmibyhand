// We are writing a Client that will be able to execute a procedure (static method) on a remote server and receive the response.
// This assignment is an example of Remote Procedure Call (RPC).

import java.io.*;
import java.net.*;

public class Client {

    // Simplified caller method
    private static Object rpcCaller(String methodName, Object... args) {
        try (Socket socket = new Socket(server, PORT);
             OutputStream outStream = socket.getOutputStream();
             ObjectOutputStream out = new ObjectOutputStream(outStream);
             InputStream inStream = socket.getInputStream();
             ObjectInputStream in = new ObjectInputStream(inStream)) {

            // Send the method name and arguments to the server
            RemoteMethod temp = new RemoteMethod(methodName, args);
            out.writeObject(temp);

            // Get the result from the server
            Object result = in.readObject();


            // Check if the type of result is an ArithmeticException
            // If so, throw the ArithmeticException

//            if (result instanceof ArithmeticException) {
//                throw new ArithmeticException();
//            }

            // Make sure to throw the ArithmeticException for the division error.
            if (result instanceof Throwable) {
                throw (Throwable) result;
            }
            return result;
        } catch (ArithmeticException arithmeticException) {
            throw arithmeticException;
        } catch (Throwable e) {
            if (e instanceof RuntimeException) {
                throw (RuntimeException) e;
            }
            return null;
        }
    }

    public static int add(int lhs, int rhs) {
        return (int) rpcCaller("add", lhs, rhs);
    }

    public static int divide(int num, int denom) {
        return (int) rpcCaller("divide", num, denom);
    }

    public static String echo(String message) {
        return (String) rpcCaller("echo", message);
    }

    static String server = "localhost";
    public static final int PORT = 10314;

    public static void main(String... args) {
        System.out.print("Test... ");

        if (add(2, 4) == 6)
            System.out.print(".");
        else
            System.out.print("X");

        try {
            divide(1, 0);
            System.out.print("X");
        }
        catch (ArithmeticException x) {
            System.out.print(".");
        }

        if (echo("Hello").equals("You said Hello!"))
            System.out.print(".");
        else
            System.out.print("X");
        System.out.println(" Finished");
    }

}
