from engine.client import Client
import sys


if __name__ == "__main__":
	try:
		args = sys.argv
		if len(args) != 3:
			print("Usage: python run_client.py <connection_type> <hostname> <port>")
			sys.exit(1)
		hostname = args[1]
		port = int(args[2])
		print("Running client...")
	except KeyboardInterrupt:
		print("Keyboard interrupt detected. Exiting...")
		sys.exit(0)
	except Exception as e:
		print(str(e))
		sys.exit(1)
