import java.io.*;
import java.net.*;
import java.util.*;

public class Server {

    public static void main(String[] args) {
        try (ServerSocket server = new ServerSocket(10314)) {
            while (true) {
                Socket socket = server.accept();
                new Thread(() -> handleTCPRequest(socket)).start();

                // Get the input stream
                ObjectInputStream inputStream = new ObjectInputStream(socket.getInputStream());

                // Get the remote method object
                RemoteMethod remoteMethod = (RemoteMethod) inputStream.readObject();

                // We get the items now
                String methodName = remoteMethod.getMethodName();
                Object[] arguments = remoteMethod.getArguments();
                Object[] result = remoteMethod.getResult();

                // Do the operation
                try {
                    switch (methodName) {
                        case "echo":
                            result[0] = echo((String) arguments[0]);
                            break;
                        case "add":
                            result[0] = add((Integer) arguments[0], (Integer) arguments[1]);
                            break;
                        case "divide":
                            result[0] = divide((Integer) arguments[0], (Integer) arguments[1]);
                            break;
                        default:
                            throw new Exception("Invalid method name: " + methodName);
                    }
                } catch (Throwable caughtError) {
                    result = new Object[]{caughtError};
                }

                // Output stream
                ObjectOutputStream outputStream = new ObjectOutputStream(socket.getOutputStream());
                outputStream.writeObject(result);
            }

        } catch (Exception err) {
            System.out.println("Server error: " + err.getMessage());
        }
    }

    public static void handleTCPRequest(Socket socket) {
        try(InputStream fis = socket.getInputStream();
        ObjectInputStream ois = new ObjectInputStream(fis);) {
            
            RemoteMethod obj = (RemoteMethod) ois.readObject();
            Object[] result;

            if(obj.getMethodName().equals("echo")) {
                Object[] args = obj.getArguments();
                obj.result[0] = echo((String)args[0]);
            } else if(obj.getMethodName().equals("add")) {
                Object[] args = obj.getArguments();
                int lhm = (Integer)args[0];
                int rhm = (Integer)args[1];
                obj.result[0] = add(lhm, rhm);
            } else if(obj.getMethodName().equals("divide")) {
                Object[] args = obj.getArguments();
                int num = (Integer)args[0];
                int denom = (Integer)args[1];
                obj.result[0] = divide(num, denom);
            }

            //serialize result
            try (
            OutputStream fos = socket.getOutputStream();
            ObjectOutputStream oos = new ObjectOutputStream(fos);) {
                oos.writeObject(obj);
                oos.flush();

                fos.close();
            } catch (Exception err) {
                err.printStackTrace();
            }
            fis.close();
            socket.close();
        } catch (Exception err) {
            err.printStackTrace();
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