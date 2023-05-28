// We are writing a Client that will be able to execute a procedure (static method) on a remote server and receive the response.
// This assignment is an example of Remote Procedure Call (RPC).

import java.io.*;
import java.net.*;

public class Client {
    public static int add(int lhs, int rhs) {
        RemoteMethod add = new RemoteMethod("add", new Object[]{lhs, rhs}, new Object[]{-1});

        try(Socket socket = new Socket("localhost", 10314)) {
            try (
            OutputStream os = socket.getOutputStream();
            ObjectOutputStream oos = new ObjectOutputStream(os);) {
            
                oos.writeObject(add);
                oos.flush();

                try(InputStream fis = socket.getInputStream();
                ObjectInputStream ois = new ObjectInputStream(fis);) {
                    RemoteMethod obj = (RemoteMethod) ois.readObject();

                    Object[] results = obj.getResult();
                    fis.close();
        
                    return (Integer)results[0];
                } catch (Exception err) {
                    err.printStackTrace();
                }
                os.close();
            } catch(IOException ex) {
                ex.printStackTrace();
            }
            socket.close();
        } catch (Exception err) {
            System.out.println("Server not running; Run program to start");
        }

        return -1;
    }

    public static int divide(int num, int denom) {
        RemoteMethod divide = new RemoteMethod("divide", new Object[]{num, denom}, new Object[]{-1});

        try(Socket socket = new Socket("localhost", 10314)) {
            try (
            OutputStream os = socket.getOutputStream();
            ObjectOutputStream oos = new ObjectOutputStream(os);) {
            
                oos.writeObject(divide);
                oos.flush();

                try(InputStream fis = socket.getInputStream();
                ObjectInputStream ois = new ObjectInputStream(fis);) {
                    RemoteMethod obj = (RemoteMethod) ois.readObject();

                    Object[] results = obj.getResult();
                    fis.close();

                    return (Integer)results[0];
                } catch (Exception err) {
                    err.printStackTrace();
                }
                os.close();
            } catch(IOException ex) {
                ex.printStackTrace();
            }
            socket.close();
        } catch (Exception err) {
            System.out.println("Server not running; Run program to start");
        }

        return -1;
    }

    public static String echo(String message) {
        RemoteMethod echo = new RemoteMethod("echo", new Object[]{message}, new Object[]{""});

        try(Socket socket = new Socket("localhost", 10314)) {
            try (
            OutputStream os = socket.getOutputStream();
            ObjectOutputStream oos = new ObjectOutputStream(os);) {
            
                oos.writeObject(echo);
                oos.flush();

                try(InputStream fis = socket.getInputStream();
                ObjectInputStream ois = new ObjectInputStream(fis);) {
                    RemoteMethod obj = (RemoteMethod) ois.readObject();

                    Object[] results = obj.getResult();
                    fis.close();

                    return (String)results[0];
                } catch (Exception err) {
                    err.printStackTrace();
                }
                os.close();
            } catch(IOException ex) {
                ex.printStackTrace();
            }
            socket.close();
        } catch (Exception err) {
            System.out.println("Server not running; Run program to start");
        }

        return "";
    }

    // Simplified caller method
    private static Object rpcCaller(String methodName, Object... args) {
        try (Socket socket = new Socket(server, PORT);
             OutputStream os = socket.getOutputStream();
             ObjectOutputStream oos = new ObjectOutputStream(os);
             InputStream fis = socket.getInputStream();
             ObjectInputStream ois = new ObjectInputStream(fis);) {

            RemoteMethod remoteMethod = new RemoteMethod(methodName, args, new Object[]{""});
            oos.writeObject(remoteMethod);
            oos.flush();

            RemoteMethod obj = (RemoteMethod) ois.readObject();
            Object[] results = obj.getResult();
            fis.close();

            return results[0];
        } catch (Exception err) {
            err.printStackTrace();
        }

        return null;
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
