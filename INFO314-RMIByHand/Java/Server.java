import java.io.*;
import java.net.*;
import java.util.*;

public class Server {

    public static void main(String[] args) {
        try (ServerSocket server = new ServerSocket(10314)) {
            while (true) {
                try (Socket socket = server.accept();
                     ObjectInputStream inputStream = new ObjectInputStream(socket.getInputStream());
                     ObjectOutputStream outputStream = new ObjectOutputStream(socket.getOutputStream())
                     // Get the remote method object

                ) {
                    RemoteMethod remoteMethod = (RemoteMethod) inputStream.readObject();

                    // We get the items now
                    String methodName = remoteMethod.getMethodName();
                    Object[] arguments = remoteMethod.getArguments();
                    Object result;

                    // Do the operation
                    try {
                        switch (methodName) {
                            case "echo":
                                result = echo((String) arguments[0]);
                                break;
                            case "add":
                                result = add((int) arguments[0], (int) arguments[1]);
                                break;
                            case "divide":
                                result = divide((int) arguments[0], (int) arguments[1]);
                                break;
                            default:
                                throw new NoSuchMethodException("Invalid method name: " + methodName);
                        }
                    } catch (Throwable caughtError) {
                        result = caughtError;
                    }

                    // Output stream

                    outputStream.writeObject(result);
                } catch (IOException | ClassNotFoundException e) {
                    System.err.println("Error: " + e.getMessage());
                }

            }

        } catch (IOException e) {
            System.err.println("Server error: " + e.getMessage());
        }
    }

    public static String echo(String message) { 
        return "You said " + message + "!";
    }
    public static int add(int lhs, int rhs) {
        return lhs + rhs;
    }
    public static int divide(int num, int denom) {
        if (denom == 0)
            throw new ArithmeticException();

        return num / denom;
    }
}