import sys
from robot import run

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: robot_runner <test_file.robot>")
        sys.exit(1)

    test_file = sys.argv[1]
    run(test_file)
