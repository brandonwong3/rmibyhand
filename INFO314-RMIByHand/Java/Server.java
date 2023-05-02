import java.io.*;
import java.net.*;
import java.util.*;

public class Server {

    public static void main(String[] args) {
        try {
            ServerSocket server = new ServerSocket(10314);
            Socket socket = null;

            while((socket = server.accept()) != null) {
                final Socket threadSocket = socket;
                new Thread( () -> handleTCPRequest(threadSocket)).start();
            }
            server.close();
        } catch (Exception err) {
            err.printStackTrace();
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