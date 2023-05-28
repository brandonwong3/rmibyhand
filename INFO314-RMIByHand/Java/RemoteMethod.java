import java.io.Serializable;

public class RemoteMethod implements Serializable {
    public String methodName;
    public Object[] args;

    // Construct our RPC object
    public RemoteMethod(String methodName, Object[] arguments) {
        this.methodName = methodName;
        this.args = arguments;
    }

    // For getting the mane of the arithmetic operation to run
    public String getMethodName() {
        return methodName;
    }

    // For getting the arguments to pass to the arithmetic operation
    public Object[] getArguments() {
        return args;
    }

}