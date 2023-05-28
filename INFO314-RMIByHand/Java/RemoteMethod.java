import java.io.Serializable;

public class RemoteMethod implements Serializable {
    public String methodName;
    public Object[] args;
    public Object[] result;

    // Construct our RPC object
    public RemoteMethod(String methodName, Object[] arguments, Object[] result) {
        this.methodName = methodName;
        this.args = arguments;
        this.result = result;
    }

    // For getting the mane of the arithmetic operation to run
    public String getMethodName() {
        return methodName;
    }

    // For getting the arguments to pass to the arithmetic operation
    public Object[] getArguments() {
        return args;
    }

    // For getting the result of the arithmetic operation
    public Object[] getResult() {
        return result;
    }
}